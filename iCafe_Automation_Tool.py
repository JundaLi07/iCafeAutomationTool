# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iCafe_Automation_Tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 568)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_Script_Display = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Script_Display.setGeometry(QtCore.QRect(20, 70, 651, 411))
        self.tableWidget_Script_Display.setObjectName("tableWidget_Script_Display")
        self.tableWidget_Script_Display.setColumnCount(4)
        self.tableWidget_Script_Display.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Script_Display.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Script_Display.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Script_Display.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Script_Display.setHorizontalHeaderItem(3, item)
        self.pushButton_Load_Script = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Load_Script.setGeometry(QtCore.QRect(1010, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Load_Script.setFont(font)
        self.pushButton_Load_Script.setObjectName("pushButton_Load_Script")
        self.pushButton_2_Save_Script = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_Save_Script.setGeometry(QtCore.QRect(940, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2_Save_Script.setFont(font)
        self.pushButton_2_Save_Script.setObjectName("pushButton_2_Save_Script")
        self.pushButton_3_Run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_Run.setGeometry(QtCore.QRect(980, 120, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3_Run.setFont(font)
        self.pushButton_3_Run.setObjectName("pushButton_3_Run")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 111, 16))
        self.label.setObjectName("label")
        self.comboBox_Game_Name = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Game_Name.setGeometry(QtCore.QRect(360, 30, 171, 31))
        self.comboBox_Game_Name.setObjectName("comboBox_Game_Name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 10, 111, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_2_Input_Mode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2_Input_Mode.setGeometry(QtCore.QRect(550, 30, 121, 31))
        self.comboBox_2_Input_Mode.setObjectName("comboBox_2_Input_Mode")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Script_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Script_Name.setGeometry(QtCore.QRect(20, 30, 321, 31))
        self.lineEdit_Script_Name.setObjectName("lineEdit_Script_Name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 230, 111, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_4_Add_Script = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4_Add_Script.setGeometry(QtCore.QRect(680, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_Add_Script.setFont(font)
        self.pushButton_4_Add_Script.setObjectName("pushButton_4_Add_Script")
        self.pushButton_5_Delete_Script = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5_Delete_Script.setGeometry(QtCore.QRect(680, 120, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5_Delete_Script.setFont(font)
        self.pushButton_5_Delete_Script.setObjectName("pushButton_5_Delete_Script")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(730, 260, 401, 221))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(730, 200, 401, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 170, 111, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_Select_Script = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Select_Script.setGeometry(QtCore.QRect(730, 30, 271, 31))
        self.comboBox_Select_Script.setObjectName("comboBox_Select_Script")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 10, 111, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(730, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Refresh.setFont(font)
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(740, 120, 151, 41))
        self.label_7.setObjectName("label_7")
        self.lineEdit_Start_Step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Start_Step.setGeometry(QtCore.QRect(860, 120, 111, 41))
        self.lineEdit_Start_Step.setObjectName("lineEdit_Start_Step")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 480, 151, 41))
        self.label_8.setObjectName("label_8")
        self.lineEdit_Target_Step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Target_Step.setGeometry(QtCore.QRect(570, 490, 101, 31))
        self.lineEdit_Target_Step.setObjectName("lineEdit_Target_Step")
        self.pushButton_Insert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Insert.setGeometry(QtCore.QRect(350, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Insert.setFont(font)
        self.pushButton_Insert.setObjectName("pushButton_Insert")
        self.pushButton_Remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Remove.setGeometry(QtCore.QRect(240, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUser_guidance = QtWidgets.QAction(MainWindow)
        self.actionUser_guidance.setObjectName("actionUser_guidance")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menuHelp.addAction(self.actionUser_guidance)
        self.menuHelp.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iCafe Automation Tool"))
        item = self.tableWidget_Script_Display.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Step"))
        item = self.tableWidget_Script_Display.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_Script_Display.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Exection Time(s)"))
        item = self.tableWidget_Script_Display.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Repeat Times"))
        self.pushButton_Load_Script.setText(_translate("MainWindow", "Load"))
        self.pushButton_2_Save_Script.setText(_translate("MainWindow", "Save Script"))
        self.pushButton_3_Run.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "Game Name:"))
        self.label_2.setText(_translate("MainWindow", "Input Mode"))
        self.label_3.setText(_translate("MainWindow", "Script Name:"))
        self.label_4.setText(_translate("MainWindow", "Log:"))
        self.pushButton_4_Add_Script.setText(_translate("MainWindow", "+"))
        self.pushButton_5_Delete_Script.setText(_translate("MainWindow", "-"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Progress:"))
        self.label_6.setText(_translate("MainWindow", "Select Script:"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_7.setText(_translate("MainWindow", "Start from step:"))
        self.label_8.setText(_translate("MainWindow", "Target step:"))
        self.pushButton_Insert.setText(_translate("MainWindow", "Insert"))
        self.pushButton_Remove.setText(_translate("MainWindow", "Remove"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionUser_guidance.setText(_translate("MainWindow", "Guidance"))
        self.actionAuthor.setText(_translate("MainWindow", "Contact Author"))

    def msg_print(self, msg):
        self.textBrowser.append(msg)
        QtWidgets.QApplication.processEvents()

