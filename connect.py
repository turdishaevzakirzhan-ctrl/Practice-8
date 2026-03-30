import psycopg2


def connect():
    return psycopg2.connect(
        dbname="phonebook",
        user="turdisaevzakirzan",
        host="localhost",
        port="5432"
    )