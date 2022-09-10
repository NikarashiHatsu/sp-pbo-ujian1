from hashlib import md5
from models.db import DBConnection as mydb

class User(mydb):
    id: str
    username: str
    password: str
    confirmPassword: str
    message: str

    def __init__(self):
        self.id = ''
        self.username = ''
        self.password = ''
        self.confirmPassword = ''
        self.message = ''
        super().__init__()

    def login(self) -> bool:
        # Search the users with corresponding username
        sql = "SELECT * FROM users WHERE username = '" + self.username + "'"
        self.affected = self.first(sql)

        if (self.affected == None):
            self.message = "Username tidak ditemukan"
            return False;

        if (self.affected[2] != md5(self.password.encode()).hexdigest()):
            self.message = "Password salah"
            return False;

        return True

    def register(self) -> bool:
        # Search the users with corresponding username
        sql = "SELECT * FROM users WHERE username = '" + self.username + "'"
        self.affected = self.first(sql)

        if (self.affected != None):
            self.message = "Username sudah ada pada database, silahkan gunakan username lain"
            return False;

        if (self.password != self.confirmPassword):
            self.message = "Password Yang anda masukkan tidak sama"
            return False;

        values = (self.username, md5(self.password.encode()).hexdigest())
        sql = "INSERT users(username, password) VALUES " + str(values)
        self.affected = self.insert(sql)

        if (self.affected == None):
            self.message = "Terjadi kegagalan pada saat memasukkan data ke database"
            return False

        return True

    def getByUsername(self, username):
        username = str(username).strip()
        sql = "SELECT * FROM users WHERE username='" + username + "'"
        self.result = self.first(sql)

        if (self.result != None):
            self.id = str(self.result[0])
            self.username = self.result[1]
            self.affected = self.cursor.rowcount
        else:
            self.id = ''
            self.username = ''
            self.affected = 0
        return self.result

    def getAllData(self):
        sql = "SELECT id, username, created_at, updated_at FROM users LIMIT 100"
        self.result = self.findAll(sql)
        return self.result