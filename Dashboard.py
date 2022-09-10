import sys

from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, uic
from DataPeminjaman import WindowDataPeminjaman
from MasterBuku import WindowMasterBuku
from MasterPengguna import WindowMasterPengguna
from MasterPenulis import WindowMasterPenulis

Ui, QtBaseClass = uic.loadUiType("ui/Dashboard.ui")

class WindowDashboard(QtWidgets.QMainWindow, Ui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui.__init__(self)
        self.setupUi(self)

        self.iconMasterPengguna.setPixmap(QPixmap('icons/identification-card.png'))
        self.iconMasterBuku.setPixmap(QPixmap('icons/books.png'))
        self.iconMasterPenulis.setPixmap(QPixmap('icons/pen-nib.png'))
        self.iconDataPeminjamanBuku.setPixmap(QPixmap('icons/cardholder.png'))

        self.btnMasterPengguna.clicked.connect(self.openMasterPengguna)
        self.btnMasterBuku.clicked.connect(self.openMasterBuku)
        self.btnMasterPenulis.clicked.connect(self.openMasterPenulis)
        self.btnDataPeminjamanBuku.clicked.connect(self.openDataPeminjamanBuku)

    def openMasterPengguna(self):
        self.windowMasterPengguna = WindowMasterPengguna()
        self.windowMasterPengguna.show()
        return

    def openMasterBuku(self):
        self.windowMasterBuku = WindowMasterBuku()
        self.windowMasterBuku.show()
        return

    def openMasterPenulis(self):
        self.windowMasterPenulis = WindowMasterPenulis()
        self.windowMasterPenulis.show()
        return

    def openDataPeminjamanBuku(self):
        self.windowDataPeminjaman = WindowDataPeminjaman()
        self.windowDataPeminjaman.show()
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboard()
    window.show()
    sys.exit(app.exec())