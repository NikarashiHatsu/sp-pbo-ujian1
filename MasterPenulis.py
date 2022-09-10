import datetime
import sys
import mysql.connector as mc

from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from models.Writer import Writer

Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/MasterPenulis.ui")

class WindowMasterPenulis(QtWidgets.QMainWindow, Ui_MainWindow):
    edit_mode: bool
    writer: Writer

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

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
            writers = Writer()
            result = writers.getAllData()

            self.gridMasterPengguna.setHorizontalHeaderLabels(['ID Penulis', 'Penulis', 'Tanggal Lahir', 'Path Thumbnail Buku', 'Tanggal Pembuatan', 'Tanggal Perubahan'])
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
            writer = Writer()
            writer.getById(id)
            affectedRows = writer.affected

            if (affectedRows != 0):
                self.writer = writer
                self.edit_mode = True

                self.txtName.setText(writer.name.strip())
                self.dateEditBirthDate.setDate(writer.birth_date)
                self.txtPicture.setText(writer.picture)
                self.thumbnail.setPixmap(QPixmap(writer.picture))

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
            writer = Writer()
            writer.name = self.txtName.text()
            writer.birth_date = self.dateEditBirthDate.date()
            writer.picture = self.txtPicture.text()

            if (self.edit_mode == True):
                self.updateData(writer)
                pass
            else:
                self.storeData(writer)

            self.select_data()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data " + e.msg)

    def storeData(self, writer: Writer):
        try:
            values = (writer.name, writer.birth_date.toString("yyyy-MM-dd"), writer.picture)
            sql = "INSERT INTO writers(name, birth_date, picture) VALUES " + str(values)
            writer.insert(sql)

            if (writer.affected == 0):
                self.messagebox("ERRRO", "Gagal menyimpan data: " + writer.message)
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def updateData(self, writer: Writer):
        try:
            values = (writer.name, writer.birth_date.toString("yyyy-MM-dd"), writer.picture, self.writer.id)
            sql = "UPDATE writers SET name = %s, birth_date = %s, picture = %s WHERE id = %s"
            writer.update(sql, values)

            if (writer.affected == 0):
                self.messagebox("ERROR", "Gagal mengupdate data: Tidak ada data yang diperbarui")
                return

            self.messagebox("SUCCESS", "Berhasil menyimpan data")
            self.clear_entry()
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def delete_data(self):
        try:
            sql = "DELETE FROM writers WHERE id = " + str(self.writer.id)
            self.writer.delete(sql)

            if (self.writer.affected == 0):
                self.messagebox("GAGAL", "Data gagal dihapus")
                return

            self.messagebox("SUKSES", "Data berhasil dihapus")
            self.select_data()
            self.clear_entry()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data: " + e.msg)

    def clear_entry(self):
        self.txtId.setText("")
        self.txtName.setText("")
        self.dateEditBirthDate.setDate(datetime.date(2000, 1, 1))
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
    window = WindowMasterPenulis()
    window.show()
    sys.exit(app.exec())