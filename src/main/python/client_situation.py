from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui import Ui_Reglement
from database import DbSocket


class EditSituation(QWidget, Ui_Reglement):
    Signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(EditSituation, self).__init__(parent)
        self.setupUi(self)
        self.db = DbSocket()
        self.pushButton.clicked.connect(self.edit)
        self.verssemntDoubleSpinBox.valueChanged.connect(self.calcDebts)
        self.debt = 0

    def setId(self, id):
        self.id = id

    def getDebts(self):
        self.debt = self.db.execute_query(
            f"SELECT debt FROM clients WHERE id = {self.id}"
        )[0][0]
        self.dettesDoubleSpinBox.setValue(self.debt)

    def edit(self):
        self.db.execute_query(
            f"UPDATE clients SET debt = '{self.dettesDoubleSpinBox.value()}' WHERE id = {self.id}"
        )
        self.Signal.emit(True)
        self.close()

    def calcDebts(self):
        self.dettesDoubleSpinBox.setValue(
            float(self.debt) - self.verssemntDoubleSpinBox.value()
        )
