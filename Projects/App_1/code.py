from PyQt5 import QtCore, QtGui, QtWidgets

import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='new_test',autocommit=True)

cursor = connection.cursor()

class Ui_MainWindow(object):
    loggedInUser = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home_frame = QtWidgets.QFrame(self.centralwidget)
        self.home_frame.setGeometry(QtCore.QRect(0, 0, 1191, 701))
        self.home_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.label = QtWidgets.QLabel(self.home_frame)
        self.label.setGeometry(QtCore.QRect(190, 10, 871, 71))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.home_frame)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 431, 61))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.home_frame)
        self.comboBox.setGeometry(QtCore.QRect(420, 190, 351, 61))
        self.comboBox.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.home_frame)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 340, 351, 61))
        self.comboBox_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.home_frame)
        self.label_3.setGeometry(QtCore.QRect(60, 340, 291, 61))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.home_frame)
        self.pushButton.setGeometry(QtCore.QRect(830, 190, 271, 61))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.home_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 330, 271, 61))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.home_frame)
        self.label_4.setGeometry(QtCore.QRect(60, 450, 1021, 201))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.home_frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1191, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(440, 20, 261, 71))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 120, 371, 61))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(580, 120, 401, 61))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 211, 371, 61))
        self.label_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 211, 401, 61))
        self.lineEdit_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 310, 371, 61))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 310, 401, 61))
        self.lineEdit_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(80, 400, 371, 61))
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(80, 480, 371, 61))
        self.label_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(580, 400, 401, 51))
        self.comboBox_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(580, 490, 401, 51))
        self.comboBox_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 590, 361, 71))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1191, 691))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 299, 401, 61))
        self.lineEdit_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(480, 9, 261, 71))
        self.label_11.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 460, 361, 71))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 200, 401, 61))
        self.lineEdit_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(120, 299, 371, 61))
        self.label_12.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(120, 200, 371, 61))
        self.label_13.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1201, 681))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(410, 0, 391, 81))
        self.label_14.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(140, 160, 331, 71))
        self.label_15.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(530, 160, 331, 71))
        self.label_16.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(530, 260, 331, 71))
        self.label_17.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(140, 260, 331, 71))
        self.label_18.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 470, 431, 91))
        self.pushButton_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(450, 40, 281, 61))
        self.label_19.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(170, 240, 291, 61))
        self.label_20.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_5.setGeometry(QtCore.QRect(570, 240, 431, 61))
        self.comboBox_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 450, 341, 81))
        self.pushButton_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_6.setGeometry(QtCore.QRect(570, 260, 431, 61))
        self.comboBox_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(170, 260, 291, 61))
        self.label_21.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(450, 60, 281, 61))
        self.label_22.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 470, 341, 81))
        self.pushButton_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1191, 691))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setGeometry(QtCore.QRect(10, 20, 261, 51))
        self.label_23.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_23.setObjectName("label_23")
        self.textEdit = QtWidgets.QTextEdit(self.frame_6)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 1141, 131))
        self.textEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 260, 361, 71))
        self.lineEdit_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(30, 260, 181, 61))
        self.label_24.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(30, 350, 181, 61))
        self.label_25.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_25.setObjectName("label_25")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 350, 361, 71))
        self.lineEdit_7.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(30, 440, 181, 61))
        self.label_26.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_26.setObjectName("label_26")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 440, 361, 71))
        self.lineEdit_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(30, 530, 181, 61))
        self.label_27.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 530, 361, 71))
        self.lineEdit_9.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(780, 270, 261, 61))
        self.label_28.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_28.setObjectName("label_28")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_10.setGeometry(QtCore.QRect(670, 350, 461, 71))
        self.lineEdit_10.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 470, 171, 101))
        self.pushButton_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_9.setGeometry(QtCore.QRect(960, 470, 171, 101))
        self.pushButton_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(10, 20, 281, 51))
        self.label_29.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(220, 20, 301, 51))
        self.label_30.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_7)
        self.label_31.setGeometry(QtCore.QRect(10, 100, 1171, 131))
        self.label_31.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.radioButton = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton.setGeometry(QtCore.QRect(30, 270, 471, 51))
        self.radioButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 340, 471, 51))
        self.radioButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 410, 471, 51))
        self.radioButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 470, 471, 51))
        self.radioButton_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_10.setGeometry(QtCore.QRect(380, 560, 351, 81))
        self.pushButton_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_11.setGeometry(QtCore.QRect(790, 560, 351, 81))
        self.pushButton_11.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_32 = QtWidgets.QLabel(self.frame_8)
        self.label_32.setGeometry(QtCore.QRect(440, 50, 251, 71))
        self.label_32.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_8)
        self.label_33.setGeometry(QtCore.QRect(160, 260, 371, 61))
        self.label_33.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_8)
        self.label_34.setGeometry(QtCore.QRect(160, 170, 371, 61))
        self.label_34.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_8)
        self.label_35.setGeometry(QtCore.QRect(160, 350, 371, 61))
        self.label_35.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_8)
        self.label_36.setGeometry(QtCore.QRect(160, 440, 371, 61))
        self.label_36.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_8)
        self.label_37.setGeometry(QtCore.QRect(160, 530, 371, 61))
        self.label_37.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_37.setObjectName("label_37")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_11.setGeometry(QtCore.QRect(600, 170, 331, 61))
        self.lineEdit_11.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_12.setGeometry(QtCore.QRect(600, 260, 331, 61))
        self.lineEdit_12.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_13.setGeometry(QtCore.QRect(600, 350, 331, 61))
        self.lineEdit_13.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_14.setGeometry(QtCore.QRect(600, 440, 331, 61))
        self.lineEdit_14.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_15.setGeometry(QtCore.QRect(600, 530, 331, 61))
        self.lineEdit_15.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_19.raise_()
        self.label_20.raise_()
        self.comboBox_5.raise_()
        self.pushButton_6.raise_()
        self.label_22.raise_()
        self.frame_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 31))
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
        self.label.setText(_translate("MainWindow", "              Welcome to Test Engine"))
        self.label_2.setText(_translate("MainWindow", "Register As"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Student"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Teacher"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Student"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Teacher"))
        self.label_3.setText(_translate("MainWindow", "Login As"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Register Now"))
        self.label_6.setText(_translate("MainWindow", "Enter Name"))
        self.label_7.setText(_translate("MainWindow", "Enter ID"))
        self.label_8.setText(_translate("MainWindow", "Enter Password"))
        self.label_9.setText(_translate("MainWindow", "Choose Course"))
        self.label_10.setText(_translate("MainWindow", "Choose Semester"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Btech"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "BCA"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "MCA"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Mtech"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "Register Now"))
        self.label_11.setText(_translate("MainWindow", "Login Now"))
        self.pushButton_4.setText(_translate("MainWindow", "Login Now"))
        self.label_12.setText(_translate("MainWindow", "Enter Password"))
        self.label_13.setText(_translate("MainWindow", "Enter ID"))
        self.label_14.setText(_translate("MainWindow", "Student Dashboard"))
        self.label_15.setText(_translate("MainWindow", "Test Attempted"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Previous Scores"))
        self.pushButton_5.setText(_translate("MainWindow", "Start New Test"))
        self.label_19.setText(_translate("MainWindow", "Create Test"))
        self.label_20.setText(_translate("MainWindow", "Choose Subject"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Python"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "C"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "C++"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "JAVA"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", ".net"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "php"))
        self.pushButton_6.setText(_translate("MainWindow", "Create Test"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Python"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "C"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "C++"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "JAVA"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", ".net"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "php"))
        self.label_21.setText(_translate("MainWindow", "Choose Subject"))
        self.label_22.setText(_translate("MainWindow", "Give Test"))
        self.pushButton_7.setText(_translate("MainWindow", "Start Test"))
        self.label_23.setText(_translate("MainWindow", "Enter Question"))
        self.label_24.setText(_translate("MainWindow", "Option 1"))
        self.label_25.setText(_translate("MainWindow", "Option 2"))
        self.label_26.setText(_translate("MainWindow", "Option 3"))
        self.label_27.setText(_translate("MainWindow", "Option 4"))
        self.label_28.setText(_translate("MainWindow", "Enter Answer"))
        self.pushButton_8.setText(_translate("MainWindow", "Next"))
        self.pushButton_9.setText(_translate("MainWindow", "Done"))
        self.label_29.setText(_translate("MainWindow", "Time Left : "))
        self.label_30.setText(_translate("MainWindow", "00"))
        self.radioButton.setText(_translate("MainWindow", "Option_1"))
        self.radioButton_2.setText(_translate("MainWindow", "Option_2"))
        self.radioButton_3.setText(_translate("MainWindow", "Option_3"))
        self.radioButton_4.setText(_translate("MainWindow", "Option_4"))
        self.pushButton_10.setText(_translate("MainWindow", "Next Question"))
        self.pushButton_11.setText(_translate("MainWindow", "Submit Test"))
        self.label_32.setText(_translate("MainWindow", "Final Score"))
        self.label_33.setText(_translate("MainWindow", "Question Attempted"))
        self.label_34.setText(_translate("MainWindow", "Total Questions"))
        self.label_35.setText(_translate("MainWindow", "Correct Answers"))
        self.label_36.setText(_translate("MainWindow", "Wrong Answers"))
        self.label_37.setText(_translate("MainWindow", "Final Result"))

        self.frame.hide()

        self.pushButton.clicked.connect(self.registerFrame)
        self.pushButton_2.clicked.connect(self.loginFrame)

        self.pushButton_3.clicked.connect(self.register)

    def registerFrame(self):
        self.frame.show()
        self.frame_2.hide()

    def loginFrame(self):
        self.frame.show()
        self.frame_3.hide()

    def login(self):
        pass

    def register(self):
        name = self.lineEdit.text()
        id = self.lineEdit_2.text()
        pwd = self.lineEdit_3.text()
        course = self.comboBox_3.currentText()
        sem = self.comboBox_4.currentText()
        self.loggedInUser = self.comboBox.currentText()

        query = "insert into users values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,id,pwd,course,sem,self.loggedInUser))
        print("Data Inserted Successfully....")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
