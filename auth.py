import os
import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen


auth0_domain = os.environ['AUTH0_DOMAIN']
algorithms = os.environ['ALGORITHMS']
api_audience = os.environ['API_AUDIENCE']


class AuthException(Exception):
    """
    Marks exception during authorization and token validation
    """
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """
    Reads the headers and extracts the authorization token from it
    :return: Authorization token
    """
    auth = request.headers.get('Authorization', None)

    if not auth:
        raise AuthException('Request does not contain authorization header', 401)

    auth_parts = auth.split()

    if auth_parts[0].lower() != 'bearer':
        raise AuthException('Authorization header must start with Bearer', 401)

    if len(auth_parts) == 1:
        raise AuthException('Authorization header has no token', 401)

    if len(auth_parts) != 2:
        raise AuthException('Authorization header must be bearer token', 401)

    return auth_parts[1]


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthException('Permissions not included in JWT', 400)

    if permission not in payload['permissions']:
        raise AuthException('Permission not found in JWT', 401)


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{auth0_domain}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthException('Authorization malformed.', 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=algorithms,
                audience=api_audience,
                issuer=f'https://{auth0_domain}/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthException('Token expired.', 401)

        except jwt.JWTClaimsError:
            raise AuthException(
                'Incorrect claims. Please, check the audience and issuer.',
                401
            )

        except Exception:
            raise AuthException('Unable to parse authentication token.', 400)

    raise AuthException('Unable to find the appropriate key.', 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
