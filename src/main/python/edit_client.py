from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui import Ui_NewClient
from database import DbSocket


class EditClient(QWidget, Ui_NewClient):
    Signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(EditClient, self).__init__(parent)
        self.setupUi(self)
        self.db = DbSocket()
        self.setWindowTitle('Modifier client')
        self.pushButton.setText(' Modifier')
        self.pushButton.clicked.connect(self.edit)

    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.nomLineEdit.setText(data[1])
        self.prenomLineEdit.setText(data[2])
        self.AgeSpinBox.setValue(data[3])
        self.ancienSoldeLDubleSpinBox.setValue(data[4])
        self.nTLPhoneLineEdit.setText(data[5])

    def edit(self):
        self.db.editClient(
            self.id, [self.nomLineEdit.text(), self.prenomLineEdit.text(), self.AgeSpinBox.value(),
                      self.ancienSoldeLDubleSpinBox.value(), self.nTLPhoneLineEdit.text()]
        )
        self.Signal.emit(True)
        self.close()
