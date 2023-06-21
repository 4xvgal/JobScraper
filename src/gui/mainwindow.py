# This Python file uses the following encoding: utf-8
import sys, os
import csv
from multiprocessing import Process
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtCore import QTimer

#matplotlib 위한 import
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from . import hisFunc as his
from . import circle_graph as c
from . import bar_graph as b
import pandas as pd
#다른 코드들 import

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from scrap.scrap_init import run_crawling
from csvEdit.csvFunc import csvEdit
from scrap.clear_csv import Initialization

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_MainWindow
filePath = r"C:\CSV\merged.csv"
export_path = r"C:\CSV\merged.cleaned.csv"
route = ["C:\CSV\saramin_final.csv", "C:\CSV\worknet_final.csv"]
cleand = r"C:\CSV\merged.cleaned.csv"
def run_crawler_in_separate_process(keyword, processCount):
    crawler_process = Process(target=run_crawling, args=(keyword, processCount))
    crawler_process.start()
    return crawler_process

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

        #그래프 함수 호출
        self.initUI() 

    # 검색버튼 눌러질때 실행되는 함수
    def initSearch(self):
        #키워드 전달하기
        processCount = int(self.ui.multiProcess.currentText()) #multiProcess 콤보박스 오브젝트에서 값 가져오기
        keyword = self.ui.search_keyword_lineEdit.text() # search_keyword_lineedit 오브젝트에서 값 가져오기
        
        # 키워드 잘 가져오는지 디버깅용 출력
        print(keyword, processCount)

        #사전 파일 초기화
        init_files()

        #크롤러 실행
        self.ui.crawler_process = run_crawler_in_separate_process(keyword, processCount)

        # 크롤러가 끝나면?
        self.ui.timer = QTimer() #<== QTimer 클래스의 객체 self.ui.timer
        self.ui.timer.timeout.connect(self.check_crawler_process) # <== timer 의 설정된 시간 (1000밀리초) 마다 timeout 되어 self.check_crawler_process 객체를 실행  
        self.ui.timer.start(1000)  # 타임아웃 간격 설정

    def check_crawler_process(self):
        
        # is_alive() 는 mutliprocess.process 클래스의 메서드입니다.

        if not self.ui.crawler_process.is_alive(): #<== self.ui.crawler_process 프로세스가 실행 중이 아닐 때
            # 프로세스 끝나면 타이머 종료
            self.ui.timer.stop()
            #csv 병합
            print("merging started")
            mergeCsvs(route,filePath)
            #CSV 재가공 코드
            csvEdit(filePath, export_path,'cp949')
            data = []
            with open(filePath, 'r', encoding='cp949') as file:
                csv_reader = csv.reader(file)

                for row in csv_reader:
                    data.append(row)

            model = CSVTableModel(data)
            self.ui.ShowingCSV.setModel(model)

    def initUI(self): #그래프 그리기
       # 그래프 1
        fig1, ax1 = plt.subplots()
        canvas1 = FigureCanvas(fig1)
        self.ui.graph_vertical.addWidget(canvas1)
        his.draw_graph(ax1, canvas1, cleand)

        # 그래프 2
        fig2, ax2 = plt.subplots()
        canvas2 = FigureCanvas(fig2)
        self.ui.graph_vertical_tap2.addWidget(canvas2)
        c.draw_graph(ax2, canvas2, cleand)

        # 그래프 3
        fig3, ax3 = plt.subplots()
        canvas3 = FigureCanvas(fig3)
        self.ui.graph_vertical_tap3.addWidget(canvas3)
        b.draw_graph(ax3, canvas3, cleand) 

#함수화
def initGUI():
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = MainWindow()
        widget.show()
        sys.exit(app.exec())
    else:
        app = QApplication(sys.argv)
        widget = MainWindow()
        widget.show()
        sys.exit(app.exec())
#사전 파일 초기화 함수
def init_files():
    if os.path.exists(filePath): # 크롤링 실행 전에 파일 존재 유무를 검사해서 중복된 파일을 제거한다.
        print("merge.csv found.")
        os.remove(filePath)
    elif (not os.path.exists(filePath)):
        print("merge.csv not found")
    touch_merge()
# 머지 생성
def touch_merge():
    with open(filePath, 'w') as file:
        print("merge.csv created")
        pass

def mergeCsvs(route, merged):
    saramin = route[0]
    worknet = route[1]
    

    df1 = pd.read_csv(worknet, encoding='CP949')
    df2 = pd.read_csv(saramin, encoding='CP949')

    merged_df = pd.concat([df1, df2])
    merged_df.to_csv(merged, index=False, encoding='CP949')
    return int(0)