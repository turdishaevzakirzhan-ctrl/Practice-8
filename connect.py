import psycopg2


def connect():
    return psycopg2.connect(
        dbname="phonebook",
        user="turdisaevzakirzan",
        password="",
        host="5432"
    )