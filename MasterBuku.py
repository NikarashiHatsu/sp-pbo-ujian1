import sys
import mysql.connector as mc

from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from models.Book import Book
from models.Writer import Writer

Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/MasterBuku.ui")

class WindowMasterBuku(QtWidgets.QMainWindow, Ui_MainWindow):
    edit_mode: bool
    book: Book

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        writers = Writer()
        writers = writers.getAllData()
        for writer in writers:
            self.cboWriterId.addItem(writer[1], str(writer[0]))

        self.txtId.returnPressed.connect(self.search_data)
        self.btnCari.clicked.connect(self.search_data)
        self.btnFileUpload.clicked.connect(self.upload)
        self.btnSimpan.clicked.connect(self.save_data)
        self.btnHapus.clicked.connect(self.delete_data)

        self.edit_mode = False
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color: black; background-color: grey")
        self.select_data()

    def select_data(self):
        try:
            books = Book()
            result = books.getAllData()

            self.gridMasterPengguna.setHorizontalHeaderLabels(['ID Buku', 'Penulis', 'Judul Buku', 'Sinopsis', 'Path Thumbnail Buku', 'Jumlah Halaman', 'Harga Sewa', 'Tanggal Pembuatan', 'Tanggal Perubahan'])
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
            book = Book()
            book.getById(id)
            affectedRows = book.affected

            if (affectedRows != 0):
                self.book = book
                self.edit_mode = True

                self.cboWriterId.setCurrentIndex(self.cboWriterId.findData(str(book.writer_id)))
                self.txtName.setText(book.name.strip())
                self.txtPages.setText(str(book.pages))
                self.txtRentCost.setText(str(book.rent_cost))
                self.txtSynopsis.setText(book.synopsis)
                self.txtPicture.setText(book.picture)
                self.thumbnail.setPixmap(QPixmap(book.picture))

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
            book = Book()
            book.writer_id = self.cboWriterId.currentData()
            book.name = self.txtName.text()
            book.pages = int(self.txtPages.text())
            book.rent_cost = int(self.txtRentCost.text())
            book.synopsis = self.txtSynopsis.toPlainText()
            book.picture = self.txtPicture.text()

            if (self.edit_mode == True):
                self.updateData(book)
                pass
            else:
                self.storeData(book)

            self.select_data()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data " + e.msg)

    def storeData(self, book: Book):
        try:
            values = (book.writer_id, book.name, book.pages, book.rent_cost, book.synopsis, book.picture)
            sql = "INSERT INTO books(writer_id, name, pages, rent_cost, synopsis, picture) VALUES " + str(values)
            book.insert(sql)

            if (book.affected == 0):
                self.messagebox("ERRRO", "Gagal menyimpan data: " + book.message)
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def updateData(self, book: Book):
        try:
            values = (book.writer_id, book.name, book.pages, book.rent_cost, book.synopsis, book.picture, self.book.id)
            sql = "UPDATE books SET writer_id = %s, name = %s, pages = %s, rent_cost = %s, synopsis = %s, picture = %s WHERE id = %s"
            book.update(sql, values)

            if (book.affected == 0):
                self.messagebox("ERROR", "Gagal mengupdate data: Tidak ada data yang diperbarui")
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def delete_data(self):
        try:
            sql = "DELETE FROM books WHERE id = " + str(self.book.id)
            print(sql)
            self.book.delete(sql)

            if (self.book.affected == 0):
                self.messagebox("GAGAL", "Data gagal dihapus")
                return

            self.messagebox("SUKSES", "Data berhasil dihapus")
            self.select_data()
            self.clear_entry()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def clear_entry(self):
        self.cboWriterId.setCurrentIndex(0)
        self.txtId.setText("")
        self.txtName.setText("")
        self.txtPages.setText("")
        self.txtRentCost.setText("")
        self.txtSynopsis.setText("")
        self.txtPicture.setText("")
        self.thumbnail.setPixmap(QPixmap(""))
        self.btnSimpan.setText("Simpan")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color: black; background-color: grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.StandardButton.Ok)
        mess.exec()

    def upload(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Image files (*.jpg *jpeg *.gif *.png)")
        self.thumbnail.setPixmap(QPixmap(fname[0]))
        self.txtPicture.setText(fname[0])
        return fname[0]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowMasterBuku()
    window.show()
    sys.exit(app.exec())