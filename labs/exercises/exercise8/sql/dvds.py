import os.path
import sqlite3

def connect(name):
    create = not os.path.exists(name)
    conn = sqlite3.connect(name)
    if create:
        sql_directors = ("CREATE TABLE directors ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
            "name TEXT UNIQUE NOT NULL)")
        sql_dvds = ("CREATE TABLE dvds ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
            "title TEXT NOT NULL, "
            "year INTEGER NOT NULL, "
            "duration INTEGER NOT NULL, "
            "director_id INTEGER NOT NULL, "
            "FOREIGN KEY (director_id) REFERENCES directors)")
        
        # todo...

    return conn

def add_dvd(conn, title, year, duration, director):
    director_id = get_and_set_director(conn, director)
    sql = ("INSERT INTO dvds "
           "(title, year, duration, director_id) "
           "VALUES (?, ?, ?, ?)")
    # todo...

def get_and_set_director(conn, director):
    director_id = get_director_id(conn, director)
    if director_id is not None:
        return director_id
    cursor = conn.cursor()
    cursor.execute("INSERT INTO directors (name) VALUES (?)",
                   (director,))
    conn.commit()
    return get_director_id(conn, director)

def get_director_id(conn, director):
    sql = "SELECT id FROM directors WHERE name=?"
    # todo...
    
def all_dvds(conn):
    sql = ("SELECT dvds.title, dvds.year, dvds.duration, "
           "directors.name FROM dvds, directors "
           "WHERE dvds.director_id = directors.id"
           " ORDER BY dvds.title")
    # todo...

def all_directors(conn):
    sql = "SELECT name FROM directors ORDER BY name"
    # todo...
    

def main():
    db_name = 'dvd_library.sqlite3'
    conn = connect(db_name)
    add_dvd(conn, 'Python Tutorial 2013', 2013, 1, 'Justin')
    print all_directors(conn)
    print all_dvds(conn)

if __name__ == '__main__':
    main()