# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/new_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewClient(object):
    def setupUi(self, NewClient):
        NewClient.setObjectName("NewClient")
        NewClient.resize(429, 236)
        NewClient.setMaximumSize(QtCore.QSize(429, 236))
        font = QtGui.QFont()
        font.setPointSize(10)
        NewClient.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewClient)
        self.verticalLayout.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nTLPhoneLineEdit = QtWidgets.QLineEdit(NewClient)
        self.nTLPhoneLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nTLPhoneLineEdit.setFont(font)
        self.nTLPhoneLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nTLPhoneLineEdit.setObjectName("nTLPhoneLineEdit")
        self.gridLayout.addWidget(self.nTLPhoneLineEdit, 2, 1, 1, 2)
        self.prenomLineEdit = QtWidgets.QLineEdit(NewClient)
        self.prenomLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prenomLineEdit.setFont(font)
        self.prenomLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.prenomLineEdit.setClearButtonEnabled(True)
        self.prenomLineEdit.setObjectName("prenomLineEdit")
        self.gridLayout.addWidget(self.prenomLineEdit, 1, 1, 1, 2)
        self.nomLineEdit = QtWidgets.QLineEdit(NewClient)
        self.nomLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomLineEdit.setFont(font)
        self.nomLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nomLineEdit.setClearButtonEnabled(True)
        self.nomLineEdit.setObjectName("nomLineEdit")
        self.gridLayout.addWidget(self.nomLineEdit, 0, 1, 1, 2)
        self.nomLabel = QtWidgets.QLabel(NewClient)
        self.nomLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomLabel.setFont(font)
        self.nomLabel.setObjectName("nomLabel")
        self.gridLayout.addWidget(self.nomLabel, 0, 0, 1, 1)
        self.prenomLabel = QtWidgets.QLabel(NewClient)
        self.prenomLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prenomLabel.setFont(font)
        self.prenomLabel.setObjectName("prenomLabel")
        self.gridLayout.addWidget(self.prenomLabel, 1, 0, 1, 1)
        self.nTLPhoneLabel = QtWidgets.QLabel(NewClient)
        self.nTLPhoneLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.nTLPhoneLabel.setObjectName("nTLPhoneLabel")
        self.gridLayout.addWidget(self.nTLPhoneLabel, 2, 0, 1, 1)
        self.ageLabel = QtWidgets.QLabel(NewClient)
        self.ageLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 3, 0, 1, 1)
        self.AgeSpinBox = QtWidgets.QSpinBox(NewClient)
        self.AgeSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.AgeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AgeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.AgeSpinBox.setMaximum(999)
        self.AgeSpinBox.setObjectName("AgeSpinBox")
        self.gridLayout.addWidget(self.AgeSpinBox, 3, 1, 1, 1)
        self.ancienSoldeLabel = QtWidgets.QLabel(NewClient)
        self.ancienSoldeLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.ancienSoldeLabel.setObjectName("ancienSoldeLabel")
        self.gridLayout.addWidget(self.ancienSoldeLabel, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(NewClient)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(NewClient)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 2)
        self.ancienSoldeLDubleSpinBox = QtWidgets.QDoubleSpinBox(NewClient)
        self.ancienSoldeLDubleSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.ancienSoldeLDubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ancienSoldeLDubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ancienSoldeLDubleSpinBox.setMaximum(1e+35)
        self.ancienSoldeLDubleSpinBox.setObjectName("ancienSoldeLDubleSpinBox")
        self.gridLayout.addWidget(self.ancienSoldeLDubleSpinBox, 4, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(NewClient)
        QtCore.QMetaObject.connectSlotsByName(NewClient)
        NewClient.setTabOrder(self.nomLineEdit, self.prenomLineEdit)
        NewClient.setTabOrder(self.prenomLineEdit, self.nTLPhoneLineEdit)
        NewClient.setTabOrder(self.nTLPhoneLineEdit, self.AgeSpinBox)
        NewClient.setTabOrder(self.AgeSpinBox, self.ancienSoldeLDubleSpinBox)
        NewClient.setTabOrder(self.ancienSoldeLDubleSpinBox, self.pushButton)

    def retranslateUi(self, NewClient):
        _translate = QtCore.QCoreApplication.translate
        NewClient.setWindowTitle(_translate("NewClient", "Nouveau client"))
        self.nomLabel.setText(_translate("NewClient", "Nom"))
        self.prenomLabel.setText(_translate("NewClient", "Prénom"))
        self.nTLPhoneLabel.setText(_translate("NewClient", "N° téléphone"))
        self.ageLabel.setText(_translate("NewClient", "Age"))
        self.ancienSoldeLabel.setText(_translate("NewClient", "Ancien solde"))
        self.label.setText(_translate("NewClient", "ans"))
        self.pushButton.setText(_translate("NewClient", "Ajouter"))