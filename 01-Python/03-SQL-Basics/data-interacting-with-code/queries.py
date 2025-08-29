# pylint: disable=missing-docstring, C0103

import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
database = conn.cursor()


def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT count(directors.name) FROM directors"
    db.execute(query)
    results = db.fetchall()
    return results[0][0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "SELECT directors.name FROM directors"
    db.execute(query)
    results = db.fetchall()
    lista = []

    for result in results:
        lista.append(result[0])

    return sorted(lista)


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """SELECT title FROM movies
WHERE UPPER(movies.title) LIKE '% LOVE %'
OR UPPER(movies.title) LIKE '% LOVE.%'
OR UPPER(movies.title) LIKE '% LOVE,%'
OR UPPER(movies.title) LIKE '% LOVE''%'
OR UPPER(movies.title) LIKE 'LOVE,%'
OR UPPER(movies.title) LIKE 'LOVE.%'
OR UPPER(movies.title) LIKE '%''LOVE%'
OR UPPER(movies.title) LIKE '% LOVE'
OR UPPER(movies.title) LIKE 'LOVE %'
OR UPPER(movies.title) = 'LOVE'
ORDER BY movies.title"""
    db.execute(query)
    results = db.fetchall()
    lista = []

    for result in results:
        lista.append(result[0])

    return sorted(lista)


def directors_named_like_count(db,name):
    # return the number of directors which contain a given word in their name
    query = "SELECT count(name) FROM directors WHERE directors.name LIKE ?"
    db.execute(query, (f"%{name}%",))
    results = db.fetchall()
    return results[0][0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = """SELECT title, minutes FROM movies
    WHERE minutes >= ?
    ORDER BY movies.title"""

    db.execute(query, (min_length,))
    results = db.fetchall()
    lista = []
    for result in results:
        lista.append(result[0])
    return sorted(lista)
