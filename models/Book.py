from hashlib import md5
from models.db import DBConnection as mydb

class Book(mydb):
    id: str
    writer_id: int
    name: str
    synopsis: str
    picture: str
    pages: int
    rent_cost: int
    message: str

    def __init__(self):
        self.id = ''
        self.writer_id = 0
        self.name = ''
        self.synopsis = ''
        self.picture = ''
        self.pages = 0
        self.rent_cost = 0
        self.message = ''
        super().__init__()

    def getById(self, id):
        id = str(id).strip()
        sql = "SELECT * FROM books WHERE id='" + id + "'"
        self.result = self.first(sql)

        if (self.result != None):
            self.id = self.result[0]
            self.writer_id = self.result[1]
            self.name = self.result[2]
            self.synopsis = self.result[3]
            self.picture = self.result[4]
            self.pages = self.result[5]
            self.rent_cost = self.result[6]
            self.affected = self.cursor.rowcount
        else:
            self.__init__()
            self.affected = 0
        return self.result

    def getAllData(self):
        sql = "SELECT books.id, writers.name, books.name, synopsis, books.picture, pages, rent_cost, books.created_at, books.updated_at FROM books LEFT JOIN writers ON books.writer_id = writers.id LIMIT 100"
        self.result = self.findAll(sql)
        return self.result