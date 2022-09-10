import sys
import mysql.connector as mc

from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from models.Book import Book
from models.User import User
from models.Rent import Rent

Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/DataPeminjaman.ui")

class WindowDataPeminjaman(QtWidgets.QMainWindow, Ui_MainWindow):
    edit_mode: bool
    rent: Rent
    books: Book

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        books = Book()
        books = books.getAllData()
        self.books = books
        for book in books:
            self.cboBookId.addItem(book[2], str(book[0]))

        users = User()
        users = users.getAllData()
        for user in users:
            self.cboUserId.addItem(user[1], str(user[0]))

        self.txtId.returnPressed.connect(self.search_data)
        self.btnCari.clicked.connect(self.search_data)
        self.btnHitungSewa.clicked.connect(self.hitungSewa)
        self.btnSimpan.clicked.connect(self.save_data)
        self.btnHapus.clicked.connect(self.delete_data)

        self.edit_mode = False
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color: black; background-color: grey")
        self.select_data()

    def select_data(self):
        try:
            rents = Rent()
            result = rents.getAllData()

            self.gridMasterPengguna.setHorizontalHeaderLabels(['ID Peminjaman', 'Nama Peminjam', 'Judul Buku', 'Durasi Peminjaman (Minggu)', 'Tanggal Pembuatan', 'Tanggal Perubahan'])
            self.gridMasterPengguna.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.gridMasterPengguna.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridMasterPengguna.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def search_data(self):
        try:
            id = self.txtId.text()
            rent = Rent()
            rent.getById(id)
            affectedRows = rent.affected

            if (affectedRows != 0):
                self.rent = rent
                self.edit_mode = True

                self.cboUserId.setCurrentIndex(self.cboUserId.findData(str(rent.user_id)))
                self.cboBookId.setCurrentIndex(self.cboBookId.findData(str(rent.book_id)))
                self.txtRentDuration.setText(str(rent.rent_duration))
                self.txtSubtotal.setText(str(rent.rent_duration * self.books[self.cboBookId.currentIndex()][6]))

                self.btnHapus.setEnabled(True)
                self.btnSimpan.setText('Update')
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet('color: white; background-color: red')
            else:
                self.edit_mode = False
                self.messagebox("ERROR", 'Data tidak ditemukan')

                self.txtId.setFocus()

                self.clear_entry()
                self.btnSimpan.setText('Simpan')
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet('color: black; background-color: grey')

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def save_data(self):
        try:
            rent = Rent()
            rent.user_id = self.cboUserId.currentData()
            rent.book_id = self.cboBookId.currentData()
            rent.rent_duration = self.txtRentDuration.text()

            if (self.edit_mode == True):
                self.updateData(rent)
                pass
            else:
                self.storeData(rent)

            self.select_data()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data " + e.msg)

    def storeData(self, rent: Rent):
        try:
            values = (rent.user_id, rent.book_id, rent.rent_duration)
            sql = "INSERT INTO rents(user_id, book_id, rent_duration) VALUES " + str(values)
            rent.insert(sql)

            if (rent.affected == 0):
                self.messagebox("ERRRO", "Gagal menyimpan data: " + rent.message)
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def hitungSewa(self):
        rentDuration = int(self.txtRentDuration.text())
        rentPrice = int(self.books[self.cboBookId.currentIndex()][6])
        self.txtSubtotal.setText(str(rentPrice * rentDuration))
        return

    def updateData(self, rent: Rent):
        try:
            values = (rent.user_id, rent.book_id, rent.rent_duration, self.rent.id)
            sql = "UPDATE rents SET user_id = %s, book_id = %s, rent_duration = %s WHERE id = %s"
            rent.update(sql, values)

            if (rent.affected == 0):
                self.messagebox("ERROR", "Gagal mengupdate data: Tidak ada data yang diperbarui")
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def delete_data(self):
        try:
            sql = "DELETE FROM rents WHERE id = " + str(self.rent.id)
            self.rent.delete(sql)

            if (self.rent.affected == 0):
                self.messagebox("GAGAL", "Data gagal dihapus")
                return

            self.messagebox("SUKSES", "Data berhasil dihapus")
            self.select_data()
            self.clear_entry()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def clear_entry(self):
        self.cboUserId.setCurrentIndex(0)
        self.cboBookId.setCurrentIndex(0)
        self.txtRentDuration.setText("")
        self.txtSubtotal.setText("")
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
    window = WindowDataPeminjaman()
    window.show()
    sys.exit(app.exec())