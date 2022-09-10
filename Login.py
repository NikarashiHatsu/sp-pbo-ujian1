import sys
import mysql.connector as mc

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from Dashboard import WindowDashboard
from models.User import User

Ui, QtBaseClass = uic.loadUiType("ui/login.ui")

class WindowLogin(QtWidgets.QMainWindow, Ui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui.__init__(self)
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister.clicked.connect(self.register)

    def login(self):
        user = User()
        user.username = self.txtLogUsername.text()
        user.password = self.txtLogPassword.text()

        try:
            if (user.login() == False):
                self.messagebox("ERROR", "Login gagal: " + user.message)
                return

            # Go to dashboard
            self.hide()
            self.windowDashboard = WindowDashboard()
            self.windowDashboard.show()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def register(self):
        user = User()
        user.username = self.txtRegUsername.text()
        user.password = self.txtRegPassword.text()
        user.confirmPassword = self.txtRegConfirmPassword.text()

        try:
            if (user.register() == False):
                self.messagebox("ERROR", "Register gagal: " + user.message)
                return

            self.messagebox("SUCCESS", "Register berhasil. Anda bisa login menggunakan akun Anda.")
            self.txtRegUsername.setText("")
            self.txtRegPassword.setText("")
            self.txtRegConfirmPassword.setText("")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.StandardButton.Ok)
        mess.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    window.show()
    sys.exit(app.exec())