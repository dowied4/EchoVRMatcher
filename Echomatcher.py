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
        self.label.setGeometry(QtCore.QRect(160, 170, 140, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 280, 140, 16))
        self.label_2.setObjectName("label_2")
        self.joinLabel = QtWidgets.QLabel(self.centralwidget)
        self.joinLabel.setGeometry(QtCore.QRect(515,280,100,20))
        self.joinLabel.setObjectName("joinLabel")
        self.matchIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.matchIDLabel.setGeometry(QtCore.QRect(100,100,180,50))
        self.matchIDLabel.setObjectName("matchIDLabel")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(280,100,500,50))
        self.IDLabel.setObjectName("IDLabel")
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
        self.IDLabel.setFont(font)

        #Adjust weight for header
        font.setWeight(80)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.joinLabel.setFont(font)    
        self.matchIDLabel.setFont(font)

        #spectate radio button
        # self.spectateRadio = QtWidgets.QRadioButton(self.centralwidget)
        # self.spectateRadio.setGeometry(QtCore.QRect(500, 320, 120, 20))
        # self.spectateRadio.setObjectName("spectateRadio")
        # self.spectateRadio.setFont(font)

        # player radio button
        # self.playerRadio = QtWidgets.QRadioButton(self.centralwidget)
        # self.playerRadio.setGeometry(QtCore.QRect(650, 320, 120, 20))
        # self.playerRadio.setObjectName("playerRadio")
        # self.playerRadio.setFont(font)
        # self.userType = "P" #monitor if user wants to be a spectator or a player


        #join button
        joinFont = QtGui.QFont()
        joinFont.setFamily("Helvetica")
        joinFont.setPointSize(20)
        joinFont.setBold(True)
        joinFont.setWeight(80)
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setGeometry(QtCore.QRect(260, 430, 251, 91))
        self.launchButton.setObjectName("launchButton")
        self.launchButton.setFont(joinFont)
        self.launchButton.setToolTip('Launches game')
        joinFont.setPointSize(10)

        #fetch button
        # self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        # self.joinButton.setGeometry(QtCore.QRect(360, 310, 111, 41))
        # self.joinButton.setObjectName("joinButton")
        # self.joinButton.setFont(font)
        # self.joinButton.setToolTip('Joins match from id')
        # self.joinButton.setFont(joinFont)

        # Blue team
        self.joinBlue = QtWidgets.QPushButton(self.centralwidget)
        self.joinBlue.setGeometry(QtCore.QRect(375,310,85,41))
        self.joinBlue.setObjectName("joinBlue")
        self.joinBlue.setFont(font)
        self.joinBlue.setToolTip("Joins Blue Team from id")
        self.joinBlue.setFont(joinFont)

        # Orange team
        self.joinOrange = QtWidgets.QPushButton(self.centralwidget)
        self.joinOrange.setGeometry(QtCore.QRect(615,310,85,41))
        self.joinOrange.setObjectName("joinOrange")
        self.joinOrange.setFont(font)
        self.joinOrange.setToolTip("Joins Orange Team from id")
        self.joinOrange.setFont(joinFont)

        # Spectator
        self.joinSpec = QtWidgets.QPushButton(self.centralwidget)
        self.joinSpec.setGeometry(QtCore.QRect(475,310,125,41))
        self.joinSpec.setObjectName("joinSpec")
        self.joinSpec.setFont(font)
        self.joinSpec.setToolTip("Joins Spectator from id")
        self.joinSpec.setFont(joinFont)

        #clipboard button
        self.clipButton = QtWidgets.QPushButton(self.centralwidget)
        self.clipButton.setGeometry(QtCore.QRect(50, 110, 30, 30))
        self.clipButton.setObjectName("clipButton")
        self.clipButton.setIcon(QtGui.QIcon('copy.png'))
        self.clipButton.setIconSize(QtCore.QSize(24,24))
        self.clipButton.setToolTip('Copy to Clipboard')
        

        #entry for match id
        self.matchEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.matchEntry.setGeometry(QtCore.QRect(50, 310, 300, 41))
        self.matchEntry.setObjectName("matchEntry")


        #entry box for the path for the executable
        self.browseEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.browseEntry.setGeometry(QtCore.QRect(50, 200, 300, 41))
        self.browseEntry.setObjectName("browseEntry")

        #button to browse for path
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(360, 200, 111, 41))
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setFont(joinFont)
        self.browseButton.setToolTip("Select the EchoVR.exe")

        #method calls
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.joinButton.clicked.connect(self.join_match)
        self.browseButton.clicked.connect(self.set_path)
        self.launchButton.clicked.connect(self.launch_game)
        # self.spectateRadio.toggled.connect(self.to_spec)
        # self.playerRadio.toggled.connect(self.to_play)
        self.joinBlue.clicked.connect(self.join_blue)
        self.joinOrange.clicked.connect(self.join_orange)
        self.joinSpec.clicked.connect(self.join_spectator)
        self.clipButton.clicked.connect(self.fetch_id)
        self.emsg = QtWidgets.QErrorMessage()
        self.emsg.setWindowModality(QtCore.Qt.WindowModal)
        self.emsg.setWindowTitle("EchoVR.exe not Found!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EchoVR Matcher"))
        self.launchButton.setText(_translate("MainWindow", "LAUNCH GAME"))
        # self.joinButton.setText(_translate("MainWindow", "Join Match"))
        self.joinBlue.setText(_translate("MainWindow", "Blue"))
        self.joinOrange.setText(_translate("MainWindow","Orange"))
        self.joinSpec.setText(_translate("MainWindow", "Spectator"))
        self.label.setText(_translate("MainWindow", "EchoVR Location"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Target Match ID"))
        self.joinLabel.setText(_translate("MainWindow", "Join As:"))
        self.matchIDLabel.setText(_translate("MainWindow", "Current Match ID: "))
        self.IDLabel.setText(_translate("MainWindow", "ID Unavailable(please launch through EchoVR Matcher)"))
        # self.spectateRadio.setText(_translate("MainWindow", "Spectator"))
        # self.playerRadio.setText(_translate("MainWindow", "Player"))
        # self.playerRadio.toggle()

        #will initialise the default path if one does not exist
        try:
            file = open("pathFile.txt","r")
            self.path = file.read()
            if(self.path==""):
                self.path = "C:\\Program Files\\Oculus\\Software\\Software\\ready-at-dawn-echo-arena\\bin\\win7\\echovr.exe"
        except:
            self.path = "C:\\Program Files\\Oculus\\Software\\Software\\ready-at-dawn-echo-arena\\bin\\win7\\echovr.exe"
        self.browseEntry.setText(_translate("MainWindow",self.path))

    def showError(self):
       self.emsg.showMessage("EchoVR.exe could not be found. Please enter a valid path!")
        
    #change userType to spectator
    # def to_spec(self):
    #     self.userType = "S"

    #change userType to Spectator
    # def to_play(self):
    #     self.userType = "P"

    def poll_id(self):
        try:
            game_state = echovr_api.fetch_state()
            self.IDLabel.setText(game_state.sessionid)
        except:
            self.IDLabel.setText("ID Unavailable(please launch through EchoVR Matcher)")
    
        
    #changes the matchid entry box to hold the sessionid of the current match
    def fetch_id(self):
        if len(self.IDLabel.text()) == 36:
            pyperclip.copy(self.IDLabel.text())


    #sets the path of the executable
    def set_path(self):
        fileName, _= QtWidgets.QFileDialog.getOpenFileName(None, "Select Match ID file","", "exe Files (*.exe)")
        try:  
             file = open("pathFile.txt","r")
             if file.read() == fileName:
                 return
        except:
            pass
        if fileName:
            pathFile = open("pathFile.txt", "w")
            pathFile.write(fileName)
            pathFile.close()
            self.path = fileName
            self.browseEntry.setText(fileName)
        print(self.path)

    #gets command based off state of app
    def get_command(self,team):
        if self.matchEntry.text() != "":
            if team == "b":
                return "\"" + self.path + "\"" + " -lobbyid " + self.matchEntry.text() + "-lobbyteam " + "0"

            if team == "o":
                return "\"" + self.path + "\"" + " -lobbyid " + self.matchEntry.text() + "-lobbyteam " + "1"
            if team =="s":
                return "\"" + self.path + "\"" + " -lobbyid " + self.matchEntry.text() + "-lobbyteam " + "2"
        else:
            self.showError()

    def launch_game(self):
        self.path = self.browseEntry.text()
        command = "\"" + self.path + "\""
        if "echovr.exe" in self.path:
            try:
                subprocess.call('taskkill /IM echovr.exe')
                subprocess.Popen(command)
            except:
                self.showError()
        else:
            self.showError()

    #joins match from a passed sessionid
    def join_match(self, com):
        self.path = self.browseEntry.text()
        if "echovr.exe" in self.path:
            try:
                subprocess.call('taskkill /IM echovr.exe')
                subprocess.Popen(com)
            except:
                self.showError()
        else:
            self.showError()

    def join_blue(self):
        self.path = self.browseEntry.text()
        command = self.get_command("b")
        self.join_match(command)

    def join_orange(self):
        self.path = self.browseEntry.text()
        command = self.get_command("o")
        self.join_match(command)

    def join_spectator(self):
        self.path = self.browseEntry.text()
        command = self.get_command("s")
        self.join_match(command)


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
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.poll_id)
    timer.start(5000)
    MainWindow.show()
    sys.exit(app.exec_())
