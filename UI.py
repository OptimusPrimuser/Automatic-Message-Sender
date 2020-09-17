

from PySide2.QtCore import QCoreApplication
#from PySide2.QtWidgets import *

from PySide2.QtWidgets import QLabel, QPushButton, QStatusBar, QTextBrowser, QWidget
from PySide2.QtCore import QCoreApplication, QMetaObject, QRect
from SendMessage import SendMessage 
class Ui_MainWindow(object):

    def delivery(self):
        nos=self.textBrowser.toPlainText()
        nos=[i for i in nos.split("\n") if i.isdigit() and len(i)==12] 
        message=self.textBrowser_2.toPlainText()
        k=SendMessage(nos,message)
        del k

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(316, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 60, 256, 192))
        self.textBrowser.setReadOnly(False)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 320, 256, 192))
        self.textBrowser_2.setReadOnly(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 30, 121, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 290, 121, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 530, 93, 28))
        self.pushButton.clicked.connect(self.delivery)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Phone Numbers", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

