import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="industrial_db",
        user="postgres",
        password="leith",
        port=5432
    )