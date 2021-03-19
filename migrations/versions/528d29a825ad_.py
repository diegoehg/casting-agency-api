"""empty message

Revision ID: 528d29a825ad
Revises: 2bfd3621e555
Create Date: 2021-03-18 23:17:35.222187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528d29a825ad'
down_revision = '2bfd3621e555'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actors')
    # ### end Alembic commands ###
