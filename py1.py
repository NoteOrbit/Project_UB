import mysql.connector
import sys
from sources import img_rc,resources
from main import *
from PyQt5.QtWidgets import QDialog, QApplication 
from PyQt5.uic import loadUi


mydb = mysql.connector.connect(option_files='sources/my.conf')


class my(QDialog):
    def __init__(self):
        self.user = ''
        super(my,self).__init__()
        loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.show2)


    def openwindows(self):


        mycursor = mydb.cursor()
        sql1 = """select user_infomations.name_eng,user_infomations.age,user_infomations.email 
        from user_login join user_infomations on user_infomations.id = user_login.id where user_login.id = '%s' """%(self.user)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        mycursor.execute(sql1)
        valuse = mycursor.fetchone()
        valuse = list(valuse)
        self.ui.setupUi(self.window)
        self.ui.setuser(valuse,self.user)
        self.show()
        self.window.show()


    def show2(self):
        self.logs()


    def logs(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM user_login WHERE BINARY id = '%s' AND BINARY password = '%s'" %(self.lineEdit.text(),self.lineEdit_2.text())
        mycursor.execute(sql)
        if mycursor.fetchone():
            self.user = self.lineEdit.text()
            self.openwindows()
            mainwindow.hide()

app = QtWidgets.QApplication(sys.argv)
mainwindow = my()
mainwindow.show()
sys.exit(app.exec_())
