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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 16))
        font = QFont()
        font.setFamilies([u"Nanum Gothic"])
        self.label.setFont(font)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 80, 731, 441))
        self.ListViewer = QWidget()
        self.ListViewer.setObjectName(u"ListViewer")
        self.ShowingCSV = QTableView(self.ListViewer)
        self.ShowingCSV.setObjectName(u"ShowingCSV")
        self.ShowingCSV.setGeometry(QRect(10, 0, 711, 391))
        self.tabWidget.addTab(self.ListViewer, "")
        self.Statics = QWidget()
        self.Statics.setObjectName(u"Statics")
        self.tabWidget.addTab(self.Statics, "")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(150, 0, 271, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.search_button = QPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(190, 1, 61, 41))
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 40, 111, 31))
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 10, 104, 21))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 71, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 50, 91, 16))
        self.label_3.setFont(font)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(430, 0, 271, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 0, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JobScraperGUI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uc778\uad6c\uc9c1 \uc815\ubcf4 \ud1b5\ud569 \uac80\uc0c9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ListViewer), QCoreApplication.translate("MainWindow", u"ListViewer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Statics), QCoreApplication.translate("MainWindow", u"\ud1b5\uacc4\uce58\ubcf4\uae30", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"8 (\uae30\ubcf8\uac12)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4 \uc785\ub825", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uba40\ud2f0\ud504\ub85c\uc138\uc11c \uc218", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uacb0\uacfc \ucd08\uae30\ud654", None))
    # retranslateUi

