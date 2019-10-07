from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(QtWidgets.QMainWindow):
    positions_occupied = []
    values = [i for i in range(9)]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 80, 121, 111))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 80, 121, 111))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 200, 481, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(160, 340, 471, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 80, 121, 111))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 220, 121, 111))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 220, 121, 111))
        self.pushButton_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 220, 121, 111))
        self.pushButton_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 360, 121, 111))
        self.pushButton_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 360, 121, 111))
        self.pushButton_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 360, 121, 111))
        self.pushButton_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(300, 70, 21, 411))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(470, 70, 21, 411))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.btns = [self.pushButton,self.pushButton_2,self.pushButton_3,
                self.pushButton_5, self.pushButton_6, self.pushButton_4,
                self.pushButton_8, self.pushButton_9, self.pushButton_7]

        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.move)

    def move(self):
        try:
            current_btn = self.sender()
            current_index = self.btns.index(current_btn)
            if current_btn.text() == 'X' or current_btn.text() == '0':
                print("Already Occupied")
            else:
                current_btn.setText(self.ch)
                # self.positions_occupied.append(self.ch)
                self.values[current_index] = self.ch
                print(current_index)
                if self.checkConditions(self.ch):
                    print("You win...")
                else:
                    print("Calling CPU Turn")
                    self.cpu_turn()

        except BaseException as ex:
            print(ex)

    def cpu_turn(self):
        cpu_move = True
        print("CPU Turn")
        while cpu_move:
            btn = random.choice(self.btns)
            cpu_index = self.btns.index(btn)
            if btn.text() == 'X' or btn.text() == '0':
                print("Already Occupied")
            else:
                btn.setText(self.cpu_ch)
                print(cpu_index)
                self.values[cpu_index] = self.cpu_ch
                if self.checkConditions(self.cpu_ch):
                    print("CPU Win")
                cpu_move = False

    def choice(self):
        self.ch = input("Enter your choice : ")
        if self.ch == 'X':
            self.cpu_ch = '0'
        else:
            self.cpu_ch = 'X'

    def checkWinner(self,pos_1, pos_2, pos_3, player):
        print(self.values)
        if self.values[pos_1] == player and self.values[pos_2] == player and self.values[pos_3] == player:
            print(player,pos_1,pos_2,pos_3)
            return True

    def checkConditions(self,player):
        if self.checkWinner(0, 1, 2, player):
            return True
        elif self.checkWinner(0, 3, 6, player):
            return True
        elif self.checkWinner(0, 4, 8, player):
            return True
        elif self.checkWinner(1, 4, 7, player):
            return True
        elif self.checkWinner(2, 5, 8, player):
            return True
        elif self.checkWinner(3, 4, 5, player):
            return True
        elif self.checkWinner(6, 7, 8, player):
            return True
        elif self.checkWinner(2, 4, 6, player):
            return True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.choice()
    MainWindow.show()
    sys.exit(app.exec_())
