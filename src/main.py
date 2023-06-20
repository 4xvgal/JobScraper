from gui.mainwindow import *
from multiprocessing import freeze_support
import sys, os
import csv
import time
from multiprocessing import Process
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractTableModel,QTimer


#다른 코드들 import

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from scrap.scrap_init import run_crawling


if __name__ == '__main__':
    freeze_support()
    #GUI 실행
    initGUI()

    