from printer import PrintHandler
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from PyQt5.QtWidgets import QWidget
from jinja2 import Template
from ui import Ui_Preview


class GenerateTemplate(QWidget, Ui_Preview):
    def __init__(self, path):
        super(GenerateTemplate, self).__init__()
        self.setupUi(self)
        self.path = path
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        handler = PrintHandler(self)
        handler.page = self.webview.page()
        self.print_tbtn.clicked.connect(handler.print)
        self.preview.clicked.connect(handler.printPreview)

    @pyqtSlot()
    def receipt(self, data):

        with open(self.path + '/fr/reciept_template.html', 'r', encoding='utf-8') as template:
            coupon = template.read()

        html = Template(str(coupon)).render(
            data=data
        )
        with open(self.path + '/fr/reciept_final.html', 'w', encoding='utf-8') as f:
            f.write(html)

        self.webview.load(
            QUrl('file:///' + self.path + '/fr/reciept_final.html'))
