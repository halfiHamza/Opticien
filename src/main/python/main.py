from datetime import datetime, date
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import Ui_MainWindow, Ui_Licence
from add_client import NewClient
from edit_client import EditClient
from templates import GenerateTemplate
from add_ordonnace import NewOrdonnace, EditOrdonnace
from client_situation import EditSituation
from database import DbSocket
from customTable import MyTableModel


import sys


class Licence(QWidget, Ui_Licence):
    Signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(Licence, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.validate_btn.clicked.connect(self.validate)

    def getKey(self, settings):
        self.settings = settings

    def validate(self):
        if self.keyLineEdit.text() == 'Q55B-8D00-9F0D-9C7A':
            self.settings.setValue("key", self.keyLineEdit.text())
            self.Signal.emit(True)
            self.close()
        else:
            QMessageBox.warning(
                self, "panorama optic", "Clé non valide", QMessageBox.Ok)


class Root(QMainWindow, Ui_MainWindow):
    def __init__(self, path, parent=None):
        super(Root, self).__init__(parent)
        self.setupUi(self)
        self.path = path
        self.settings = QSettings('panorama', 'optic')
        self.tabWidget.setTabIcon(
            0, QIcon(':/icons/src/main/resources/base/img/icons8_management_100px.png'))
        self.tabWidget.setTabIcon(
            1, QIcon(':/icons/src/main/resources/base/img/icons8_pie_chart_50px.png'))
        self.db = DbSocket()
        self.add_client = NewClient()
        self.add_ord = NewOrdonnace()
        self.edit_ord = EditOrdonnace()
        self.edit_ord.Signal.connect(self.reload_ord)
        self.edit_client = EditClient()
        self.edit_situation = EditSituation()
        self.license_ui = Licence()
        self.license_ui.Signal.connect(self.activeMainWindow)
        self.template = GenerateTemplate(self.path)
        self.add_client.Signal.connect(lambda: self.loadDb('All'))
        self.edit_client.Signal.connect(lambda: self.loadDb('All'))
        self.edit_situation.Signal.connect(lambda: self.loadDb('All'))
        self.add_ord.Signal.connect(self.directPrint)
        self.add_client_btn.clicked.connect(lambda: self.add_client.show())
        self.add_ord_btn.clicked.connect(self.ordonnance)
        self.edit_ord_btn.clicked.connect(self.edit_ord_func)
        self.remove_ord_btn.clicked.connect(self.remove_ord)
        self.edit_client_btn.clicked.connect(self.editClient)
        self.remove_client_btn.clicked.connect(self.deleteClient)
        self.situation_client_btn.clicked.connect(self.situation)
        self.print_bill_btn.clicked.connect(self.printer)
        self.pwd_tbtn.clicked.connect(self.changePwd)
        self.client_row = []
        self.ord_row = []
        self.day_row = []
        self.week_row = []
        self.month_row = []
        self.clientTableView.clicked.connect(self.loadOrdonnance)
        self.ordonnaceTableView.clicked.connect(self.getOrd)
        self.searchLineEdit.textChanged.connect(self.loadDb)

        self.dailyTableView.clicked.connect(self.loadDayDetails)
        # self.weeklyTableView.clicked.connect(self.loadWeekDetails)
        self.monthlyTableView.clicked.connect(self.loadMonthDetails)

        self.client_header = ['ID', 'Nom', 'Prenom',
                              'Age', 'N° téléphone', 'Dettes', 'Date']
        self.ord_header = [
            'N°', 'Date d’ordonnace', 'Correction od', 'Type verre od', 'Correction og', 'Type verre og', 'add og ',
            'ad dog', 'Remarque', 'Prix monture', 'Total', 'Verssemnt', 'Reste'
        ]
        self.daily_header = ['Journée', 'Montures Q', 'Totale']
        self.loadDb('All')
        self.weekly_header = [
            'Semaine N°', 'Début de la semaine', 'Montures Q', 'Totale']
        self.monthly_header = ['Date', 'Montures Q', 'Totale']
        self.details_header = ['Montures', 'De Prix']

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(self.ord_header)
        self.ordonnaceTableView.setModel(model)
        self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
        self.tabWidget.currentChanged.connect(self.statisticTab)
        self.license()
        self.pwdEdit = QShortcut(QKeySequence('Ctrl+Shift+P'), self)
        self.pwdEdit.activated.connect(self.changePwd)

    def changePwd(self):
        QInputDialog.setMinimumHeight(self, 100)
        pwd, okPressed = QInputDialog.getText(
            self, "panorama optic", "Changer le mot de passe", QLineEdit.Normal, "")
        if okPressed and pwd != '':
            self.db.execute_query(
                f"UPDATE pwd SET pwd = '{pwd}' WHERE id = 1")
            QMessageBox.warning(
                self, "panorama optic", "Votre mot de passe a changé", QMessageBox.Ok)
        else:
            QMessageBox.warning(
                self, "panorama optic", "Votre mot de passe n'a pas changé", QMessageBox.Ok)

    def statisticTab(self):
        if self.tabWidget.currentIndex() == 1:
            QInputDialog.setMinimumHeight(self, 100)
            while True:
                pwd, okPressed = QInputDialog.getText(
                    self, "panorama optic", "Entrer le mot de passe", QLineEdit.Password, "")
                if okPressed:
                    if pwd == self.db.execute_query("SELECT pwd FROM pwd")[0][0]:
                        self.dailyAmount()
                        # self.weeklyAmount()
                        self.monthlyAmount()
                        self.dayAmount()
                        self.stackedWidget.setCurrentIndex(0)
                        break
                    else:
                        QMessageBox.warning(
                            self, "panorama optic", "Mauvais mot de passe réessayer", QMessageBox.Ok)
                        continue
                else:
                    self.tabWidget.setCurrentIndex(0)
                    break
        else:
            self.stackedWidget.setCurrentIndex(1)

    def dayAmount(self):
        amount = self.db.cashActual()
        if amount:
            self.dayCash_label.setText(amount)
        else:
            self.dayCash_label.setText('0,00 Da')

    def dailyAmount(self):
        # _Get days and sum of each day_________
        result = self.db.dailyAmount()
        if result:
            model = MyTableModel(result[::-1], header=self.daily_header)
            self.dailyTableView.setModel(model)
            self.dailyTableView.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.daily_header)
            self.dailyTableView.setModel(model)
            self.dailyTableView.horizontalHeader().setFixedHeight(30)

    # def weeklyAmount(self):
    #     # _Get weeks and sum of each week________
    #     result = self.db.weeklyAmount()
    #     if result:
    #         model = MyTableModel(result[::-1], header=self.weekly_header)
    #         self.weeklyTableView.setModel(model)
    #         self.weeklyTableView.horizontalHeader().setFixedHeight(30)
    #     else:
    #         model = QStandardItemModel()
    #         model.setHorizontalHeaderLabels(self.weekly_header)
    #         self.weeklyTableView.setModel(model)
    #         self.weeklyTableView.horizontalHeader().setFixedHeight(30)

    def monthlyAmount(self):
        # _Get months and sum of each month______
        result = self.db.monthlyAmount()
        if result:
            model = MyTableModel(result[::-1], header=self.monthly_header)
            self.monthlyTableView.setModel(model)
            self.monthlyTableView.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.monthly_header)
            self.monthlyTableView.setModel(model)
            self.monthlyTableView.horizontalHeader().setFixedHeight(30)

    @pyqtSlot(bool)
    def reload_ord(self, cond):
        if cond:
            ordonnaces = self.db.ordSelect(self.client_row[0])
            if ordonnaces:
                model = MyTableModel(ordonnaces, header=self.ord_header)
                self.ordonnaceTableView.setModel(model)
                self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
            else:
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(self.ord_header)
                self.ordonnaceTableView.setModel(model)
                self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
    
    def remove_ord(self):
        if self.ord_row:
            replay = QMessageBox.question(
                self, "Panorama Optic", "êtes-vous sûr de vouloir supprimer cette ordonnance", QMessageBox.Yes, QMessageBox.No)
            if replay == QMessageBox.Yes:
                self.db.execute_query(
                    f"DELETE FROM ordonnaces WHERE id = {self.ord_row[0]}"
                )
                ordonnaces = self.db.ordSelect(self.client_row[0])
                if ordonnaces:
                    model = MyTableModel(ordonnaces, header=self.ord_header)
                    self.ordonnaceTableView.setModel(model)
                    self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
                else:
                    model = QStandardItemModel()
                    model.setHorizontalHeaderLabels(self.ord_header)
                    self.ordonnaceTableView.setModel(model)
                    self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)

    @pyqtSlot(list)
    def directPrint(self, data):
        self.loadDb('All')
        if data:
            self.template.receipt(
                data=data
            )
            self.template.show()

    def printer(self):
        if self.ord_row:
            self.template.receipt(
                data=[self.client_row[1] + ' ' + self.client_row[2], self.ord_row[9], self.ord_row[3],
                      self.ord_row[5], self.ord_row[8], self.ord_row[-3], self.ord_row[-2], self.ord_row[1],
                      self.client_row[4], self.ord_row[2], self.ord_row[4]]
            )
            self.template.show()

    def getOrd(self, index):
        self.ord_row.clear()
        for value in range(len(self.ord_header)):
            item = self.ordonnaceTableView.model().index(index.row(), value)
            self.ord_row.append(
                self.ordonnaceTableView.model().data(item, Qt.DisplayRole)
            )

    def loadDb(self, text):
        # _Select clients form database______________
        if text == 'All':
            result = self.db.execute_query(
                "SELECT id, first_name, last_name, age, phone, CONCAT(CAST(debt AS CHAR), ' Da'), DATE_FORMAT(date, '%d-%M-%Y') FROM clients;")
        else:
            result = self.db.execute_query(
                f"SELECT id, first_name, last_name, age, phone, CONCAT(CAST(debt AS CHAR), ' Da'), DATE_FORMAT(date, '%d-%M-%Y') from clients where first_name like '{text}%' or last_name like '{text}%' or age like '{text}%' or phone like '{text}%'"
            )
        # _Display clients in table_______________
        if result:
            model = MyTableModel(result, header=self.client_header)
            self.clientTableView.setModel(model)
            self.clientTableView.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.client_header)
            self.clientTableView.setModel(model)
            self.clientTableView.horizontalHeader().setFixedHeight(30)

    def loadDayDetails(self, index):
        self.day_row.clear()
        for value in range(len(self.daily_header)):
            item = self.dailyTableView.model().index(index.row(), value)
            self.day_row.append(
                self.dailyTableView.model().data(item, Qt.DisplayRole)
            )
        dayDetails = self.db.dayDetails(self.day_row[0])
        if dayDetails:
            model = MyTableModel(dayDetails, header=self.details_header)
            self.dailyTableView_2.setModel(model)
            self.dailyTableView_2.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.details_header)
            self.dailyTableView_2.setModel(model)
            self.dailyTableView_2.horizontalHeader().setFixedHeight(30)

    # def loadWeekDetails(self, index):
    #     self.week_row.clear()
    #     for value in range(len(self.weekly_header)):
    #         item = self.weeklyTableView.model().index(index.row(), value)
    #         self.week_row.append(
    #             self.weeklyTableView.model().data(item, Qt.DisplayRole)
    #         )
    #     weekDetails = self.db.weekDetails(self.week_row[0], self.week_row[1])
    #     if weekDetails:
    #         model = MyTableModel(weekDetails, header=self.details_header)
    #         self.weeklyTableView_2.setModel(model)
    #         self.weeklyTableView_2.horizontalHeader().setFixedHeight(30)
    #     else:
    #         model = QStandardItemModel()
    #         model.setHorizontalHeaderLabels(self.details_header)
    #         self.weeklyTableView_2.setModel(model)
    #         self.weeklyTableView_2.horizontalHeader().setFixedHeight(30)

    def loadMonthDetails(self, index):
        self.month_row.clear()
        for value in range(len(self.monthly_header)):
            item = self.monthlyTableView.model().index(index.row(), value)
            self.month_row.append(
                self.monthlyTableView.model().data(item, Qt.DisplayRole)
            )
        monthDetails = self.db.monthDetails(self.month_row[0])
        if monthDetails:
            model = MyTableModel(monthDetails, header=self.details_header)
            self.monthlyTableView_2.setModel(model)
            self.monthlyTableView_2.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.details_header)
            self.monthlyTableView_2.setModel(model)
            self.monthlyTableView_2.horizontalHeader().setFixedHeight(30)

    def loadOrdonnance(self, index=None):
        self.client_row.clear()
        for value in range(len(self.ord_header)):
            item = self.clientTableView.model().index(index.row(), value)
            self.client_row.append(
                self.clientTableView.model().data(item, Qt.DisplayRole)
            )
        ordonnaces = self.db.ordSelect(self.client_row[0])
        if ordonnaces:
            model = MyTableModel(ordonnaces, header=self.ord_header)
            self.ordonnaceTableView.setModel(model)
            self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
        else:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.ord_header)
            self.ordonnaceTableView.setModel(model)
            self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)

    def ordonnance(self):
        if self.client_row:
            self.add_ord.setId(self.client_row[0])
            self.add_ord.defaultUi()
            self.add_ord.show()
    
    def edit_ord_func(self):
        if self.ord_row:
            self.edit_ord.data(ordonence=self.ord_row)
            self.edit_ord.fillForm()
            self.edit_ord.show()

    def editClient(self):
        if self.client_row:
            self.edit_client.setId(self.client_row[0])
            self.edit_client.setData(self.db.getClient(self.client_row[0])[0])
            self.edit_client.show()

    def deleteClient(self):
        client = self.db.execute_query(
            f"SELECT first_name, last_name FROM clients WHERE id = {self.client_row[0]}")
        replay = QMessageBox.question(
            self, 'PANORAMA OPTIC', f"Êtes-vous sûr de vouloir supprimer ce client\n{' '.join(client[0])}",
            QMessageBox.Yes, QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.db.deleteClient(self.client_row[0])
            self.loadDb('All')
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.ord_header)
            self.ordonnaceTableView.setModel(model)
            self.ordonnaceTableView.horizontalHeader().setFixedHeight(30)
        else:
            pass

    def situation(self):
        self.edit_situation.setId(self.client_row[0])
        self.edit_situation.getDebts()
        self.edit_situation.show()

    def license(self):
        if not self.settings.contains('key'):
            if not self.settings.contains('date'):
                self.settings.setValue('date', datetime.now().date().strftime(
                    '%d/%m/%Y'))
            else:
                d, m, y = self.settings.value('date').split('/')
                d1, m1, y1 = datetime.now().date().strftime('%d/%m/%Y').split('/')
                dt = date(int(y), int(m), int(d))
                dt1 = date(int(y1), int(m1), int(d1))
                delta = (dt1-dt).days
                if abs(delta) >= 5:
                    self.setEnabled(False)
                    self.license_ui.getKey(self.settings)
                    self.license_ui.show()

    @pyqtSlot(bool)
    def activeMainWindow(self, active):
        if active:
            self.setEnabled(True)


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    QFontDatabase.addApplicationFont(appctxt.get_resource(
        "template").replace("\\", "/")+"\\webfonts\\ImprintMTShadow.ttf")
    window = Root(appctxt.get_resource("template").replace("\\", "/"))
    window.showMaximized()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
