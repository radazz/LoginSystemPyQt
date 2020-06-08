import subprocess
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

class Login(object):
    def GetHWID(self):
        return str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip())

    def GetSerialNumber(self):
        return str(subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip())

    def GetDatabaseInformation(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'users'
        }

        self.getattributes = (
            "SELECT `username`, `password`, `HWID` FROM `users`"
        )

        self.database_info = mysql.connector.connect(**self.config)

        self.db = self.database_info.cursor()
        self.db.execute(self.getattributes)

    def Window_LoginSuccess(self):
        self.window = QtWidgets.QMessageBox()
        self.window.setWindowTitle("[Result] Login")
        self.window.setIcon(QtWidgets.QMessageBox.Information)
        self.window.setStandardButtons(QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Ignore)
        self.window.setDefaultButton(QtWidgets.QMessageBox.Close)
        self.window.setText("Bun venit")
        self.window.exec_()
