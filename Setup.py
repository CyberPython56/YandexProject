import datetime
import sys
import sqlite3
from datetime import timedelta, time, datetime
from math import ceil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView, QApplication


class Ui_Form_booking(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 498)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 160, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStatusTip("")
        self.lineEdit_name.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(320, 350, 171, 131))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_5)
        self.dateEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                    "color: white")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 9), QtCore.QTime(12, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_5.addWidget(self.dateEdit)
        self.timeEdit = QtWidgets.QTimeEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                    "color: white")
        self.timeEdit.setReadOnly(False)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 9), QtCore.QTime(12, 0, 0)))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_5.addWidget(self.timeEdit)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                      "color: white")
        self.timeEdit_2.setReadOnly(False)
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 9), QtCore.QTime(13, 0, 0)))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.verticalLayout_5.addWidget(self.timeEdit_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 301, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_choice_club = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox_choice_club.setFont(font)
        self.comboBox_choice_club.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                "color: white\n"
                                                "")
        self.comboBox_choice_club.setObjectName("comboBox_choice_club")
        self.comboBox_choice_club.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_choice_club)
        self.comboBox_choice_VIP = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_choice_VIP.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox_choice_VIP.setFont(font)
        self.comboBox_choice_VIP.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                               "color: white\n"
                                               "")
        self.comboBox_choice_VIP.setEditable(False)
        self.comboBox_choice_VIP.setObjectName("comboBox_choice_VIP")
        self.comboBox_choice_VIP.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_choice_VIP)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_booking1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_booking1.setFont(font)
        self.btn_booking1.setStyleSheet("background-color: rgb(247, 155, 119)")
        self.btn_booking1.setObjectName("btn_booking1")
        self.verticalLayout.addWidget(self.btn_booking1)
        self.btn_sign_in = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_sign_in.setFont(font)
        self.btn_sign_in.setStyleSheet("background-color: rgb(247, 155, 119)\n"
                                       "")
        self.btn_sign_in.setObjectName("btn_sign_in")
        self.verticalLayout.addWidget(self.btn_sign_in)
        self.btn_agree = QtWidgets.QPushButton(Form)
        self.btn_agree.setGeometry(QtCore.QRect(670, 440, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_agree.setFont(font)
        self.btn_agree.setStyleSheet("background-color: white")
        self.btn_agree.setObjectName("btn_agree")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 350, 301, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_choice_date = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_choice_date.setFont(font)
        self.label_choice_date.setStyleSheet("color: white")
        self.label_choice_date.setObjectName("label_choice_date")
        self.verticalLayout_4.addWidget(self.label_choice_date)
        self.label_choice_time = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_choice_time.setFont(font)
        self.label_choice_time.setStyleSheet("color: white")
        self.label_choice_time.setObjectName("label_choice_time")
        self.verticalLayout_4.addWidget(self.label_choice_time)
        self.label_choice_duration = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_choice_duration.setFont(font)
        self.label_choice_duration.setStyleSheet("color: white")
        self.label_choice_duration.setObjectName("label_choice_duration")
        self.verticalLayout_4.addWidget(self.label_choice_duration)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(320, 240, 481, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_address_and_phone = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_address_and_phone.setFont(font)
        self.label_address_and_phone.setStyleSheet("color: white")
        self.label_address_and_phone.setText("")
        self.label_address_and_phone.setObjectName("label_address_and_phone")
        self.verticalLayout_3.addWidget(self.label_address_and_phone)
        self.label_specifications_and_price = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_specifications_and_price.setFont(font)
        self.label_specifications_and_price.setStyleSheet("color: white")
        self.label_specifications_and_price.setText("")
        self.label_specifications_and_price.setObjectName("label_specifications_and_price")
        self.verticalLayout_3.addWidget(self.label_specifications_and_price)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 10, 451, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-rKvzO6WOi8sUhp2.jpg"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "Введите ваше имя..."))
        self.comboBox_choice_club.setItemText(0, _translate("Form", "Выбрать клуб"))
        self.comboBox_choice_VIP.setItemText(0, _translate("Form", "Выбрать зал"))
        self.btn_booking1.setText(_translate("Form", "Забронировать"))
        self.btn_sign_in.setText(_translate("Form", "Авторизация"))
        self.btn_agree.setText(_translate("Form", "Подтвердить"))
        self.label_choice_date.setText(_translate("Form", "Выберите дату:"))
        self.label_choice_time.setText(_translate("Form", "Выберите начальное время:"))
        self.label_choice_duration.setText(_translate("Form", "Выберите конечное время:"))
        self.label_address_and_phone.setWhatsThis(
            _translate("Form", "<html><head/><body><p>фцораиифцюалорфица</p></body></html>"))
        self.label_specifications_and_price.setWhatsThis(
            _translate("Form", "<html><head/><body><p>фцораиифцюалорфица</p></body></html>"))


class Ui_Form_add_club(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 199)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_address = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                            "color: white\n"
                                            "")
        self.lineEdit_address.setText("")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.gridLayout.addWidget(self.lineEdit_address, 1, 1, 1, 1)
        self.lineEdit_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white\n"
                                          "")
        self.lineEdit_title.setText("")
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout.addWidget(self.lineEdit_title, 0, 1, 1, 1)
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("\n"
                                       "color: white\n"
                                       "")
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        self.label_address = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_address.setFont(font)
        self.label_address.setStyleSheet("color: white")
        self.label_address.setObjectName("label_address")
        self.gridLayout.addWidget(self.label_address, 1, 0, 1, 1)
        self.label_phone = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_phone.setFont(font)
        self.label_phone.setStyleSheet("color: white")
        self.label_phone.setObjectName("label_phone")
        self.gridLayout.addWidget(self.label_phone, 2, 0, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white\n"
                                          "")
        self.lineEdit_phone.setText("")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout.addWidget(self.lineEdit_phone, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 150, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reboot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_reboot.setFont(font)
        self.btn_reboot.setStyleSheet("background-color: white")
        self.btn_reboot.setObjectName("btn_reboot")
        self.horizontalLayout.addWidget(self.btn_reboot)
        self.btn_agree = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_agree.setFont(font)
        self.btn_agree.setStyleSheet("background-color: white")
        self.btn_agree.setObjectName("btn_agree")
        self.horizontalLayout.addWidget(self.btn_agree)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "Введите название клуба:"))
        self.label_address.setText(_translate("Form", "Введите адрес:"))
        self.label_phone.setText(_translate("Form", "Введите телефон:"))
        self.btn_reboot.setText(_translate("Form", "Сброс"))
        self.btn_agree.setText(_translate("Form", "Подтвердить"))


class Ui_Form_add_computer(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 217)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 499, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_vip = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_vip.setFont(font)
        self.comboBox_vip.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                        "color: white\n"
                                        "")
        self.comboBox_vip.setObjectName("comboBox_vip")
        self.gridLayout_2.addWidget(self.comboBox_vip, 1, 1, 1, 1)
        self.comboBox_clubs = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_clubs.setFont(font)
        self.comboBox_clubs.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white\n"
                                          "")
        self.comboBox_clubs.setObjectName("comboBox_clubs")
        self.gridLayout_2.addWidget(self.comboBox_clubs, 0, 1, 1, 1)
        self.lineEdit_places = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_places.setFont(font)
        self.lineEdit_places.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                           "color: white\n"
                                           "")
        self.lineEdit_places.setText("")
        self.lineEdit_places.setObjectName("lineEdit_places")
        self.gridLayout_2.addWidget(self.lineEdit_places, 2, 1, 1, 1)
        self.label_vip = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_vip.setFont(font)
        self.label_vip.setStyleSheet("\n"
                                     "color: white\n"
                                     "")
        self.label_vip.setObjectName("label_vip")
        self.gridLayout_2.addWidget(self.label_vip, 1, 0, 1, 1)
        self.label_club = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_club.setFont(font)
        self.label_club.setStyleSheet("\n"
                                      "color: white\n"
                                      "")
        self.label_club.setObjectName("label_club")
        self.gridLayout_2.addWidget(self.label_club, 0, 0, 1, 1)
        self.label_places = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_places.setFont(font)
        self.label_places.setStyleSheet("\n"
                                        "color: white\n"
                                        "")
        self.label_places.setObjectName("label_places")
        self.gridLayout_2.addWidget(self.label_places, 2, 0, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 160, 191, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_reboot = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_reboot.setFont(font)
        self.btn_reboot.setStyleSheet("background-color: white")
        self.btn_reboot.setObjectName("btn_reboot")
        self.horizontalLayout_2.addWidget(self.btn_reboot)
        self.btn_agree = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_agree.setFont(font)
        self.btn_agree.setStyleSheet("background-color: white")
        self.btn_agree.setObjectName("btn_agree")
        self.horizontalLayout_2.addWidget(self.btn_agree)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_vip.setText(_translate("Form", "Выберите тип зала"))
        self.label_club.setText(_translate("Form", "Выберите клуб"))
        self.label_places.setText(_translate("Form", "Введите количество \n"
                                                     "компьютеров"))
        self.btn_reboot.setText(_translate("Form", "Сброс"))
        self.btn_agree.setText(_translate("Form", "Подтвердить"))


class Ui_Form_add_hall(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 271)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_clubs = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_clubs.setFont(font)
        self.comboBox_clubs.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white\n"
                                          "")
        self.comboBox_clubs.setObjectName("comboBox_clubs")
        self.gridLayout.addWidget(self.comboBox_clubs, 0, 1, 1, 1)
        self.lineEdit_places = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_places.setFont(font)
        self.lineEdit_places.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                           "color: white\n"
                                           "")
        self.lineEdit_places.setText("")
        self.lineEdit_places.setObjectName("lineEdit_places")
        self.gridLayout.addWidget(self.lineEdit_places, 2, 1, 1, 1)
        self.label_vip = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_vip.setFont(font)
        self.label_vip.setStyleSheet("\n"
                                     "color: white\n"
                                     "")
        self.label_vip.setObjectName("label_vip")
        self.gridLayout.addWidget(self.label_vip, 1, 0, 1, 1)
        self.lineEdit_specifications = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_specifications.setFont(font)
        self.lineEdit_specifications.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                   "color: white\n"
                                                   "")
        self.lineEdit_specifications.setText("")
        self.lineEdit_specifications.setObjectName("lineEdit_specifications")
        self.gridLayout.addWidget(self.lineEdit_specifications, 4, 1, 1, 1)
        self.label_club = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_club.setFont(font)
        self.label_club.setStyleSheet("\n"
                                      "color: white\n"
                                      "")
        self.label_club.setObjectName("label_club")
        self.gridLayout.addWidget(self.label_club, 0, 0, 1, 1)
        self.label_price = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_price.setFont(font)
        self.label_price.setStyleSheet("\n"
                                       "color: white\n"
                                       "")
        self.label_price.setObjectName("label_price")
        self.gridLayout.addWidget(self.label_price, 3, 0, 1, 1)
        self.label_specifications = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_specifications.setFont(font)
        self.label_specifications.setStyleSheet("\n"
                                                "color: white\n"
                                                "")
        self.label_specifications.setObjectName("label_specifications")
        self.gridLayout.addWidget(self.label_specifications, 4, 0, 1, 1)
        self.lineEdit_price = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white\n"
                                          "")
        self.lineEdit_price.setText("")
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.gridLayout.addWidget(self.lineEdit_price, 3, 1, 1, 1)
        self.label_places = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_places.setFont(font)
        self.label_places.setStyleSheet("\n"
                                        "color: white\n"
                                        "")
        self.label_places.setObjectName("label_places")
        self.gridLayout.addWidget(self.label_places, 2, 0, 1, 1)
        self.comboBox_vip = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_vip.setFont(font)
        self.comboBox_vip.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                        "color: white\n"
                                        "")
        self.comboBox_vip.setObjectName("comboBox_vip")
        self.gridLayout.addWidget(self.comboBox_vip, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 220, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reboot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_reboot.setFont(font)
        self.btn_reboot.setStyleSheet("background-color: white")
        self.btn_reboot.setObjectName("btn_reboot")
        self.horizontalLayout.addWidget(self.btn_reboot)
        self.btn_agree = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_agree.setFont(font)
        self.btn_agree.setStyleSheet("background-color: white")
        self.btn_agree.setObjectName("btn_agree")
        self.horizontalLayout.addWidget(self.btn_agree)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_vip.setText(_translate("Form", "Выберите тип зала"))
        self.label_club.setText(_translate("Form", "Выберите клуб"))
        self.label_price.setText(_translate("Form", "Введите цену каждого ПК"))
        self.label_specifications.setText(_translate("Form", "Введите характеристики ПК"))
        self.label_places.setText(_translate("Form", "Введите количество мест"))
        self.btn_reboot.setText(_translate("Form", "Сброс"))
        self.btn_agree.setText(_translate("Form", "Подтвердить"))


class Ui_Form_admin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(811, 498)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add_computer = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_add_computer.setFont(font)
        self.pushButton_add_computer.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                   "color: white\n"
                                                   "")
        self.pushButton_add_computer.setObjectName("pushButton_add_computer")
        self.gridLayout.addWidget(self.pushButton_add_computer, 0, 2, 1, 1)
        self.pushButton_booking = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_booking.setFont(font)
        self.pushButton_booking.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                              "color: white\n"
                                              "")
        self.pushButton_booking.setObjectName("pushButton_booking")
        self.gridLayout.addWidget(self.pushButton_booking, 1, 2, 1, 1)
        self.pushButton_add_club = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_add_club.setFont(font)
        self.pushButton_add_club.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                               "color: white\n"
                                               "")
        self.pushButton_add_club.setObjectName("pushButton_add_club")
        self.gridLayout.addWidget(self.pushButton_add_club, 0, 1, 1, 1)
        self.pushButton_all_halls = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_all_halls.setFont(font)
        self.pushButton_all_halls.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                "color: white\n"
                                                "")
        self.pushButton_all_halls.setObjectName("pushButton_all_halls")
        self.gridLayout.addWidget(self.pushButton_all_halls, 1, 3, 1, 1)
        self.pushButton_all_clubs = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_all_clubs.setFont(font)
        self.pushButton_all_clubs.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                "color: white\n"
                                                "")
        self.pushButton_all_clubs.setObjectName("pushButton_all_clubs")
        self.gridLayout.addWidget(self.pushButton_all_clubs, 1, 1, 1, 1)
        self.pushButton_add_hall = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_add_hall.setFont(font)
        self.pushButton_add_hall.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                               "color: white\n"
                                               "")
        self.pushButton_add_hall.setObjectName("pushButton_add_hall")
        self.gridLayout.addWidget(self.pushButton_add_hall, 0, 3, 1, 1)
        self.btn_booking = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_booking.setFont(font)
        self.btn_booking.setStyleSheet("background-color: rgb(247, 155, 119)")
        self.btn_booking.setObjectName("btn_booking")
        self.gridLayout.addWidget(self.btn_booking, 0, 0, 1, 1)
        self.btn_sign_in = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_sign_in.setFont(font)
        self.btn_sign_in.setStyleSheet("background-color: rgb(247, 155, 119)\n"
                                       "")
        self.btn_sign_in.setObjectName("btn_sign_in")
        self.gridLayout.addWidget(self.btn_sign_in, 1, 0, 1, 1)
        self.grid = QtWidgets.QTableWidget(Form)
        self.grid.setGeometry(QtCore.QRect(10, 100, 791, 341))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grid.setFont(font)
        self.grid.setStyleSheet("")
        self.grid.setShowGrid(True)
        self.grid.setObjectName("grid")
        self.grid.setColumnCount(0)
        self.grid.setRowCount(0)
        self.btn_cancel_booking = QtWidgets.QPushButton(Form)
        self.btn_cancel_booking.setGeometry(QtCore.QRect(600, 460, 201, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cancel_booking.setFont(font)
        self.btn_cancel_booking.setStyleSheet("background-color: white")
        self.btn_cancel_booking.setObjectName("btn_cancel_booking")
        self.btn_get_club_and_hall = QtWidgets.QPushButton(Form)
        self.btn_get_club_and_hall.setGeometry(QtCore.QRect(420, 460, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_get_club_and_hall.setFont(font)
        self.btn_get_club_and_hall.setStyleSheet("background-color: white")
        self.btn_get_club_and_hall.setObjectName("btn_get_club_and_hall")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_add_computer.setText(_translate("Form", "Добавить компьютер"))
        self.pushButton_booking.setText(_translate("Form", "Бронирования"))
        self.pushButton_add_club.setText(_translate("Form", "Добавить клуб"))
        self.pushButton_all_halls.setText(_translate("Form", "Все залы"))
        self.pushButton_all_clubs.setText(_translate("Form", "Все клубы"))
        self.pushButton_add_hall.setText(_translate("Form", "Добавить зал"))
        self.btn_booking.setText(_translate("Form", "Забронировать"))
        self.btn_sign_in.setText(_translate("Form", "Авторизация"))
        self.btn_cancel_booking.setText(_translate("Form", "Отменить бронь"))
        self.btn_get_club_and_hall.setText(_translate("Form", "Узнать зал и клуб ПК"))


class Ui_Form_get_club_and_hall(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 125)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_id_computer = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_id_computer.setFont(font)
        self.label_id_computer.setStyleSheet("\n"
                                             "color: white\n"
                                             "")
        self.label_id_computer.setObjectName("label_id_computer")
        self.horizontalLayout.addWidget(self.label_id_computer)
        self.lineEdit_id_commputer = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_id_commputer.setFont(font)
        self.lineEdit_id_commputer.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                                 "color: white\n"
                                                 "")
        self.lineEdit_id_commputer.setText("")
        self.lineEdit_id_commputer.setObjectName("lineEdit_id_commputer")
        self.horizontalLayout.addWidget(self.lineEdit_id_commputer)
        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(320, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("background-color: white")
        self.btn_search.setObjectName("btn_search")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_id_computer.setText(_translate("Form", "Введите id компьютера:"))
        self.btn_search.setText(_translate("Form", "Найти клуб и зал"))


class Ui_Form_login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 197)
        Form.setStyleSheet("background-color: rgb(75, 67, 69)")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 211, 105))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                          "color: white")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color: rgb(16, 42, 73);\n"
                                             "color: white")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_sign_in_ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_sign_in_.setFont(font)
        self.pushButton_sign_in_.setStyleSheet("background-color: rgb(247, 155, 119)\n"
                                               "")
        self.pushButton_sign_in_.setObjectName("pushButton_sign_in_")
        self.horizontalLayout.addWidget(self.pushButton_sign_in_)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_login.setPlaceholderText(_translate("Form", "Login..."))
        self.lineEdit_password.setPlaceholderText(_translate("Form", "Password..."))
        self.pushButton_sign_in_.setText(_translate("Form", "Войти в аккаунт"))


class Login(QWidget, Ui_Form_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_sign_in_.clicked.connect(self.check_login_and_password)
        self.setWindowTitle('Авторизация')

    def check_login_and_password(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            logins = cur.execute("""SELECT login FROM admins""").fetchall()
            logins = [i[0] for i in logins]
            if login in logins:
                password_of_login = cur.execute(f"""SELECT password FROM admins WHERE login = '{login}'""").fetchone()[
                    0]
                if password_of_login == password:
                    return True
                return False


class Admin(QWidget, Ui_Form_admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(550, 300)
        self.setWindowTitle('Для админов')
        # self.grid.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.grid.hide()
        self.all_grid = ['clubs', 'booking', 'halls']
        self.which_grid = None

        self.pushButton_all_clubs.clicked.connect(self.view_clubs)
        self.pushButton_all_halls.clicked.connect(self.view_halls)
        self.pushButton_booking.clicked.connect(self.view_booking)
        self.btn_booking.clicked.connect(self.open_booking)
        self.btn_cancel_booking.clicked.connect(self.explore_id)
        self.pushButton_add_club.clicked.connect(self.add_club)
        self.pushButton_add_hall.clicked.connect(self.add_hall)
        self.pushButton_add_computer.clicked.connect(self.add_computer)
        self.btn_get_club_and_hall.clicked.connect(self.get_club_and_hall)

        self.btn_cancel_booking.hide()
        self.btn_get_club_and_hall.hide()

    def open_booking(self):
        pass

    def view_clubs(self):
        self.btn_get_club_and_hall.hide()
        self.btn_cancel_booking.setText('Удалить клуб')
        self.which_grid = self.all_grid[0]
        self.setWindowTitle('Все клубы')
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            columns = cur.execute("""SELECT * FROM clubs""").fetchone()
            rows = cur.execute("""SELECT count(*) FROM clubs""").fetchone()[0]
            self.all_info_clubs = cur.execute("""SELECT * FROM clubs""").fetchall()

            self.grid.setColumnCount(len(columns))
            self.grid.setHorizontalHeaderLabels(['id', 'Название', 'Адрес', 'Телефон'])
            self.grid.verticalHeader().setVisible(False)
            header = self.grid.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

            self.grid.setRowCount(len(self.all_info_clubs))

            for i, row in enumerate(self.all_info_clubs):
                for j, elem in enumerate(row):
                    self.grid.setItem(i, j, QTableWidgetItem(str(elem)))

            self.grid.setStyleSheet("""
                        QTableWidget{
                            background-color: rgb(75, 67, 69);
                            color: white;
                        }

                    """)
            self.grid.show()
            self.btn_cancel_booking.show()

    def view_halls(self):
        self.btn_get_club_and_hall.hide()
        self.btn_cancel_booking.setText('Удалить зал')
        self.which_grid = self.all_grid[2]
        self.setWindowTitle('Все залы')
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            columns = cur.execute("""SELECT * FROM halls""").fetchone()
            rows = cur.execute("""SELECT count(*) FROM halls""").fetchone()[0]
            self.all_info_halls = cur.execute("""SELECT * FROM halls""").fetchall()

            self.grid.setColumnCount(len(columns))
            self.grid.setHorizontalHeaderLabels(['id зала', 'Название клуба', 'Тип зала', 'Всего мест',
                                                 'Цена за компьютер', 'Характеристики каждого ПК'])
            self.grid.verticalHeader().setVisible(False)

            header = self.grid.horizontalHeader()
            header.setSectionResizeMode(5, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

            self.grid.setRowCount(len(self.all_info_halls))
            for i, row in enumerate(self.all_info_halls):
                with sqlite3.connect('YandexProject.sqlite') as con:
                    cur = con.cursor()
                club_name = cur.execute(f"""SELECT title FROM clubs WHERE clubid = {row[1]}""").fetchone()[0]
                for j, elem in enumerate(row):
                    if j == 1:
                        self.grid.setItem(i, j, QTableWidgetItem(str(club_name)))
                    else:
                        self.grid.setItem(i, j, QTableWidgetItem(str(elem)))

            self.grid.setStyleSheet("""
                                    QTableWidget{
                                        background-color: rgb(75, 67, 69);
                                        color: white;
                                    }

                                """)
            self.grid.show()
            self.btn_cancel_booking.show()

    def view_booking(self):
        self.btn_get_club_and_hall.show()
        self.btn_cancel_booking.setText('Отменить бронирование')
        self.which_grid = self.all_grid[1]
        self.setWindowTitle('Все бронирования')
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            columns = cur.execute("""SELECT * FROM booking""").fetchone()
            rows = cur.execute("""SELECT count(*) FROM booking""").fetchone()[0]
            self.all_info_booking = cur.execute("""SELECT * FROM booking""").fetchall()

            self.grid.setColumnCount(len(columns))
            self.grid.setHorizontalHeaderLabels(['id бронирования', 'id компьютера', 'Имя', 'Дата', 'Время начала',
                                                 'Время конца', 'Итоговая стоимость'])
            self.grid.verticalHeader().setVisible(False)

            header = self.grid.horizontalHeader()
            header.setSectionResizeMode(2, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QHeaderView.ResizeToContents)

            self.grid.setRowCount(len(self.all_info_booking))

            for i, row in enumerate(self.all_info_booking):
                for j, elem in enumerate(row):
                    self.grid.setItem(i, j, QTableWidgetItem(str(elem)))

            self.grid.setStyleSheet("""
                                    QTableWidget{
                                        background-color: rgb(75, 67, 69);
                                        color: white;
                                    }

                                """)
            self.grid.show()
            self.btn_cancel_booking.show()

    def update_window(self):
        if self.which_grid == self.all_grid[0]:
            self.view_clubs()
        if self.which_grid == self.all_grid[1]:
            self.view_booking()
        if self.which_grid == self.all_grid[2]:
            self.view_halls()

    def explore_id(self):
        if self.which_grid == self.all_grid[1]:
            row = self.grid.currentIndex().row()
            id = self.grid.item(row, 0).text()
            warning_delete_booking = QMessageBox()
            warning_delete_booking.setWindowTitle('Удаление бронирования')
            warning_delete_booking.setText(f'Вы уверены, что хотите удалить бронирование №{id}?'
                                           '\nЭтот элемент будет удален навсегда')
            warning_delete_booking.setIcon(QMessageBox.Question)
            warning_delete_booking.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            warning_delete_booking.buttonClicked.connect(self.cancel_booking)
            warning_delete_booking.exec()

        elif self.which_grid == self.all_grid[0]:
            row = self.grid.currentIndex().row()
            title = self.grid.item(row, 1).text()
            warning_delete_club = QMessageBox()
            warning_delete_club.setWindowTitle('Удаление клуба')
            warning_delete_club.setText(f'Вы уверены, что хотите удалить клуб {title}?'
                                        '\nЭтот элемент будет удален навсегда')
            warning_delete_club.setIcon(QMessageBox.Question)
            warning_delete_club.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            warning_delete_club.buttonClicked.connect(self.delete_club)
            warning_delete_club.exec()

        elif self.which_grid == self.all_grid[2]:
            row = self.grid.currentIndex().row()
            vip = self.grid.item(row, 2).text()
            warning_delete_hall = QMessageBox()
            warning_delete_hall.setWindowTitle('Удаление зала')
            warning_delete_hall.setText(f'Вы уверены, что хотите удалить {vip}?'
                                        '\nЭтот элемент будет удален навсегда')
            warning_delete_hall.setIcon(QMessageBox.Question)
            warning_delete_hall.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            warning_delete_hall.buttonClicked.connect(self.delete_hall)
            warning_delete_hall.exec()

    def cancel_booking(self, btn):
        if btn.text() == 'OK':
            row = self.grid.currentIndex().row()
            id = self.grid.item(row, 0).text()
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                cur.execute(f"""DELETE FROM booking WHERE bookingid = {id}""")
            self.update_window()

    def delete_club(self, btn):
        if btn.text() == 'OK':
            row = self.grid.currentIndex().row()
            id = self.grid.item(row, 0).text()
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                cur.execute(f"""DELETE FROM halls WHERE clubid = {id}""")
                cur.execute(f"""DELETE FROM clubs WHERE clubid = {id}""")
            self.update_window()

    def delete_hall(self, btn):
        if btn.text() == 'OK':
            row = self.grid.currentIndex().row()
            id = self.grid.item(row, 0).text()
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                cur.execute(f"""DELETE FROM halls WHERE hallid = {id}""")
            self.update_window()

    def add_club(self):
        self.window = AddClub()
        self.window.show()

    def add_hall(self):
        self.window = AddHall()
        self.window.show()

    def add_computer(self):
        self.window = AddComputer()
        self.window.show()

    def get_club_and_hall(self):
        self.window = ClubAndHall()
        self.window.show()


class AddClub(QWidget, Ui_Form_add_club):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавление клуба')
        self.btn_agree.clicked.connect(self.run)
        self.btn_reboot.clicked.connect(self.reboot)

    def run(self):
        if self.lineEdit_title.text() != '' and self.lineEdit_address.text() != '' and self.lineEdit_phone.text() != '':
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                cur.execute(f"""INSERT INTO clubs(title, address, phone) VALUES('{self.lineEdit_title.text()}',
                '{self.lineEdit_address.text()}', '{self.lineEdit_phone.text()}')""")
            add_club_res = QMessageBox()
            add_club_res.setWindowTitle('Клуб успешно добавлен')
            add_club_res.setText(f'Клуб {self.lineEdit_title.text()} добавлен')
            add_club_res.setIcon(QMessageBox.Information)
            add_club_res.setStandardButtons(QMessageBox.Ok)
            add_club_res.exec()
            self.close()
        else:
            warning_not_data = QMessageBox()
            warning_not_data.setWindowTitle('Неккоректность данных')
            warning_not_data.setText(f'Введите все данные о клубе')
            warning_not_data.setIcon(QMessageBox.Warning)
            warning_not_data.setStandardButtons(QMessageBox.Ok)
            warning_not_data.exec()

    def reboot(self):
        self.lineEdit_title.setText('')
        self.lineEdit_address.setText('')
        self.lineEdit_phone.setText('')


class AddHall(QWidget, Ui_Form_add_hall):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавление зала')
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            clubs0 = cur.execute("""SELECT title FROM clubs""").fetchall()
            clubs = []
            for i in clubs0:
                clubs.append(*i)
        self.comboBox_clubs.addItems(clubs)
        self.comboBox_vip.addItems(['Обычный зал', 'VIP-зал'])
        self.btn_agree.clicked.connect(self.run)
        self.btn_reboot.clicked.connect(self.reboot)

    def run(self):
        if self.lineEdit_places.text() != '' and self.lineEdit_price.text() != '' \
                and self.lineEdit_specifications.text() != '':
            with sqlite3.connect("YandexProject.sqlite") as con:
                cur = con.cursor()
                cur_club = self.comboBox_clubs.currentText()
                cur_club_id = cur.execute(f"""SELECT clubid FROM clubs WHERE title = '{cur_club}'""").fetchone()[0]
                cur_hall = self.comboBox_vip.currentText()
                cur.execute(f"""INSERT INTO halls(clubid, vip, places, price, specifications)
                            VALUES({cur_club_id}, '{cur_hall}', {self.lineEdit_places.text()},
                            {self.lineEdit_price.text()}, '{self.lineEdit_specifications.text()}')""")
            add_hall_res = QMessageBox()
            add_hall_res.setWindowTitle('Зал успешно добавлен')
            add_hall_res.setText(f'{self.comboBox_vip.currentText()} в клуб {cur_club} успешно добавлен')
            add_hall_res.setIcon(QMessageBox.Information)
            add_hall_res.setStandardButtons(QMessageBox.Ok)
            add_hall_res.exec()
            self.close()

        else:
            warning_not_data = QMessageBox()
            warning_not_data.setWindowTitle('Неккоректность данных')
            warning_not_data.setText(f'Введите все данные о клубе')
            warning_not_data.setIcon(QMessageBox.Warning)
            warning_not_data.setStandardButtons(QMessageBox.Ok)
            warning_not_data.exec()

    def reboot(self):
        self.lineEdit_places.setText('')
        self.lineEdit_price.setText('')
        self.lineEdit_specifications.setText('')


class AddComputer(QWidget, Ui_Form_add_computer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавление компьютера')
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            clubs0 = cur.execute("""SELECT title FROM clubs""").fetchall()
            clubs = []
            for i in clubs0:
                clubs.append(*i)
        self.comboBox_clubs.addItems(clubs)
        self.comboBox_vip.addItems(['Обычный зал', 'VIP-зал'])
        self.btn_agree.clicked.connect(self.run)
        self.btn_reboot.clicked.connect(self.reboot)

    def run(self):
        if self.lineEdit_places.text() != '':
            with sqlite3.connect("YandexProject.sqlite") as con:
                cur = con.cursor()
                cur_club = self.comboBox_clubs.currentText()
                cur_club_id = cur.execute(f"""SELECT clubid FROM clubs WHERE title = '{cur_club}'""").fetchone()[0]
                cur_hall = self.comboBox_vip.currentText()
                cur_hall_id = cur.execute(f"""SELECT hallid FROM halls 
                    WHERE clubid = {cur_club_id} AND vip = '{cur_hall}'""").fetchone()[0]
                for i in range(int(self.lineEdit_places.text())):
                    cur.execute(f"""INSERT INTO computers(hallid) VALUES({cur_hall_id})""")
                    cur.execute(f"""UPDATE halls SET places = places + 1 WHERE hallid = {cur_hall_id}""")
                add_hall_res = QMessageBox()
                add_hall_res.setWindowTitle('Компьютер(ы) успешно добавлен(ы)')
                add_hall_res.setText(f'{self.lineEdit_places.text()} Компьютер(а/ов) в '
                                     f'{self.comboBox_vip.currentText()} клуба {cur_club} успешно добавлен(ы)')
                add_hall_res.setIcon(QMessageBox.Information)
                add_hall_res.setStandardButtons(QMessageBox.Ok)
                add_hall_res.exec()
                self.close()

        else:
            warning_not_data = QMessageBox()
            warning_not_data.setWindowTitle('Неккоректность данных')
            warning_not_data.setText(f'Укажите количество мест')
            warning_not_data.setIcon(QMessageBox.Warning)
            warning_not_data.setStandardButtons(QMessageBox.Ok)
            warning_not_data.exec()

    def reboot(self):
        self.lineEdit_places.setText('')


class ClubAndHall(QWidget, Ui_Form_get_club_and_hall):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.clicked.connect(self.run)
        self.setWindowTitle('Узнать клуб и зал по id')

    def run(self):
        if self.lineEdit_id_commputer.text() != '':
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                hall_type = cur.execute(f"""SELECT vip FROM halls WHERE clubid = (SELECT hallid FROM computers 
                    WHERE computerid = {int(self.lineEdit_id_commputer.text())})""").fetchone()[0]
                club_title = cur.execute(f"""SELECT title from clubs WHERE clubid = (SELECT clubid FROM halls 
                    WHERE hallid = (SELECT hallid FROM computers 
                    WHERE computerid = {int(self.lineEdit_id_commputer.text())}))""").fetchone()[0]
                print(hall_type, club_title)
                if hall_type and club_title:
                    result = QMessageBox()
                    result.setWindowTitle('Выполнено')
                    result.setText(f'Клуб {club_title} {hall_type}')
                    result.setIcon(QMessageBox.Information)
                    result.setStandardButtons(QMessageBox.Ok)
                    result.exec()

                else:
                    result = QMessageBox()
                    result.setWindowTitle('ПК не найден')
                    result.setText(f'Компьютер с id {self.lineEdit_id_commputer.text().lower()} не найден')
                    result.setIcon(QMessageBox.Warning)
                    result.setStandardButtons(QMessageBox.Ok)
                    result.exec()

        else:
            warning_id = QMessageBox()
            warning_id.setWindowTitle('Некоторекктные данные')
            warning_id.setText(f'Введите id компьютера')
            warning_id.setIcon(QMessageBox.Warning)
            warning_id.setStandardButtons(QMessageBox.Ok)
            warning_id.exec()


class Booking(QWidget, Ui_Form_booking):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(550, 300)
        self.setWindowTitle('Забронировать')

        self.admin = Admin()
        self.login = Login()

        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            clubs0 = cur.execute("""SELECT title FROM clubs""").fetchall()
            self.clubs = []
            for i in clubs0:
                self.clubs.append(*i)
        now_date_time = datetime.now()
        self.dateEdit.setDate(now_date_time.date())
        time_start_delta = now_date_time + timedelta(hours=1)
        self.timeEdit.setTime(time_start_delta.time())
        time_finish_delta = now_date_time + timedelta(hours=2)
        self.timeEdit_2.setTime(time_finish_delta.time())

        self.halls = ['Обычный зал', 'VIP-зал']
        self.cur_club = self.comboBox_choice_club.currentText()

        self.comboBox_choice_club.addItems(self.clubs)
        self.comboBox_choice_VIP.addItems(self.halls)

        self.comboBox_choice_club.currentIndexChanged.connect(self.set_address_and_phone)
        self.comboBox_choice_VIP.currentIndexChanged.connect(self.set_specifications_and_price)
        self.btn_agree.clicked.connect(self.set_booking)

        self.btn_sign_in.clicked.connect(self.open_sign_in)

    def open_sign_in(self):
        if not self.login.check_login_and_password():
            self.login.show()
            self.login.pushButton_sign_in_.clicked.connect(self.open_admin)
        else:
            self.open_admin()

    def open_admin(self):
        if self.login.check_login_and_password():
            self.admin.btn_sign_in.setText('Выполнен вход')
            self.btn_sign_in.setText('Выполнен вход')
            self.admin.show()
            self.login.close()
            self.hide()
            self.admin.btn_booking.clicked.connect(self.open_booking)
        else:
            error_login = QMessageBox()
            error_login.setWindowTitle('Неправильный логин или пароль')
            error_login.setText('Пожалуйста, проверьте правильность ввода данных!')
            error_login.setIcon(QMessageBox.Warning)
            error_login.exec()

    def open_booking(self):
        self.show()
        self.admin.hide()

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.set_booking()

    def set_address_and_phone(self):
        self.cur_club = self.comboBox_choice_club.currentText()

        if self.cur_club in self.clubs:
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()
                address = cur.execute(f"""SELECT address FROM clubs WHERE title = '{self.cur_club}'""").fetchone()[0]
                phone = cur.execute(f"""SELECT phone FROM clubs WHERE title = '{self.cur_club}'""").fetchone()[0]
                self.label_address_and_phone.setText('Адрес: ' + address + '. Телефон: ' + phone)
                self.set_specifications_and_price()
        else:
            self.label_address_and_phone.setText('')
            self.label_specifications_and_price.setText('')

    def set_specifications_and_price(self):
        if self.cur_club != 'Выбрать клуб':
            self.cur_hall = self.comboBox_choice_VIP.currentText()

            if self.cur_hall in self.halls:
                with sqlite3.connect('YandexProject.sqlite') as con:
                    cur = con.cursor()

                    specifications = cur.execute(f"""SELECT specifications FROM halls WHERE VIP = '{self.cur_hall}' AND clubid = 
                    (SELECT clubid FROM clubs WHERE title = '{self.cur_club}')""").fetchone()[0]
                    price = cur.execute(f"""SELECT price FROM halls WHERE VIP = '{self.cur_hall}' AND clubid = 
                    (SELECT clubid FROM clubs WHERE title = '{self.cur_club}')""").fetchone()[0]
                    self.label_specifications_and_price.setText('Характеристики: ' + str(specifications) +
                                                                '. \nЦена: ' + str(price) + ' рублей/час')

    def set_booking(self):
        hours0 = int(self.timeEdit.text().split(':')[0])
        minutes0 = int(self.timeEdit.text().split(':')[1])
        start_time = time(hours0, minutes0)
        hours1 = int(self.timeEdit_2.text().split(':')[0])
        minutes1 = int(self.timeEdit_2.text().split(':')[1])
        finish_time = time(hours1, minutes1)

        date0 = list(map(int, self.dateEdit.text().split('.')))
        time_booking0 = list(map(int, self.timeEdit.text().split(':')))
        self.datetime_booking = datetime(day=date0[0], month=date0[1], year=date0[2],
                                         hour=time_booking0[0], minute=time_booking0[1])
        self.datetime_now = datetime.now()

        if finish_time > start_time and self.lineEdit_name.text() != '' \
                and self.comboBox_choice_club.currentText() != 'Выбрать клуб' \
                and self.comboBox_choice_VIP.currentText() != 'Выбрать зал' \
                and self.datetime_now < self.datetime_booking:
            with sqlite3.connect('YandexProject.sqlite') as con:
                cur = con.cursor()

                halls0 = cur.execute(f"""SELECT computerid FROM computers WHERE hallid =
                (SELECT hallid FROM halls WHERE vip = '{self.cur_hall}' AND clubid =
                (SELECT clubid FROM clubs WHERE title = '{self.cur_club}'))""").fetchall()

                self.seats = list(map(lambda x: x[1:-2], list(map(str, halls0))))
                first_id = int(self.seats[0])
                last_id = int(self.seats[-1])
                self.flag_booking_complete = False
                # while not self.flag_booking_complete:
                for i in range(len(self.seats)):
                    if not self.flag_booking_complete:
                        self.id = self.seats[i]
                        self.flag_can_book = True
                        self.can_booking(self.timeEdit.text(), self.timeEdit_2.text(), self.id)
                        if self.flag_can_book:
                            self.booking_sqlite()
                            self.flag_booking_complete = True
                if self.flag_booking_complete:
                    booking_successful = QMessageBox()
                    booking_successful.setWindowTitle('Бронирование выполнено успешно!')
                    booking_successful.setText(f'Вы забронировали компьютер №{self.id} в клубе '
                                               f'{self.cur_club}\n{self.dateEdit.text()} с {self.timeEdit.text()} '
                                               f'до {self.timeEdit_2.text()}. \n{self.cur_hall}, цена за '
                                               f'{self.time_delta} часа(ов) {self.full_price} рублей')
                    booking_successful.setIcon(QMessageBox.Information)
                    booking_successful.setStandardButtons(QMessageBox.Ok)
                    booking_successful.exec()

                else:
                    booking_successful = QMessageBox()
                    booking_successful.setWindowTitle('Мест нет')
                    booking_successful.setText(f'Извините, на это время все компьютеры заняты'
                                               f'\nПожалуйста выберите другое время')
                    booking_successful.setIcon(QMessageBox.Information)
                    booking_successful.setStandardButtons(QMessageBox.Ok)
                    booking_successful.exec()




        else:
            if start_time > finish_time:
                error_time = QMessageBox()
                error_time.setWindowTitle('Некорректность ввода времени')
                error_time.setText('Конечное время не может быть раньше начального!')
                error_time.setIcon(QMessageBox.Warning)
                error_time.exec()

            elif self.lineEdit_name.text() == '':
                error_name = QMessageBox()
                error_name.setWindowTitle('Некорректность ввода имени')
                error_name.setText('Введите имя! Оно нужно для бронирования компьютера')
                error_name.setIcon(QMessageBox.Warning)
                error_name.exec()

            elif self.comboBox_choice_club.currentText() == 'Выбрать клуб':
                error_club = QMessageBox()
                error_club.setWindowTitle('Некорректность выбора клуба')
                error_club.setText('Выберите клуб, в котором хотите забронировать ПК!')
                error_club.setIcon(QMessageBox.Warning)
                error_club.exec()

            elif self.datetime_now > self.datetime_booking:
                error_club = QMessageBox()
                error_club.setWindowTitle('Некорректность выбора времени')
                error_club.setText('Выбранное вами время уже прошло!')
                error_club.setIcon(QMessageBox.Warning)
                error_club.exec()

            else:
                error_club = QMessageBox()
                error_club.setWindowTitle('Некорректность выбора зала')
                error_club.setText('Выберите зал, в котором хотите забронировать ПК!')
                error_club.setIcon(QMessageBox.Warning)
                error_club.exec()

    def booking_sqlite(self):
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            price0 = cur.execute(f"""SELECT price FROM halls WHERE hallid =
                                (SELECT hallid FROM computers WHERE computerid = '{self.id}')""").fetchone()
            price = price0[0]
            time0 = self.timeEdit.text().split(':')
            time1 = self.timeEdit_2.text().split(':')
            time_delta0 = timedelta(hours=int(time0[0]), minutes=int(time0[1]))
            time_delta1 = timedelta(hours=int(time1[0]), minutes=int(time1[1]))
            self.time_delta = time_delta1 - time_delta0
            self.time_delta = ceil(self.time_delta.seconds / 3600)
            self.full_price = price * self.time_delta
            cur.execute(f"""INSERT INTO booking(ComputerId, date, time_start, time_finish,
                                    full_price, name) VALUES({self.id}, '{self.dateEdit.text()}',
                                    '{self.timeEdit.text()}', '{self.timeEdit_2.text()}',
                                    {self.full_price}, '{self.lineEdit_name.text()}')""")

    def can_booking(self, time_start, time_finish, computer):
        with sqlite3.connect('YandexProject.sqlite') as con:
            cur = con.cursor()
            bookings = cur.execute(f"""SELECT * FROM booking WHERE computerid = {computer} 
                AND date = '{self.dateEdit.text()}'""").fetchall()
            for i in bookings:
                self.flag_time = False
                self.check_time(time_start, time_finish, i[4], i[5])
                if self.flag_time:
                    self.flag_can_book = False

    def check_time(self, t0_self, t1_self, t0_other, t1_other):
        time_start = tuple([int(t0_self.split(':')[0]), int(t0_self.split(':')[1])])
        time_finish = tuple([int(t1_self.split(':')[0]), int(t1_self.split(':')[1])])
        time_start_other = tuple([int(t0_other.split(':')[0]), int(t0_other.split(':')[1])])
        time_finish_other = tuple([int(t1_other.split(':')[0]), int(t1_other.split(':')[1])])

        time_start = time(time_start[0], time_start[1])
        time_finish = time(time_finish[0], time_finish[1])
        time_start_other = time(time_start_other[0], time_start_other[1])
        time_finish_other = time(time_finish_other[0], time_finish_other[1])

        if (time_start_other < time_start < time_finish_other \
            or time_start_other < time_finish < time_finish_other) \
                or (time_start <= time_start_other and time_finish >= time_finish_other) \
                or (time_start >= time_start_other and time_finish <= time_finish_other):
            self.flag_time = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    book = Booking()
    book.show()
    sys.exit(app.exec())
