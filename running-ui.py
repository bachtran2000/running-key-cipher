
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEncryp = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.encode())
        self.btnEncryp.setGeometry(QtCore.QRect(150, 290, 141, 51))
        self.btnEncryp.setObjectName("btnEncryp")
        self.btnDecryp = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.decode())
        self.btnDecryp.setGeometry(QtCore.QRect(440, 290, 141, 51))
        self.btnDecryp.setObjectName("btnDecryp")
        self.lbOUT = QtWidgets.QLabel(self.centralwidget)
        self.lbOUT.setGeometry(QtCore.QRect(10, 200, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbOUT.setFont(font)
        self.lbOUT.setObjectName("lbOUT")
        self.lbKey = QtWidgets.QLabel(self.centralwidget)
        self.lbKey.setGeometry(QtCore.QRect(40, 130, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbKey.setFont(font)
        self.lbKey.setObjectName("lbKey")
        self.lbIn = QtWidgets.QLabel(self.centralwidget)
        self.lbIn.setGeometry(QtCore.QRect(30, 60, 53, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lbIn.setFont(font)
        self.lbIn.setObjectName("lbIn")
        self.txtInput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInput.setGeometry(QtCore.QRect(120, 50, 561, 51))
        self.txtInput.setObjectName("txtInput")
        self.txtKey = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(120, 120, 561, 51))
        self.txtKey.setObjectName("txtKey")
        self.lbOut = QtWidgets.QLabel(self.centralwidget)
        self.lbOut.setGeometry(QtCore.QRect(120, 190, 561, 41))
        self.lbOut.setText("")
        self.lbOut.setObjectName("lbOut")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def encode(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        plaintext = self.txtInput.text()
        key = self.txtKey.text()
        ciphertxt = ''
        # Xử lý chuỗi ban đầu
        key = key.replace(" ","").lower().strip(" ")
        plaintext = plaintext.replace(" ","").lower().strip(" ")
        
        # Xét trường hợp cho phép nếu chiều dài chuỗi lớn hơn hoặc bằng chiều dài key
        if len(plaintext)>=len(key):
            # Tạo ra khoá hoàn chỉnh
            for i in plaintext:
                if len(key) < len(plaintext):
                    key = key + i
            for i in range(0,len(plaintext)):
                # lấy vị trí của phần tử thứ i
                pos = (alphabet.find(plaintext[i])+alphabet.find(key[i]))%26
                # mã hoá ký tự vị trí thứ i
                ciphertxt = ciphertxt+alphabet[pos]
            self.lbIn.setText('Plaint text: ')
            self.lbOUT.setText('Encrypht: ')
            self.lbOut.setText(ciphertxt)
        else:
            self.lbOut.setText('Plain text must shorter than key!')

    def decode(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        plaintext=''
        cipher = self.txtInput.text()
        key = self.txtKey.text()

        cipher = cipher.replace(" ","").lower().strip(" ")
        key = key.replace(" ","").lower().strip(" ")
        flag=0
        # trường hợp mã hoá bằng với key
        if len(cipher) == len(key):
            # Việc giải mã đơn giản, không cần phải chèn plain text đã giải được vào key
            for i in range(0,len(key)):
                pos = (alphabet.find(cipher[i])-alphabet.find(key[i])%26)
                plaintext = plaintext+alphabet[abs(pos)]
        elif len(key)<len(cipher):
            # vì chiều dài plain text bằng với chiều dài cipher,
            # nên nếu chiều dài bằng nhau là lúc giải mã xong
            while len(plaintext) < len(cipher):
                # biến flag giúp cho việc sau mỗi vòng lặp, 
                # phần tử thứ i sẽ quay về đúng vị trí của nó
                for i in range(flag,len(cipher)):
                    # lấy vị trí của phần tử thứ i
                    pos = (alphabet.find(cipher[i])-alphabet.find(key[i]))%26
                    # chèn phần tử thứ i vào chuỗi
                    plaintext = plaintext + alphabet[abs(pos)]
                    # chèn phần tử thứ i sau khi giải mã xong vào key
                    key = key + plaintext[i]
                    flag = flag+1
            self.lbOut.setText(plaintext)
            self.lbIn.setText('Cipher text: ')
            self.lbOUT.setText('Decrypht: ')
        else:
            self.lbOut.setText('Cipher text must shorter than key!')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnEncryp.setText(_translate("MainWindow", "Encrypht"))
        self.btnDecryp.setText(_translate("MainWindow", "Decrypht"))
        self.lbOUT.setText(_translate("MainWindow", "Output:"))
        self.lbKey.setText(_translate("MainWindow", "Key:"))
        self.lbIn.setText(_translate("MainWindow", "Input:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
