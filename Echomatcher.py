# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Echomatcher.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        self.joinButton.setGeometry(QtCore.QRect(260, 430, 251, 91))
        self.joinButton.setObjectName("joinButton")
        self.fetchButton = QtWidgets.QPushButton(self.centralwidget)
        self.fetchButton.setGeometry(QtCore.QRect(530, 310, 111, 41))
        self.fetchButton.setObjectName("fetchButton")
        self.matchEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.matchEntry.setGeometry(QtCore.QRect(220, 310, 311, 41))
        self.matchEntry.setObjectName("matchEntry")
        self.browseEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.browseEntry.setGeometry(QtCore.QRect(220, 200, 311, 41))
        self.browseEntry.setObjectName("browseEntry")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 170, 111, 16))
        self.label.setObjectName("label")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(530, 200, 111, 41))
        self.browseButton.setObjectName("browseButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 290, 55, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fetchButton.clicked.connect(self.fetchid)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.joinButton.setText(_translate("MainWindow", "Join Match"))
        self.fetchButton.setText(_translate("MainWindow", "Get Match ID"))
        self.label.setText(_translate("MainWindow", "EchoVR Location"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Match ID"))

    def fetchid(self):
        game_state = echovr_api.fetch_state()
        matchEntry.setText(game_state.sessionid)
        return

if __name__ == "__main__":
    import sys
    import echovr_api
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
