from models import Movie, Actor
from datetime import date


def load_data():
    Movie("Batman vs Superman", date(2016, 3, 16)).insert()
    Movie("Man of Steel", date(2013, 6, 24)).insert()
    Movie("Justice League", date(2017, 11, 17)).insert()
    Movie("Aquaman", date(2018, 12, 12)).insert()
    Movie("Wonder Woman", date(2017, 6, 17)).insert()

    Movie("Captain America: Civil War", date(2016, 4, 28)).insert()
    Movie("Captain America: The Winter Soldier", date(2014, 4, 14)).insert()
    Movie("Captain America", date(2011, 7, 29)).insert()
    Movie("Captain Marvel", date(2019, 3, 8)).insert()
    Movie("Wonder Woman 1984", date(2020, 12, 16)).insert()

    Movie("Ant-Man", date(2015, 7, 17)).insert()
    Movie("Doctor Strange", date(2016, 10, 28)).insert()
    Movie("Thor: Ragnarok", date(2017, 11, 3)).insert()
    Movie("Avengers: Infinity War", date(2018, 4, 28)).insert()
    Movie("Avengers: Endgame", date(2019, 4, 26)).insert()

    Movie("Joker", date(2019, 10, 4)).insert()
    Movie("Parasite", date(2019, 12, 25)).insert()
    Movie("Interstellar", date(2019, 11, 6)).insert()
    Movie("Inception", date(2010, 7, 23)).insert()
    Movie("The Dark Knight", date(2008, 7, 18)).insert()

    Actor("Elliot Page", 30, 'male').insert()
    Actor("Ellen Green", 28, 'female').insert()
    Actor("Brad Presley", 53, 'male').insert()
    Actor("Gina Morello", 42, 'female').insert()
    Actor("Romeo Tarantello", 22, 'male').insert()

    Actor("Leonardo Da Lima", 45, 'male').insert()
    Actor("Julia Richards", 33, 'female').insert()
    Actor("Antonio Margueritti", 65, 'male').insert()
    Actor("Diana Pratt", 27, 'female').insert()
    Actor("Don Draper", 43, 'male').insert()

    Actor("Ruth Badger", 65, 'female').insert()
    Actor("Rick Tracy", 78, 'male').insert()
    Actor("Sophie Laurent", 42, 'female').insert()
    Actor("John Raves", 42, 'male').insert()
    Actor("Megan Reagan", 38, 'female').insert()

    Actor("Juniper Lee", 17, 'female').insert()
    Actor("Kurt Cornell", 25, 'male').insert()
    Actor("Vanessa James", 24, 'female').insert()
    Actor("Ted Russell", 63, 'male').insert()
    Actor("Olivia Coleman", 40, 'female').insert()
