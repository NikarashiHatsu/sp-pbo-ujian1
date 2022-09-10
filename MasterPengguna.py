import sys
import mysql.connector as mc

from hashlib import md5
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from models.User import User

Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/MasterUser.ui")

class WindowMasterPengguna(QtWidgets.QMainWindow, Ui_MainWindow):
    edit_mode: bool
    user: User

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.txtUsername.returnPressed.connect(self.search_data)
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.btnHapus.clicked.connect(self.delete_data)

        self.edit_mode = False
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color: black; background-color: grey")
        self.select_data()

    def select_data(self):
        try:
            users = User()
            result = users.getAllData()

            self.gridMasterPengguna.setHorizontalHeaderLabels(['ID', 'Username', 'Tanggal Pembuatan', 'Tanggal Perubahan'])
            self.gridMasterPengguna.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.gridMasterPengguna.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridMasterPengguna.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def search_data(self):
        try:
            username = self.txtUsername.text()
            user = User()
            user.getByUsername(username)
            affectedRows = user.affected

            if (affectedRows != 0):
                self.user = user
                self.edit_mode = True
                self.txtUsername.setText(user.username.strip())
                self.btnHapus.setEnabled(True)
                self.btnSimpan.setText('Update')
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet('color: white; background-color: red')
            else:
                self.edit_mode = False
                self.messagebox("ERROR", 'Data tidak ditemukan')
                self.txtUsername.setFocus()
                self.btnSimpan.setText('Simpan')
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet('color: black; background-color: grey')

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def save_data(self):
        try:
            user = User()
            user.username = self.txtUsername.text()
            user.password = self.txtPassword.text()
            user.confirmPassword = self.txtKonfirmasiPassword.text()

            if (self.edit_mode == True):
                self.updateData(user)
            else:
                self.storeData(user)

            self.select_data()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data " + e.msg)

    def storeData(self, user: User):
        try:
            if (user.register() == False):
                self.messagebox("ERROR", "Gagal menyimpan data: " + user.message)
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.txtUsername.setText("")
            self.txtPassword.setText("")
            self.txtKonfirmasiPassword.setText("")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def updateData(self, user: User):
        try:
            if (user.password != user.confirmPassword):
                self.messagebox("ERROR", "Password dan konfirmasi password tidak sama")
                return

            values = (user.username, md5(user.password.encode()).hexdigest(), self.user.id)
            sql = "UPDATE users SET username = %s, password = %s WHERE id = %s"
            user.update(sql, values)

            if (user.affected == 0):
                self.messagebox("ERROR", "Gagal mengupdate data: Tidak ada data yang diperbarui")
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.txtUsername.setText("")
            self.txtPassword.setText("")
            self.txtKonfirmasiPassword.setText("")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def delete_data(self):
        try:
            sql = "DELETE FROM users WHERE id = " + self.user.id
            self.user.delete(sql)

            if (self.user.affected == 0):
                self.messagebox("GAGAL", "Data gagal dihapus")
                return

            self.messagebox("SUKSES", "Data berhasil dihapus")
            self.select_data()
            self.clear_entry()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def clear_entry(self):
        self.txtUsername.setText('')
        self.txtPassword.setText('')
        self.txtKonfirmasiPassword.setText('')
        self.btnSimpan.setText("Simpan")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color: black; background-color: grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.StandardButton.Ok)
        mess.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowMasterPengguna()
    window.show()
    sys.exit(app.exec())