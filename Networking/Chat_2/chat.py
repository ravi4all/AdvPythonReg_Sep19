from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading, json

class Ui_MainWindow(QtWidgets.QMainWindow):

    chatData = {
            "Ram" : [{'msg':'hello','rply':'hey'},
                     {'msg':'hi'},
                     {'msg':'what is python', 'rply':'programming'},
                     {'msg':'nice','rply':'yup'},
                     {'rply':'where are you ?'},
                     {'rply':'take care'},
                     {'msg':'delhi'}
                     ],
            "Shyam" : [
                {'msg': 'hey', 'rply': 'hi'},
                {'msg': 'how are you ?','rply':'fine'},
                {'msg': 'where are you', 'rply': 'delhi'},
                {'msg': 'great', 'rply': 'yes'},
            ]
        }


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 401, 741))
        self.listWidget.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 10, 801, 521))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setObjectName("frame")

        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 5, 800, 520))
        self.listWidget_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget_2.setObjectName("listWidget_2")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 560, 801, 107))
        self.textEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 690, 351, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textEdit_2.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Send"))

        self.showUsers()

        # Calling server
        threading.Thread(target=self.server).start()

        self.listWidget.itemClicked.connect(self.changeUser)
        self.pushButton.clicked.connect(self.sendMessage)

    def showUsers(self):
        self.users = list(self.chatData.keys())
        for i in range(len(self.users)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(self.users[i])

    def changeUser(self,item):
        self.listWidget_2.clear()
        self.textEdit_2.setReadOnly(False)
        try:
            current_user = item.text()
            chat = self.chatData[current_user]
            for data in chat:
                for key in data:
                    item = QtWidgets.QListWidgetItem()
                    self.listWidget_2.addItem(item)
                    if key == 'msg':
                        item.setText(data[key])
                        item.setTextAlignment(QtCore.Qt.AlignLeft)
                    else:
                        item.setText(data[key])
                        item.setTextAlignment(QtCore.Qt.AlignRight)
        except BaseException as ex:
            print(ex)

    def sendMessage(self):
        msg = self.textEdit_2.toPlainText()
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item.setText(msg)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        self.textEdit_2.setText("")

    def recvMessage(self):
        pass

    def server(self):
        host = "localhost"
        port = 80

        mySocket = socket.socket()
        mySocket.bind((host, port))

        print("Server started on", port)
        print("Waiting for connections...")

        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print("Connection from: " + str(addr))
        i = 0
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            data = json.loads(data)
            # print(type(data))
            # print("=> ",data)
            username = data['name']
            if i == 0:
                print("Welcome",username)
                i += 1
            else:
                print("{} : {}".format(data['name'],data['message']))
            # data = str(data).upper()
            data = input("Enter message: ")
            print("Server: " + str(data))
            print()
            conn.send(data.encode())

        conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
