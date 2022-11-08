from PyQt5.QtCore import QObject, pyqtSlot, QEventLoop, QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QDialog


class PrintHandler(QObject):
    def __init__(self, parent=None):
        super(PrintHandler, self).__init__(parent)
        self.m_page = None
        self.m_inPrintPreview = False

    @property
    def page(self):
        return self.m_page

    @page.setter
    def page(self, page):
        if isinstance(page, QWebEnginePage):
            self.m_page = page
            # self.page.printRequested.connect(self.printPreview)
        else:
            raise TypeError("page must be a QWebEnginePage")

    @pyqtSlot()
    def print(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPaperSize(QPrinter.A6)
        # printer.setOrientation(QPrinter.Landscape)
        dialog = QPrintDialog(printer, self.page.view())
        if dialog.exec_() != QDialog.Accepted:
            return
        self.printDocument(printer)

    @pyqtSlot()
    def printPreview(self):
        if self.page is None:
            return
        if self.m_inPrintPreview:
            return
        self.m_inPrintPreview = True
        printer = QPrinter()
        printer.setPaperSize(QPrinter.A6)
        printer.setOrientation(QPrinter.Landscape)
        preview = QPrintPreviewDialog(printer, self.page.view())
        preview.paintRequested.connect(self.printDocument)
        preview.exec_()
        self.m_inPrintPreview = False

    @pyqtSlot(QPrinter)
    def printDocument(self, printer):
        result = False
        loop = QEventLoop()

        def printPreview(sucess):
            nonlocal result
            result = sucess
            loop.quit()

        self.page.print(printer, printPreview)
        loop.exec_()
        if not result:
            painter = QPainter()
            if painter.begin(printer):
                font = painter.font()
                font.setPixelSize(20)
                painter.setFont(font)
                painter.drawText(
                    QPointF(10, 25), "Could not generate print preview.")
                painter.end()
