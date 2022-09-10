from datetime import datetime
from hashlib import md5
from models.db import DBConnection as mydb

class Writer(mydb):
    id: str
    name: str
    birth_date: datetime.date
    picture: str

    def __init__(self):
        self.id = ''
        self.name = ''
        self.birth_date = ''
        self.picture = ''
        super().__init__()

    def getById(self, id):
        id = str(id).strip()
        sql = "SELECT * FROM writers WHERE id='" + id + "'"
        self.result = self.first(sql)

        if (self.result != None):
            self.id = self.result[0]
            self.name = self.result[1]
            self.birth_date = self.result[2]
            self.picture = self.result[3]
            self.affected = self.cursor.rowcount
        else:
            self.__init__()
            self.affected = 0
        return self.result

    def getAllData(self):
        sql = "SELECT * FROM writers LIMIT 100"
        self.result = self.findAll(sql)
        return self.result