# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1680, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 80, 1251, 591))
        self.ListViewer = QWidget()
        self.ListViewer.setObjectName(u"ListViewer")
        self.ShowingCSV = QTableView(self.ListViewer)
        self.ShowingCSV.setObjectName(u"ShowingCSV")
        self.ShowingCSV.setGeometry(QRect(0, 0, 1241, 551))
        self.tabWidget.addTab(self.ListViewer, "")
        self.Statics = QWidget()
        self.Statics.setObjectName(u"Statics")
        self.verticalLayoutWidget = QWidget(self.Statics)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 19, 1221, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Tab4 = QTabWidget(self.verticalLayoutWidget)
        self.Tab4.setObjectName(u"Tab4")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayoutWidget_2 = QWidget(self.tab_1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 1211, 501))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graph_vertical = QVBoxLayout()
        self.graph_vertical.setObjectName(u"graph_vertical")

        self.verticalLayout_2.addLayout(self.graph_vertical)

        self.tab1_label1 = QLabel(self.verticalLayoutWidget_2)
        self.tab1_label1.setObjectName(u"tab1_label1")

        self.verticalLayout_2.addWidget(self.tab1_label1)

        self.Tab4.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_4 = QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(9, 9, 1191, 481))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graph_vertical_tap2 = QVBoxLayout()
        self.graph_vertical_tap2.setObjectName(u"graph_vertical_tap2")

        self.verticalLayout_8.addLayout(self.graph_vertical_tap2)

        self.tab2_label1 = QLabel(self.verticalLayoutWidget_4)
        self.tab2_label1.setObjectName(u"tab2_label1")
        self.tab2_label1.setMinimumSize(QSize(1185, 0))

        self.verticalLayout_8.addWidget(self.tab2_label1)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.Tab4.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_5 = QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 1181, 471))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.graph_vertical_tap3 = QVBoxLayout()
        self.graph_vertical_tap3.setObjectName(u"graph_vertical_tap3")

        self.verticalLayout_5.addLayout(self.graph_vertical_tap3)

        self.tab3_label1 = QLabel(self.verticalLayoutWidget_5)
        self.tab3_label1.setObjectName(u"tab3_label1")

        self.verticalLayout_5.addWidget(self.tab3_label1)

        self.Tab4.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.Tab4)

        self.tabWidget.addTab(self.Statics, "")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 0, 781, 83))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Nanum Gothic"])
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.search_keyword_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.search_keyword_lineEdit.setObjectName(u"search_keyword_lineEdit")

        self.horizontalLayout.addWidget(self.search_keyword_lineEdit)

        self.search_button = QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout.addWidget(self.search_button)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.multiProcess = QComboBox(self.horizontalLayoutWidget)
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.addItem("")
        self.multiProcess.setObjectName(u"multiProcess")

        self.horizontalLayout.addWidget(self.multiProcess)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(810, 0, 160, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TimerView = QLabel(self.verticalLayoutWidget_3)
        self.TimerView.setObjectName(u"TimerView")
        self.TimerView.setFont(font)

        self.verticalLayout_3.addWidget(self.TimerView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.Tab4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JobScraperGUI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ListViewer), QCoreApplication.translate("MainWindow", u"ListViewer", None))
        self.tab1_label1.setText("")
        self.Tab4.setTabText(self.Tab4.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tab2_label1.setText("")
        self.Tab4.setTabText(self.Tab4.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tab3_label1.setText("")
        self.Tab4.setTabText(self.Tab4.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Statics), QCoreApplication.translate("MainWindow", u"\ud1b5\uacc4\uce58\ubcf4\uae30", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uc778\uad6c\uc9c1 \uc815\ubcf4 \ud1b5\ud569 \uac80\uc0c9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4 \uc785\ub825", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uacb0\uacfc \ucd08\uae30\ud654", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uba40\ud2f0\ud504\ub85c\uc138\uc11c \uc218", None))
        self.multiProcess.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.multiProcess.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.multiProcess.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.multiProcess.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.multiProcess.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.multiProcess.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.multiProcess.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.multiProcess.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))

        self.TimerView.setText("")
    # retranslateUi

