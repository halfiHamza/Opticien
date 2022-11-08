from PyQt5.QtWidgets import QWidget
from ui import Ui_NewOrdonnace
from PyQt5.QtCore import pyqtSignal
from database import DbSocket
from PyQt5.QtCore import *
import calendar
from re import findall


class NewOrdonnace(QWidget, Ui_NewOrdonnace):
    Signal = pyqtSignal(list)

    def __init__(self):
        super(NewOrdonnace, self).__init__()
        self.setupUi(self)
        self.id = 0
        self.db = DbSocket()
        self.dateEdit.setDate(QDate.currentDate())
        self.Ajouter_btn.clicked.connect(self.add)
        self.verssemntDoubleSpinBox.valueChanged.connect(self.calcSolde)

    def setId(self, id):
        self.id = id

    # _Get week number ______________
    def month_week(self):
        date = self.dateEdit.date().toPyDate().strftime("%Y/%m/%d")
        date = date.split("/")
        calendar.setfirstweekday(calendar.SATURDAY)
        month = calendar.monthcalendar(int(date[0]), int(date[1]))
        for i, week in enumerate(month):
            for day in week:
                if day == int(date[2]):
                    return [str(date[0]+'-'+date[1]), i + 1]

    def add(self):
        self.db.ordInsert(
            [
                self.id, self.dateEdit.date().toPyDate(), self.correctionOdLineEdit.text(),
                self.typeVerreOdLineEdit.text(), self.correctionOgLineEdit.text(
                ), self.typeVerreOGLineEdit.text(),
                self.addOgLineEdit.text(), self.adDogLineEdit.text(
                ), self.plainTextEdit.toPlainText(), self.prixMontureDoubleSpinBox.value(),
                self.totalDoubleSpinBox.value(), self.verssemntDoubleSpinBox.value(
                ), self.resteDoubleSpinBox.value()
            ]
        )
        phone = self.db.execute_query(
            f"SELECT phone FROM clients WHERE id = {self.id}")
        if phone:
            phone = phone[0][0]
        self.Signal.emit([
            ' '.join(self.db.execute_query(
                f"SELECT first_name, last_name FROM clients WHERE id = {self.id}")[0]
            ),
            self.prixMontureDoubleSpinBox.value(), self.typeVerreOdLineEdit.text(),
            self.typeVerreOGLineEdit.text(), self.plainTextEdit.toPlainText(),
            self.totalDoubleSpinBox.value(), self.verssemntDoubleSpinBox.value(),
            self.dateEdit.date().toPyDate().strftime(
                "%d/%m/%Y"), phone, self.correctionOdLineEdit.text(), self.correctionOgLineEdit.text()
        ])
        self.close()

    def calcSolde(self):
        self.resteDoubleSpinBox.setValue(
            self.totalDoubleSpinBox.value() - self.verssemntDoubleSpinBox.value()
        )

    def defaultUi(self):
        self.dateEdit.setDate(QDate.currentDate())
        self.correctionOdLineEdit.clear(),
        self.typeVerreOdLineEdit.clear(),
        self.correctionOgLineEdit.clear(),
        self.typeVerreOGLineEdit.clear(),
        self.addOgLineEdit.clear(),
        self.adDogLineEdit.clear(),
        self.plainTextEdit.clear(),
        self.prixMontureDoubleSpinBox.setValue(0.00),
        self.totalDoubleSpinBox.setValue(0.00),
        self.verssemntDoubleSpinBox.setValue(0.00),
        self.resteDoubleSpinBox.setValue(0.00)



class EditOrdonnace(QWidget, Ui_NewOrdonnace):
    Signal = pyqtSignal(bool)

    def __init__(self):
        super(EditOrdonnace, self).__init__()
        self.setupUi(self)
        self.db = DbSocket()
        self.dateEdit.setDate(QDate.currentDate())
        self.Ajouter_btn.clicked.connect(self.add)
        self.verssemntDoubleSpinBox.valueChanged.connect(self.calcSolde)
        self.Ajouter_btn.setText('Éditer')
        self.ordonence = None

    def data(self, ordonence):
        self.ordonence = ordonence

    # _Get week number ______________
    def month_week(self):
        date = self.dateEdit.date().toPyDate().strftime("%Y/%m/%d")
        date = date.split("/")
        calendar.setfirstweekday(calendar.SATURDAY)
        month = calendar.monthcalendar(int(date[0]), int(date[1]))
        for i, week in enumerate(month):
            for day in week:
                if day == int(date[2]):
                    return [str(date[0]+'-'+date[1]), i + 1]

    def add(self):
        self.db.ordEdit(
            [
                self.ordonence[0], self.dateEdit.date().toPyDate(), self.correctionOdLineEdit.text(),
                self.typeVerreOdLineEdit.text(), self.correctionOgLineEdit.text(
                ), self.typeVerreOGLineEdit.text(),
                self.addOgLineEdit.text(), self.adDogLineEdit.text(
                ), self.plainTextEdit.toPlainText(), self.prixMontureDoubleSpinBox.value(),
                self.totalDoubleSpinBox.value(), self.verssemntDoubleSpinBox.value(
                ), self.resteDoubleSpinBox.value()
            ]
        )
        self.Signal.emit(True)
        self.close()

    def calcSolde(self):
        self.resteDoubleSpinBox.setValue(
            self.totalDoubleSpinBox.value() - self.verssemntDoubleSpinBox.value()
        )

    def fillForm(self):
        if self.ordonence:
            # convert str to QDate
            qdate = QDate.fromString(self.ordonence[1], "d-MMM-yyyy")
            self.dateEdit.setDate(qdate)
            self.correctionOdLineEdit.setText(self.ordonence[2]),
            self.typeVerreOdLineEdit.setText(self.ordonence[3]),
            self.correctionOgLineEdit.setText(self.ordonence[4]),
            self.typeVerreOGLineEdit.setText(self.ordonence[5]),
            self.addOgLineEdit.setText(self.ordonence[6]),
            self.adDogLineEdit.setText(self.ordonence[7]),
            self.plainTextEdit.setPlainText(self.ordonence[8]),
            self.prixMontureDoubleSpinBox.setValue(float(findall(r'-?\d+', self.ordonence[9])[0])),
            self.totalDoubleSpinBox.setValue(float(findall(r'-?\d+', self.ordonence[10])[0])),
            self.verssemntDoubleSpinBox.setValue(float(findall(r'-?\d+', self.ordonence[11])[0])),
            self.resteDoubleSpinBox.setValue(float(findall(r'-?\d+', self.ordonence[12])[0]))
