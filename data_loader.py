from models import Movie
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
