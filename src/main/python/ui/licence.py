# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/licence.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Licence(object):
    def setupUi(self, Licence):
        Licence.setObjectName("Licence")
        Licence.resize(395, 146)
        Licence.setMaximumSize(QtCore.QSize(395, 146))
        font = QtGui.QFont()
        font.setPointSize(10)
        Licence.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Licence)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Licence)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keyLineEdit = QtWidgets.QLineEdit(Licence)
        self.keyLineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.keyLineEdit.setFont(font)
        self.keyLineEdit.setText("")
        self.keyLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.horizontalLayout.addWidget(self.keyLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.validate_btn = QtWidgets.QPushButton(Licence)
        self.validate_btn.setMinimumSize(QtCore.QSize(200, 30))
        self.validate_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.validate_btn.setObjectName("validate_btn")
        self.horizontalLayout_2.addWidget(self.validate_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Licence)
        QtCore.QMetaObject.connectSlotsByName(Licence)

    def retranslateUi(self, Licence):
        _translate = QtCore.QCoreApplication.translate
        Licence.setWindowTitle(_translate("Licence", "PANORAMA OPTIC"))
        self.label.setText(_translate("Licence", "Tapez votre clé"))
        self.validate_btn.setText(_translate("Licence", "Valider"))