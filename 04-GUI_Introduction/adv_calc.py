from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    opr = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 681, 101))
        self.lineEdit.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"text-align: right;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 101, 91))
        self.pushButton.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 101, 91))
        self.pushButton_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 180, 101, 91))
        self.pushButton_3.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 300, 101, 91))
        self.pushButton_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 300, 101, 91))
        self.pushButton_5.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 420, 101, 91))
        self.pushButton_6.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 420, 101, 91))
        self.pushButton_7.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 300, 101, 91))
        self.pushButton_8.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 420, 101, 91))
        self.pushButton_9.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 540, 101, 91))
        self.pushButton_10.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(380, 540, 101, 91))
        self.pushButton_11.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 540, 101, 91))
        self.pushButton_12.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(550, 180, 101, 91))
        self.pushButton_13.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(550, 300, 101, 91))
        self.pushButton_14.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(550, 420, 101, 91))
        self.pushButton_15.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(550, 540, 101, 91))
        self.pushButton_16.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(700, 540, 151, 91))
        self.pushButton_17.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(700, 180, 151, 91))
        self.pushButton_18.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(700, 300, 151, 91))
        self.pushButton_19.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(700, 420, 151, 91))
        self.pushButton_20.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255,255);")
        self.pushButton_20.setObjectName("pushButton_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 31))
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
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "2"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "exp"))
        self.pushButton_12.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "-"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_16.setText(_translate("MainWindow", "*"))
        self.pushButton_17.setText(_translate("MainWindow", "="))
        self.pushButton_18.setText(_translate("MainWindow", "C"))
        self.pushButton_19.setText(_translate("MainWindow", "x"))
        self.pushButton_20.setText(_translate("MainWindow", "pow"))

        self.lineEdit.setReadOnly(True)

        btns = [self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,
                self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
                self.pushButton_9, self.pushButton_10]

        for i in range(len(btns)):
            btns[i].clicked.connect(self.appendValues)

        operators = [self.pushButton_13,self.pushButton_14,self.pushButton_15,self.pushButton_16]
        for i in range(len(operators)):
            operators[i].clicked.connect(self.appendOperators)

        self.pushButton_17.clicked.connect(self.calc)

    def appendValues(self):
        btn = self.sender()
        text = btn.text()
        self.opr += text
        # print(self.opr)
        self.lineEdit.setText(self.opr)

    def appendOperators(self):
        btn = self.sender()
        text = btn.text()
        self.opr += text
        # print(self.opr)
        self.lineEdit.setText(self.opr)

    def calc(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
