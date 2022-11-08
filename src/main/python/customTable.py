from PyQt5.QtCore import QAbstractTableModel, Qt


class MyTableModel(QAbstractTableModel):

    def __init__(self, data, header):
        QAbstractTableModel.__init__(self, parent=None)
        self.data_rows = data or []
        self.header = header

    def rowCount(self, parent):
        if self.data_rows:
            return len(self.data_rows)
        else:
            return 0

    def columnCount(self, parent):
        if self.data_rows:
            return len(self.data_rows[0])
        else:
            return 0

    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        if not index.isValid():
            return None
        if (index.column() == 0):
            value = self.data_rows[index.row()][index.column()]
        else:
            value = self.data_rows[index.row()][index.column()]
        if role == Qt.EditRole:
            return value
        elif role == Qt.DisplayRole:
            value = self.data_rows[index.row()][index.column()]
            return value

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
