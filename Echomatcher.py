# -*- coding: utf-8 -*-

# Author: David Dowie
# Gui purpose to be able to join matches without the need to wait for invite from party members
# and to be able to fetch a session id to send to other players to join the match

from PyQt5 import QtCore, QtGui, QtWidgets

#initialise gui and initial funtion calls for button presses
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(800,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 170, 140, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 290, 140, 16))
        self.label_2.setObjectName("label_2")
        self.copied = QtWidgets.QLabel(self.centralwidget)
        self.copied.setGeometry(QtCore.QRect(650, 310, 111, 41))
        self.copied.setObjectName("copied")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #set font
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(60)

        #set label font
        self.label.setFont(font)
        self.label_2.setFont(font)

        #spectate radio button
        self.spectateRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.spectateRadio.setGeometry(QtCore.QRect(220, 100, 120, 20))
        self.spectateRadio.setObjectName("spectateRadio")
        self.spectateRadio.setFont(font)

        #player radio button
        self.playerRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.playerRadio.setGeometry(QtCore.QRect(550, 100, 120, 20))
        self.playerRadio.setObjectName("playerRadio")
        self.playerRadio.setFont(font)
        self.userType = "P" #monitor if user wants to be a spectator or a player


        #join button
        joinFont = QtGui.QFont()
        joinFont.setFamily("Helvetica")
        joinFont.setPointSize(20)
        joinFont.setBold(True)
        joinFont.setWeight(80)
        self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        self.joinButton.setGeometry(QtCore.QRect(260, 430, 251, 91))
        self.joinButton.setObjectName("joinButton")
        self.joinButton.setFont(joinFont)

        #fetch button
        self.fetchButton = QtWidgets.QPushButton(self.centralwidget)
        self.fetchButton.setGeometry(QtCore.QRect(530, 310, 111, 41))
        self.fetchButton.setObjectName("fetchButton")
        self.fetchButton.setFont(font)

        #entry for match id
        self.matchEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.matchEntry.setGeometry(QtCore.QRect(220, 310, 311, 41))
        self.matchEntry.setObjectName("matchEntry")


        #entry box for the path for the executable
        self.browseEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.browseEntry.setGeometry(QtCore.QRect(220, 200, 311, 41))
        self.browseEntry.setObjectName("browseEntry")

        #button to browse for path
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(530, 200, 111, 41))
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setFont(font)

        #method calls
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fetchButton.clicked.connect(self.fetch_id)
        self.browseButton.clicked.connect(self.set_path)
        self.joinButton.clicked.connect(self.join_match)
        self.spectateRadio.toggled.connect(self.to_spec)
        self.playerRadio.toggled.connect(self.to_play)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.joinButton.setText(_translate("MainWindow", "LAUNCH"))
        self.fetchButton.setText(_translate("MainWindow", "Get Match ID"))
        self.label.setText(_translate("MainWindow", "EchoVR Location"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Match ID"))
        self.copied.setText(_translate("MainWindow", "Copied to clipboard"))
        self.copied.hide()
        self.spectateRadio.setText(_translate("MainWindow", "Spectator"))
        self.playerRadio.setText(_translate("MainWindow", "Player"))
        self.playerRadio.toggle()

        #will initialise the default path if one does not exist
        try:
            file = open("pathFile.txt","r")
            self.path = file.read()
            if(self.path==""):
                self.path = "C:\\Program Files\\Oculus\\Software\\Software\\ready-at-dawn-echo-arena\\bin\\win7\\echovr.exe"
        except:
            self.path = "C:\\Program Files\\Oculus\\Software\\Software\\ready-at-dawn-echo-arena\\bin\\win7\\echovr.exe"
        self.browseEntry.setText(_translate("MainWindow",self.path))

    #change userType to spectator
    def to_spec(self):
        self.userType = "S"

    #change userType to Spectator
    def to_play(self):
        self.userType = "P"
    def set_clipboard(self, data):
        p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        p.stdin.write(data)
        p.stdin.close()
        retcode = p.wait()

    #changes the matchid entry box to hold the sessionid of the current match
    def fetch_id(self):
        try:
            self.copied.show()
            pyperclip.copy(self.matchEntry.text())

            game_state = echovr_api.fetch_state()
        except:
            return
        print(game_state.sessionid)
        time.sleep(0.3)
        self.copied.hide()
        self.matchEntry.setText(game_state.sessionid)

    #sets the path of the executable
    def set_path(self):
        fileName, _= QtWidgets.QFileDialog.getOpenFileName(None, "Select Match ID file","", "exe Files (*.exe)")
        if fileName:
            self.browseEntry.setText(fileName)
            pathFile = open("pathFile.txt", "w")
            pathFile.write(fileName)
            pathFile.close()

    #gets command based off state of app
    def get_command(self):
        if self.userType == "P":
            if self.matchEntry.text() == "":
                command = "\"" + self.path + "\"" + " -http"
            else:
                command = "\"" + self.path + "\""  + " -http -lobbyid " + self.matchEntry.text()
                print(self.matchEntry)
        else:
            if self.matchEntry.text() == "":
                command = "\"" + self.path + "\"" + "-spectatorstream -http"
            else:
                command = "\"" + self.path + "\""  + " -spectatorstream -http -lobbyid " + self.matchEntry.text()
        return command
    #joins match from a passed sessionid
    def join_match(self):
        self.path = self.browseEntry.text()
        if not self.path:
            self.set_path()

        if "echovr.exe" in self.path:
            command = self.get_command()
            try:
                subprocess.call('taskkill /IM echovr.exe')
                subprocess.Popen(command)

            except SystemError as e:
                print("unable to run exe")
        else:
            raise Exception('This exe is not EchoVR!')



if __name__ == "__main__":
    import sys
    import subprocess
    import pyperclip
    import time
    import echovr_api
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
