from datetime import datetime
from hashlib import md5
from models.db import DBConnection as mydb

class Rent(mydb):
    id: str
    user_id: int
    book_id: int
    rent_duration: int

    def __init__(self):
        self.id = ''
        self.user_id = 0
        self.book_id = 0
        self.rent_duration = 0
        super().__init__()

    def getById(self, id):
        id = str(id).strip()
        sql = "SELECT * FROM rents WHERE id='" + id + "'"
        self.result = self.first(sql)

        if (self.result != None):
            self.id = self.result[0]
            self.user_id = self.result[1]
            self.book_id = self.result[2]
            self.rent_duration = self.result[3]
            self.affected = self.cursor.rowcount
        else:
            self.__init__()
            self.affected = 0
        return self.result

    def getAllData(self):
        sql = "SELECT rents.id, users.username, books.name, rents.rent_duration, rents.created_at, rents.updated_at FROM rents LEFT JOIN users ON rents.user_id = users.id LEFT JOIN books ON rents.book_id = books.id LIMIT 100"
        self.result = self.findAll(sql)
        return self.result