from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui import Ui_NewClient
from database import DbSocket
from datetime import datetime


class NewClient(QWidget, Ui_NewClient):
    Signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(NewClient, self).__init__(parent)
        self.setupUi(self)
        self.db = DbSocket()
        self.pushButton.setText(' Ajouter')
        self.pushButton.clicked.connect(self.add)

    def add(self):
        self.db.clientInsert(
            [self.nomLineEdit.text(), self.prenomLineEdit.text(), self.AgeSpinBox.value(), self.nTLPhoneLineEdit.text(),
             self.ancienSoldeLDubleSpinBox.value(), datetime.date(datetime.now())]
        )
        self.Signal.emit(True)
        self.close()
