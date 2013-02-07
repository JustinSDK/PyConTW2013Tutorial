import shelve

class DVD:
    def __init__(self, title, year=None, duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'DVD({0}, {1}, {2}, {3})'.format(
            self.title, self.year, self.duration, self.director_id)

class DvdDao:
    def __init__(self, shelve_name):
        self.shelve_name = shelve_name

    def save(self, dvd):
        shelve_db = None
        try:
            shelve_db = shelve.open(self.shelve_name)
            shelve_db[dvd.title] = (dvd.year, dvd.duration, dvd.director_id)
            shelve_db.sync()
        finally:
            if shelve_db is not None:
                shelve_db.close()

    def all(self):
        shelve_db = None
        try:
            shelve_db = shelve.open(self.shelve_name)
            return [DVD(title, *shelve_db[title]) 
                    for title in sorted(shelve_db, key=str.lower)]
        finally:
            if shelve_db is not None:
                shelve_db.close()
        return []

    def load(self, title):
        shelve_db = None
        try:
            shelve_db = shelve.open(self.shelve_name)
            if title in shelve_db:
                return DVD(title, *shelve_db[title])
        finally:
            if shelve_db is not None:
                shelve_db.close()
        return None

    def remove(self, title):
        shelve_db = None
        try:
            shelve_db = shelve.open(self.shelve_name)
            del shelve_db[title]
            shelve_db.sync()
        finally:
            if shelve_db is not None:
                shelve_db.close()

def main():
    filename = 'dvd_library.slv'
    dao = DvdDao(filename)
    dvd1 = DVD('PyCon Tutorial 2012', 2012, 1, 'Justin Lin')
    dvd2 = DVD('PyCon Tutorial 2013', 2013, 1, 'Justin Lin')
    dao.save(dvd1)
    dao.save(dvd2)
    print dao.all()
    print dao.load('PyCon Tutorial 2012')
    dao.remove('PyCon Tutorial 2013')
    print dao.all()

if __name__ == '__main__':
    main()