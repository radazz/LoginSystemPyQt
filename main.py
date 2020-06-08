from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Login

class Ui_InternalCheat(Login, object):
    def Setup(self, InternalCheat):
        InternalCheat.setObjectName("InternalCheat")
        InternalCheat.setWindowModality(QtCore.Qt.NonModal)
        InternalCheat.setEnabled(True)
        InternalCheat.resize(150, 150)
        InternalCheat.setMinimumSize(QtCore.QSize(150, 150))
        InternalCheat.setMaximumSize(QtCore.QSize(150, 150))
        InternalCheat.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\Desktop\\main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InternalCheat.setWindowIcon(icon)
        InternalCheat.setAutoFillBackground(False)
        InternalCheat.setStyleSheet("")

        self.username_placeholder = QtWidgets.QLineEdit(InternalCheat)
        self.username_placeholder.setGeometry(QtCore.QRect(20, 20, 113, 20))
        self.username_placeholder.setObjectName("username_placeholder")

        self.password_placeholder = QtWidgets.QLineEdit(InternalCheat)
        self.password_placeholder.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.password_placeholder.setObjectName("password_placeholder")

        self.login_btn = QtWidgets.QPushButton(InternalCheat)
        self.login_btn.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.login_btn.setObjectName("login_btn")

        self.login_btn.clicked.connect(self.TryCredentials)

        self.TranslateUI(InternalCheat)
        QtCore.QMetaObject.connectSlotsByName(InternalCheat)

    def TryCredentials(self):
        self.username = self.username_placeholder.text()
        self.password = self.password_placeholder.text()

        if (self.username == "" or self.username == "Username" and self.password == "" or self.password == "Password"):
            print("wrong credentials")
            pass

        self.GetDatabaseInformation()

        for (user, passw, hwid) in self.db:
            print("username <{}>, password <{}>, hwid <{}>".format(user, passw, hwid))


    def TranslateUI(self, InternalCheat):
        _translate = QtCore.QCoreApplication.translate

        InternalCheat.setWindowTitle(_translate("InternalCheat", "InternalCheat"))
        self.username_placeholder.setText(_translate("InternalCheat", "Username"))
        self.password_placeholder.setText(_translate("InternalCheat", "Password"))
        self.login_btn.setText(_translate("InternalCheat", "Login"))

if __name__ == "__main__":
    import sys
    GUI = QtWidgets.QApplication(sys.argv)
    InternalCheat = QtWidgets.QWidget()
    UI = Ui_InternalCheat()
    UI.Setup(InternalCheat)
    InternalCheat.show()
    sys.exit(GUI.exec_())
