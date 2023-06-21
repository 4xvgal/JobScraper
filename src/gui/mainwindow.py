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
import pandas as pd
#다른 코드들 import

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from scrap.scrap_init import run_crawling
from csvEdit.csvFunc import csvEdit
from scrap.clear_csv import Initialization

from . import circle_graph as c
from . import bar_graph as b


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

keyword = str(None)
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
        #상태 표시 라벨 텍스트 설정
        #self.ui.StatusView.setText("Stanby")
        setStatusText(self,"Stanby")
        # 검색버튼을 클릭할때 함수 실행
        self.ui.search_button.clicked.connect(self.initSearch)

        # 검색결과 초기화 버튼 누를 때 함수 실행
        self.ui.reset_button.clicked.connect(self.resetResult)
        #그래프 함수 호출
        self.initUI() 

    # 검색버튼 눌러질때 실행되는 함수
    def initSearch(self):
        global keyword
        #키워드 전달하기
        processCount = int(self.ui.multiProcess.currentText()) #multiProcess 콤보박스 오브젝트에서 값 가져오기
        keyword = self.ui.search_keyword_lineEdit.text() # search_keyword_lineedit 오브젝트에서 값 가져오기
        
        # 키워드 잘 가져오는지 디버깅용 출력
        print(keyword, processCount)

        #사전 파일 초기화
        init_files()

        #크롤러 실행
        self.ui.crawler_process = run_crawler_in_separate_process(keyword, processCount)
        setStatusText(self, "Crawlling Started")
        # 크롤러가 끝나면?
        self.ui.timer = QTimer() #<== QTimer 클래스의 객체 self.ui.timer
        self.ui.timer.timeout.connect(self.check_crawler_process) # <== timer 의 설정된 시간 (1000밀리초) 마다 timeout 되어 self.check_crawler_process 객체를 실행  
        self.ui.timer.start(1000)  # 타임아웃 간격 설정

    #rst button clicked func (reset result)
    def resetResult(self):
        setStatusText(self,"Reset")
        self.ui.ShowingCSV.setModel(None)
        
    def check_crawler_process(self):
        # is_alive() 는 mutliprocess.process 클래스의 메서드입니다.

        if not self.ui.crawler_process.is_alive(): #<== self.ui.crawler_process 프로세스가 실행 중이 아닐 때
            # 프로세스 끝나면 타이머 종료
            self.ui.timer.stop()
            setStatusText(self, "Crawlling Done")
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
            setStatusText(self, "Table Generating started")
            model = CSVTableModel(data)
            self.ui.ShowingCSV.setModel(model)
            setStatusText(self, "Table Generating done")
            #그래프 함수 호출
            self.initUI() 

    def initUI(self): #그래프 그리기
        #레이아웃 초기화
        clearlayout(self.ui.graph_vertical)
        clearlayout(self.ui.graph_vertical_tap2)
        clearlayout(self.ui.graph_vertical_tap3)
       # 그래프 1
        if plt.get_fignums():  # 활성화된 figure가 있으면
            plt.figure().clear()  # 이전에 그려진 그래프를 지움
        fig1, ax1 = plt.subplots() 
        canvas1 = FigureCanvas(fig1)
        self.ui.graph_vertical.addWidget(canvas1)
        his.draw_graph(ax1, canvas1, cleand)

        # 그래프 2
        fig2, ax2 = plt.subplots()
        canvas2 = FigureCanvas(fig2)
        self.ui.graph_vertical_tap2.addWidget(canvas2)
        c.draw_graph(ax2, canvas2, cleand,keyword)

       
        # 그래프 3
        fig3, ax3 = plt.subplots()
        canvas3 = FigureCanvas(fig3)
        self.ui.graph_vertical_tap3.addWidget(canvas3)
        b.draw_graph(ax3, canvas3, cleand,keyword)

#레이아웃 초기화
def clearlayout(layout):
    for i in reversed(range(layout.count())):
        print(layout.itemAt(i))
        layout.removeItem(layout.itemAt(i))
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
#csv 파일들 병합
def mergeCsvs(route, merged):
    saramin = route[0]
    worknet = route[1]
    

    df1 = pd.read_csv(worknet, encoding='CP949')
    df2 = pd.read_csv(saramin, encoding='CP949')

    merged_df = pd.concat([df1, df2])
    merged_df.to_csv(merged, index=False, encoding='CP949')
    return int(0)

#set text
def setStatusText(self, text):
    self.ui.StatusView.setText(text) 

