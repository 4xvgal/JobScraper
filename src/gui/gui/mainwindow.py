# This Python file uses the following encoding: utf-8
import sys
import csv
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractTableModel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
filePath = "src/csv/forTestFiles/cleaned.csv"

# CSV 데이터 저장형식 클래스
class CSVTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data_list = data

    def rowCount(self, parent):
        return len(self.data_list)

    def columnCount(self, parent):
        return len(self.data_list[0]) if self.data_list else 0

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data_list[row][col])
        return None

# 주 윈도우 클래스
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 검색버튼을 클릭할때 함수 실행
        self.ui.search_button.clicked.connect(self.initSearch)
    # 검색버튼 눌러질때 실행되는 함수
    def initSearch(self):
        global filePath

        
        # Read CSV file and retrieve the data
        data = []
        with open(filePath, 'r', encoding='cp949') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)

        # Create a model and set it to the table view
        model = CSVTableModel(data)
        self.ui.ShowingCSV.setModel(model)

# 실행부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
