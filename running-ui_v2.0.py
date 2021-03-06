
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import webbrowser

# pyinstaller -F <name>
# pyuic5 -x tool.ui -o running-ui_v2.0.py

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbTitle.setGeometry(QtCore.QRect(280, 10, 500, 51))
        self.lbTitle.setMaximumSize(QtCore.QSize(16777214, 16777214))
        # self.centralwidget.setStyleSheet('background-color: rgb(50,50,50)')
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lbTitle.setFont(font)
        self.lbTitle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbTitle.setTabletTracking(False)
        self.lbTitle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbTitle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lbTitle.setAcceptDrops(False)
        self.lbTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbTitle.setAutoFillBackground(False)
        self.lbTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbTitle.setLineWidth(3)
        self.lbTitle.setTextFormat(QtCore.Qt.RichText)
        self.lbTitle.setWordWrap(False)
        self.lbTitle.setObjectName("lbTitle")
        self.lbInput = QtWidgets.QLabel(self.centralwidget)
        self.lbInput.setGeometry(QtCore.QRect(60, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbInput.setFont(font)
        self.lbInput.setAcceptDrops(False)
        self.lbInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbInput.setLineWidth(1)
        self.lbInput.setObjectName("lbInput")
        self.lbKey = QtWidgets.QLabel(self.centralwidget)
        self.lbKey.setGeometry(QtCore.QRect(60, 220, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbKey.setFont(font)
        self.lbKey.setAcceptDrops(False)
        self.lbKey.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbKey.setLineWidth(1)
        self.lbKey.setObjectName("lbKey")
        self.lbOutput = QtWidgets.QLabel(self.centralwidget)
        self.lbOutput.setGeometry(QtCore.QRect(60, 350, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbOutput.setFont(font)
        self.lbOutput.setAcceptDrops(False)
        self.lbOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbOutput.setLineWidth(1)
        self.lbOutput.setObjectName("lbOutput")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 350, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAcceptDrops(False)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.btnDe = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.decode())
        self.btnDe.setGeometry(QtCore.QRect(610, 470, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnDe.setFont(font)
        self.btnDe.setObjectName("btnDe")
        self.btnEn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.encode())
        self.btnEn.setGeometry(QtCore.QRect(260, 470, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnEn.setFont(font)
        self.btnEn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEn.setAutoFillBackground(False)
        self.btnEn.setAutoExclusive(False)
        self.btnEn.setAutoDefault(False)
        self.btnEn.setDefault(False)
        self.btnEn.setFlat(False)
        self.btnEn.setObjectName("btnEn")
        self.txtInput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInput.setGeometry(QtCore.QRect(280, 100, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.txtInput.setFont(font)
        self.txtInput.setReadOnly(False)
        self.txtInput.setObjectName("txtInput")
        self.txtKey = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(280, 220, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.txtKey.setFont(font)
        self.txtKey.setReadOnly(False)
        self.txtKey.setObjectName("txtKey")
        self.txtOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(280, 350, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.txtOutput.setFont(font)
        self.txtOutput.setReadOnly(True)
        self.txtOutput.setObjectName("txtOutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 24))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuAbout.addAction(self.actionLicense)
        self.menuAbout.addSeparator()
        self.menubar.addAction(self.menuAbout.menuAction(), )
        self.actionLicense.triggered.connect(lambda:webbrowser.open_new_tab('https://facebook.com/trancaominhbach'))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def encode(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        plaintext = self.txtInput.text()
        key = self.txtKey.text()
        ciphertxt = ''
        # X??? l?? chu???i ban ?????u
        key = key.replace(" ","").lower().strip(" ")
        plaintext = plaintext.replace(" ","").lower().strip(" ")

        # Xet empty
        if not key  and not plaintext :
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Input and Key can't empty!")
        elif key == "" and plaintext != "":
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Key can't empty!")
        elif plaintext == "" and key!="":
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Input can't empty!")

        # X??t tr?????ng h???p cho ph??p n???u chi???u d??i chu???i l???n h??n ho???c b???ng chi???u d??i key
        elif len(plaintext)>=len(key):
            # T???o ra kho?? ho??n ch???nh
            for i in plaintext:
                if len(key) < len(plaintext):
                    key = key + i
            for i in range(0,len(plaintext)):
                # l???y v??? tr?? c???a ph???n t??? th??? i
                pos = (alphabet.find(plaintext[i])+alphabet.find(key[i]))%26
                # m?? ho?? k?? t??? v??? tr?? th??? i
                ciphertxt = ciphertxt+alphabet[pos]
            self.lbInput.setText('Plaint Text: ')
            self.lbOutput.setText('Cipher Text: ')
            self.txtOutput.setText(ciphertxt)
        else:
            self.txtOutput.setText('Plain text must shorter than key!')

    def decode(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        plaintext=''
        cipher = self.txtInput.text()
        key = self.txtKey.text()

        cipher = cipher.replace(" ","").lower().strip(" ")
        key = key.replace(" ","").lower().strip(" ")
        flag = 0

        if not key and not cipher :
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Input and Key can't empty!")
            
        elif key == "" and cipher != "":
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Key can't empty!")
            
        elif cipher == "" and key!="":
            self.lbInput.setText('Input: ')
            self.lbOutput.setText("Warning")
            self.txtOutput.setText("Input can't empty!")
            
        # tr?????ng h???p m?? ho?? b???ng v???i key
        elif len(cipher) == len(key):
            # Vi???c gi???i m?? ????n gi???n, kh??ng c???n ph???i ch??n plain text ???? gi???i ???????c v??o key
            for i in range(0,len(key)):
                pos = (alphabet.find(cipher[i])-alphabet.find(key[i])%26)
                plaintext = plaintext+alphabet[abs(pos)]
            self.txtOutput.setText(plaintext)
            self.lbInput.setText('Cipher Text: ')
            self.lbOutput.setText('Plain Text: ')
        elif len(key)<len(cipher):
            # v?? chi???u d??i plain text b???ng v???i chi???u d??i cipher,
            # n??n n???u chi???u d??i b???ng nhau l?? l??c gi???i m?? xong
            while len(plaintext) < len(cipher):
                # bi???n flag gi??p cho vi???c sau m???i v??ng l???p, 
                # ph???n t??? th??? i s??? quay v??? ????ng v??? tr?? c???a n??
                for i in range(flag,len(cipher)):
                    # l???y v??? tr?? c???a ph???n t??? th??? i
                    pos = (alphabet.find(cipher[i])-alphabet.find(key[i]))%26
                    # ch??n ph???n t??? th??? i v??o chu???i
                    plaintext = plaintext + alphabet[abs(pos)]
                    # ch??n ph???n t??? th??? i sau khi gi???i m?? xong v??o key
                    key = key + plaintext[i]
                    flag = flag+1
            self.txtOutput.setText(plaintext)
            self.lbInput.setText('Cipher Text: ')
            self.lbOutput.setText('Plain Text: ')
        else:
            self.txtOutput.setText('Cipher text must shorter than key!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Running Cipher Tool"))
        self.lbTitle.setText(_translate("MainWindow", "Running Cipher Tool - Nh??m 8"))
        self.lbInput.setText(_translate("MainWindow", "Input"))
        self.lbKey.setText(_translate("MainWindow", "Key"))
        self.lbOutput.setText(_translate("MainWindow", "Output"))
        self.btnDe.setText(_translate("MainWindow", "Decrypht"))
        self.btnEn.setText(_translate("MainWindow", "Encrypht"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLicense.setText(_translate("MainWindow", "License"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
