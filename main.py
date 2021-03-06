from mysql.connector.fabric import connect
import imgall_rc
import sys
import mysql.connector
import requests
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap, QImage
import json
r = requests.get('http://newsapi.org/v2/top-headlines?country=th&apiKey=dd41f87ceaa54798a19a277b9d318610')
json.loads(r.content)
data = json.loads(r.content)
mydb = mysql.connector.connect(option_files='sources/my.conf')

class cal:
    def __init__(self,g):
        self.g = g
        self.total = 0
        self.default = 3
        self.count = 0
    def calculate(self):
        self.valuse = self.g[-1]
        self.g.pop()
        dict ={
            'A' : 4.0,
            'B+': 3.5,
            'B': 3.0,
            'C+': 2.5,
            'C': 2.0,
            'D+': 1.5,
            'D': 1.0,
            'F': 0
            }
        
        for val  in self.g:
          self.total += dict[val]*self.default
          self.count += self.default
        self.g.append(self.valuse)

        return self.total / self.count   
class setSTR:
    def __init__(self,datanews):
        self.data = datanews
        self.valuse = ''
        self.key1 = []
    def setstring(self):
        for i in range(10):
                for key,valuse in self.data['articles'][i].items():
                        if key == 'content':
                                break
                        v = []
                        self.key1.append(key)
                        v.append(valuse)
                        self.key1.extend(v)
                self.key1.extend('\n')
        for  item in self.key1:
                self.valuse += str(item)
                self.valuse += '\n'
        return self.valuse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 740))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons_18x18/gif/green/normal/004_12.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_bar.setObjectName("Top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Bnt_toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bnt_toggle.sizePolicy().hasHeightForWidth())
        self.Bnt_toggle.setSizePolicy(sizePolicy)
        self.Bnt_toggle.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px solid;\n"
"    image: url(:/newPrefix/cropped-UBU-Logo-Square-transparent.png);\n"
"}\n"
"\n"
"")
        self.Bnt_toggle.setText("")
        self.Bnt_toggle.setObjectName("Bnt_toggle")
        self.horizontalLayout_3.addWidget(self.Bnt_toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_bar)
        self.Content_bar = QtWidgets.QFrame(self.centralwidget)
        self.Content_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content_bar.setObjectName("Content_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content_bar)
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_left_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_top_menu = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menu.setObjectName("frame_top_menu")
        self.Bnt_menu_1 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Bnt_menu_1.setGeometry(QtCore.QRect(0, 0, 70, 70))
        self.Bnt_menu_1.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    \n"
"    image: url(:/newPrefix/icons_18x18/gif/green/normal/004_08.gif);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        self.Bnt_menu_1.setText("")
        self.Bnt_menu_1.setObjectName("Bnt_menu_1")
        self.Bnt_menu_2 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Bnt_menu_2.setGeometry(QtCore.QRect(0, 70, 70, 71))
        self.Bnt_menu_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    image: url(:/newPrefix/icons_18x18/gif/green/normal/004_18.gif);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        self.Bnt_menu_2.setText("")
        self.Bnt_menu_2.setObjectName("Bnt_menu_2")
        self.Bnt_menu_3 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Bnt_menu_3.setGeometry(QtCore.QRect(0, 140, 70, 70))
        self.Bnt_menu_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    image: url(:/newPrefix/icons_18x18/gif/green/normal/004_47.gif);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        self.Bnt_menu_3.setText("")
        self.Bnt_menu_3.setObjectName("Bnt_menu_3")
        self.Bnt_menu_4 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Bnt_menu_4.setGeometry(QtCore.QRect(0, 210, 70, 70))
        self.Bnt_menu_4.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    \n"
"    \n"
"    image: url(:/newPrefix/icons_18x18/gif/green/normal/004_13.gif);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        self.Bnt_menu_4.setText("")
        self.Bnt_menu_4.setObjectName("Bnt_menu_4")
        self.Bnt_menu_5 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Bnt_menu_5.setGeometry(QtCore.QRect(0, 280, 70, 70))
        self.Bnt_menu_5.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    \n"
"    image: url(:/newPrefix/icons_18x18/gif/green/normal/004_37.gif);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        self.Bnt_menu_5.setText("")
        self.Bnt_menu_5.setObjectName("Bnt_menu_5")
        self.horizontalLayout_4.addWidget(self.frame_top_menu)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_page = QtWidgets.QFrame(self.Content_bar)
        self.frame_page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_page.setObjectName("frame_page")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_page)
        self.stackedWidget.setGeometry(QtCore.QRect(9, -1, 1191, 681))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.groupBox = QtWidgets.QGroupBox(self.page_1)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.groupBox.setStyleSheet('color :rgb(255,255,255);')
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1171, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 977, 567))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color: rgb(255,255,255);")
        self.label.setStyleSheet("font: 20pt \"Ekkamai New\";")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("font: 20pt \"Ekkamai New\";")
        self.page_2.setObjectName("page_2")
        self.sh = QtWidgets.QLabel(self.page_2)
        self.sh.setGeometry(QtCore.QRect(0, 0, 1191, 681))
        self.sh.setAlignment(QtCore.Qt.AlignCenter)
        self.sh.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.sh.setObjectName("sh")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("font: 20pt \"Ekkamai New\";")
        self.page_3.setObjectName("page_3")
        self.socia = QtWidgets.QLabel(self.page_3)
        self.socia.setGeometry(QtCore.QRect(360, 480, 571, 41))
        self.socia.setStyleSheet("font: 20pt \"Ekkamai New\";")
        self.socia.setStyleSheet("color: rgb(255, 255, 255);")
        self.socia.setObjectName("socia")
        self.com = QtWidgets.QLabel(self.page_3)
        self.com.setGeometry(QtCore.QRect(360, 420, 571, 41))
        self.com.setStyleSheet("color: rgb(255, 255, 255);")
        self.com.setObjectName("com")
        self.math = QtWidgets.QLabel(self.page_3)
        self.math.setGeometry(QtCore.QRect(360, 360, 571, 41))
        self.math.setStyleSheet("color: rgb(255, 255, 255);")
        self.math.setObjectName("math")
        self.img = QtWidgets.QLabel(self.page_3)
        self.img.setGeometry(QtCore.QRect(10, 20, 321, 651))
        self.img.setStyleSheet("color: rgb(255, 255, 255);")
        self.img.setObjectName("img")
        self.thai = QtWidgets.QLabel(self.page_3)
        self.thai.setGeometry(QtCore.QRect(360, 240, 571, 41))
        self.thai.setStyleSheet("color: rgb(255, 255, 255);")
        self.thai.setObjectName("thai")
        self.Name = QtWidgets.QLabel(self.page_3)
        self.Name.setGeometry(QtCore.QRect(360, 180, 571, 41))
        self.Name.setStyleSheet("color: rgb(255, 255, 255);")
        self.Name.setObjectName("Name")
        self.eng = QtWidgets.QLabel(self.page_3)
        self.eng.setGeometry(QtCore.QRect(360, 300, 571, 41))
        self.eng.setStyleSheet("color: rgb(255, 255, 255);")
        self.eng.setObjectName("eng")
        self.Gpa = QtWidgets.QLabel(self.page_3)
        self.Gpa.setGeometry(QtCore.QRect(360, 540, 571, 41))
        self.Gpa.setStyleSheet("color: rgb(255, 255, 255);")
        self.Gpa.setObjectName("Gpa")
        self.id = QtWidgets.QLabel(self.page_3)
        self.id.setGeometry(QtCore.QRect(360, 120, 571, 41))
        self.id.setStyleSheet("color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("font: 20pt \"Ekkamai New\";")
        self.page_4.setObjectName("page_4")
        self.id_ = QtWidgets.QLabel(self.page_4)
        self.id_.setGeometry(QtCore.QRect(360, 180, 571, 41))
        self.id_.setStyleSheet("color: rgb(255, 255, 255);")
        self.id_.setObjectName("id_")
        self.name_eng = QtWidgets.QLabel(self.page_4)
        self.name_eng.setGeometry(QtCore.QRect(360, 240, 571, 41))
        self.name_eng.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_eng.setObjectName("name_eng")
        self.name_thai = QtWidgets.QLabel(self.page_4)
        self.name_thai.setGeometry(QtCore.QRect(360, 300, 571, 41))
        self.name_thai.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_thai.setObjectName("name_thai")
        self.Faculty = QtWidgets.QLabel(self.page_4)
        self.Faculty.setGeometry(QtCore.QRect(360, 360, 571, 41))
        self.Faculty.setStyleSheet("color: rgb(255, 255, 255);")
        self.Faculty.setObjectName("Faculty")
        self.BD = QtWidgets.QLabel(self.page_4)
        self.BD.setGeometry(QtCore.QRect(360, 420, 571, 41))
        self.BD.setStyleSheet("color: rgb(255, 255, 255);")
        self.BD.setObjectName("BD")
        self.AGE = QtWidgets.QLabel(self.page_4)
        self.AGE.setGeometry(QtCore.QRect(360, 480, 571, 41))
        self.AGE.setStyleSheet("color: rgb(255, 255, 255);")
        self.AGE.setObjectName("AGE")
        self.picc = QtWidgets.QLabel(self.page_4)
        self.picc.setGeometry(QtCore.QRect(10, 20, 321, 651))
        self.picc.setStyleSheet("color: rgb(255, 255, 255);")
        self.picc.setObjectName("picc")
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_2.addWidget(self.frame_page)
        self.verticalLayout.addWidget(self.Content_bar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ## bot
        self.Bnt_menu_1.clicked.connect(self.hello1)
        self.Bnt_menu_2.clicked.connect(self.hello2)
        self.Bnt_menu_3.clicked.connect(self.hello3)
        self.Bnt_menu_4.clicked.connect(self.hello4)
        self.Bnt_menu_5.clicked.connect(self.hello5)
        
        
        ## dict to string

        self.label.setText(setSTR(data).setstring())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REGUBU"))
        self.groupBox.setTitle(_translate("MainWindow", "News"))
        self.label.setText(_translate("MainWindow", "news"))
        self.sh.setText(_translate("MainWindow", "SCHEDULE"))
        self.socia.setText(_translate("MainWindow", "socia"))
        self.com.setText(_translate("MainWindow", "com"))
        self.math.setText(_translate("MainWindow", "math"))
        self.img.setText(_translate("MainWindow", "--------------------------------Img profile----------------------------------"))
        self.thai.setText(_translate("MainWindow", "thai "))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.eng.setText(_translate("MainWindow", "eng "))
        self.Gpa.setText(_translate("MainWindow", "gpax"))
        self.id.setText(_translate("MainWindow", "id"))
        self.id_.setText(_translate("MainWindow", "id"))
        self.name_eng.setText(_translate("MainWindow", "name eng"))
        self.name_thai.setText(_translate("MainWindow", "name thai"))
        self.Faculty.setText(_translate("MainWindow", "faculty"))
        self.BD.setText(_translate("MainWindow", "birthday"))
        self.AGE.setText(_translate("MainWindow", "age"))
        self.picc.setText(_translate("MainWindow", "--------------------------------Img profile----------------------------------"))


        ## functions make to switch screen
    def hello1(self):
        self.stackedWidget.setCurrentIndex(0)
    def hello2(self):
        self.stackedWidget.setCurrentIndex(1)
    def hello3(self):
        self.stackedWidget.setCurrentIndex(2)
    def hello4(self):
        self.stackedWidget.setCurrentIndex(3)
    def hello5(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are You sure!")
        msgBox.setWindowTitle("Exit")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            sys.exit()
        else :
            pass

    def setuser(self,valuse1,userid):
        import os
        mycursor = mydb.cursor(buffered=True)
        sql = 'select * from user_infomations where user_infomations.ID = (%s)'%(userid)
        mycursor.execute(sql)
        a = mycursor.fetchone()
        a = list(a)

        if a[7] == None :
                picture = 'https://storage.googleapis.com/picture-data/imgde.jpg'
        else:
                picture ='https://storage.googleapis.com/picture-data/img{:s}.jpg'.format(a[7])

        image = QImage()
        image.loadFromData(requests.get(picture).content)
        #pixmap = QPixmap('https://console.cloud.google.com/storage/browser/picture-data/img{:s}.jpg'.format(a[7]))
        pixmap = QPixmap(image)
        smaller = pixmap.scaled(400,250, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.picc.setPixmap(smaller)
        self.id_.setText('ID {:}'.format(a[0]))
        self.name_eng.setText('Name {:}'.format(valuse1[0]))
        self.AGE.setText('Age {:}'.format(valuse1[1]))
        self.name_thai.setText('Email {:}'.format(valuse1[2]))
        self.BD.setText('BD {:}'.format(a[-1]))


        mycursor2 = mydb.cursor(buffered=True)
        sqlfa = """SELECT describe1 FROM user_faculty 
                join user_infomations 
                on user_faculty.faculty = user_infomations.faculty 
                where user_infomations.faculty = (%s)"""%(a[6])
        mycursor2.execute(sqlfa)
        fa = mycursor2.fetchone()
        fa = list(fa)
        self.Faculty.setText(fa[0])

        mycursor4 = mydb.cursor(buffered=True)
        sqlbrach_ = """SELECT info_barch FROM user_faculty 
                join user_infomations 
                on user_faculty.barch = user_infomations.beach_id
                where user_infomations.beach_id = (%s)"""%(a[8])
        mycursor4.execute(sqlbrach_)
        ba = mycursor4.fetchone()
        ba = list(ba)
        self.BD.setText(ba[0])
        

        mycursor3 = mydb.cursor(buffered=True)
        sqlgr = """SELECT eng,math,com,thai,socia,sc FROM test.user_gr 
                join test.user_infomations 
                on user_infomations.ID = user_gr.ID 
                where test.user_gr.ID = (%s)"""%(a[0])
        mycursor3.execute(sqlgr)
        gr = mycursor3.fetchone()
        gr = list(gr)
        self.img.setPixmap(smaller)
        self.id.setText(str(a[0]))
        self.Name.setText('name {:}'.format(valuse1[0]))
        self.socia.setText('Man and Society --> {:}'.format(gr[4]))
        self.thai.setText('Thai language for communication --> {:}'.format(gr[3]))
        self.math.setText('Numerical method --> {:}'.format(gr[1]))
        self.eng.setText('Foundation English II --> {:}'.format(gr[0]))
        self.com.setText('Data structures and algorithms --> {:}'.format(gr[2]))
        self.Gpa.setText('GPA {:2f}'.format(cal(gr).calculate()))
        if gr[5] == None :
                picture = 'https://storage.googleapis.com/img_gr/imgde.jpg'
        else:
                picture ='https://storage.googleapis.com/img_gr/img{:s}.jpg'.format(gr[5])
        
        image = QImage()
        image.loadFromData(requests.get(picture).content)
        pixmap = QPixmap(image)
        smaller2 = pixmap.scaled(1191,681, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.sh.setPixmap(smaller2)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
