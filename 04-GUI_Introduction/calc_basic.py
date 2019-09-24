from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 381, 61))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 85, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 361, 61))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 401, 61))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 110, 431, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 220, 431, 71))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 350, 401, 61))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 350, 431, 71))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 480, 101, 81))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 480, 101, 81))
        self.pushButton_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 480, 101, 81))
        self.pushButton_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 480, 101, 81))
        self.pushButton_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(850, 480, 151, 81))
        self.pushButton_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 31))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBasic_Calc = QtWidgets.QAction(MainWindow)
        self.actionBasic_Calc.setObjectName("actionBasic_Calc")
        self.actionAdvance_Calc = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Calc.setObjectName("actionAdvance_Calc")
        self.actionScientific_Calc = QtWidgets.QAction(MainWindow)
        self.actionScientific_Calc.setObjectName("actionScientific_Calc")
        self.menuOptions.addAction(self.actionBasic_Calc)
        self.menuOptions.addAction(self.actionAdvance_Calc)
        self.menuOptions.addAction(self.actionScientific_Calc)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Basic Calculator"))
        self.label_2.setText(_translate("MainWindow", "Enter first number"))
        self.label_3.setText(_translate("MainWindow", "Enter second number"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionBasic_Calc.setText(_translate("MainWindow", "Basic Calc"))
        self.actionAdvance_Calc.setText(_translate("MainWindow", "Advance Calc"))
        self.actionScientific_Calc.setText(_translate("MainWindow", "Scientific Calc"))

        self.lineEdit_3.setReadOnly(True)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.sub)
        self.pushButton_3.clicked.connect(self.div)
        self.pushButton_4.clicked.connect(self.mul)
        self.pushButton_5.clicked.connect(self.clear)

    def add(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())

        result = f_num + s_num
        self.lineEdit_3.setText(str(result))

    def sub(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())

        result = f_num - s_num
        self.lineEdit_3.setText(str(result))

    def div(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())

        result = f_num / s_num
        self.lineEdit_3.setText(str(result))

    def mul(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())

        result = f_num * s_num
        self.lineEdit_3.setText(str(result))

    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
