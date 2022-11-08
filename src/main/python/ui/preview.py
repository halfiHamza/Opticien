# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/preview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName("Preview")
        Preview.resize(790, 590)
        Preview.setMaximumSize(QtCore.QSize(790, 590))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Preview)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Preview)
        self.frame.setStyleSheet("#frame {\n"
"border:1px solid rgb(42, 130, 218);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webview = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.webview.setObjectName("webview")
        self.horizontalLayout_2.addWidget(self.webview)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.preview_fram = QtWidgets.QFrame(self.frame)
        self.preview_fram.setMinimumSize(QtCore.QSize(150, 100))
        self.preview_fram.setMaximumSize(QtCore.QSize(125, 16777215))
        self.preview_fram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview_fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preview_fram.setObjectName("preview_fram")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.preview_fram)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.print_tbtn = QtWidgets.QToolButton(self.preview_fram)
        self.print_tbtn.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.print_tbtn.setFont(font)
        self.print_tbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/src/main/resources/base/img/icons8_print_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_tbtn.setIcon(icon)
        self.print_tbtn.setIconSize(QtCore.QSize(32, 32))
        self.print_tbtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.print_tbtn.setAutoRaise(False)
        self.print_tbtn.setObjectName("print_tbtn")
        self.verticalLayout_3.addWidget(self.print_tbtn)
        self.preview = QtWidgets.QToolButton(self.preview_fram)
        self.preview.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.preview.setFont(font)
        self.preview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/src/main/resources/base/img/icons8_file_preview_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preview.setIcon(icon1)
        self.preview.setIconSize(QtCore.QSize(32, 32))
        self.preview.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.preview.setAutoRaise(False)
        self.preview.setObjectName("preview")
        self.verticalLayout_3.addWidget(self.preview)
        self.toolButton = QtWidgets.QToolButton(self.preview_fram)
        self.toolButton.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolButton.setFont(font)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/src/main/resources/base/img/icons8_close_window_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_3.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.preview_fram)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Preview)
        self.toolButton.clicked.connect(Preview.close)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        _translate = QtCore.QCoreApplication.translate
        Preview.setWindowTitle(_translate("Preview", "Panorama optic - Preview"))
        self.print_tbtn.setText(_translate("Preview", "Imprimer"))
        self.preview.setText(_translate("Preview", "Aperçu"))
        self.toolButton.setText(_translate("Preview", "Annuler"))
from PyQt5 import QtWebEngineWidgets
import img_rc
