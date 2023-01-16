import sys
import time
import ast
import pymysql
import matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("smartapp.ui")[0]
class Smart_App(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_stackedWidget.setCurrentIndex(0)

        #회원가입 및 로그인 관련
        self.signup_btn.clicked.connect(self.signup) # 회원가입창으로
        self.sign_in_btn.clicked.connect(self.signin) # 가입하기버튼 눌렀을때
        self.confirm_btn.clicked.connect(self.confirm_id)# 아이디 중복확인
        self.login_btn.clicked.connect(self.log_in)#로그인 버튼 눌렀을때
        self.move_log_btn.clicked.connect(self.login_page) # 로그인창 눌렀을때

    def login_page(self):#로그인창으로
        self.login_stackedWidget.setCurrentIndex(0)

    def log_in(self): # 로그인창에서 로그인버튼 눌렀을때
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",
                               charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT id FROM user_info WHERE BINARY id='{self.id_lineEdit.text()}' and password='{self.password_lineEdit.text()}'");
        id_count=c.fetchall()
        # print(id_count[0][0])
        if id_count !=() and self.id_lineEdit.text()==id_count[0][0]:
            QMessageBox.about(self, "알림", "로그인성공")
            self.login_stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.about(self, "알림", "아이디나 비밀번호가 틀립니다")


    def signup(self): # 회원가입창
        self.login_stackedWidget.setCurrentIndex(1)
        self.id_input_lineEdit.clear()
        self.password_input_lineEdit.clear()
        self.re_password_lineEdit.clear()
        self.name_lineEdit.clear()
        self.address_lineEdit.clear()


    def confirm_id(self):
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT COUNT(id) from user_info WHERE id='{self.id_input_lineEdit.text()}'");
        id_compare=c.fetchall()
        print(id_compare)
        if id_compare[0][0] == 1:
            QMessageBox.about(self, "알림", "아이디 중복")
        else:
            QMessageBox.about(self, "알림", "사용가능한 아이디")
        conn.close()
    def signin(self): # 가입하기 눌렀을때
        self.sign_id = self.id_input_lineEdit.text()
        self.sign_password = self.password_input_lineEdit.text()
        self.re_password = self.re_password_lineEdit.text()
        self.sign_name = self.name_lineEdit.text()
        self.sign_address = self.address_lineEdit.text()
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()

        if self.sign_id != "" and self.sign_password != "" and self.re_password != "" and self.sign_name != "" and self.sign_address != "":
            c.execute(f"SELECT COUNT(id) from user_info WHERE id='{self.sign_id}'");
            compare_id=c.fetchall()
            if compare_id[0][0]==0:
                if self.sign_password == self.re_password:
                    c.execute(f"INSERT INTO user_info (id, password, name, address) VALUES ('{self.sign_id}','{self.sign_password}','{self.sign_name}', '{self.sign_address}')")
                    QMessageBox.about(self, "알림", "회원가입완료")
                    self.login_stackedWidget.setCurrentIndex(0)
                else:
                    QMessageBox.about(self, "알림", "비밀번호가 다릅니다")
            else:
                QMessageBox.about(self, "알림", "회원가입 안됩니다")
        else:
            QMessageBox.about(self, "경고창", "빈칸없이 입력하세요")
        conn.commit()
        conn.close()


if __name__=="__main__":
    app=QApplication(sys.argv)
    popup=Smart_App()
    popup.show()
    app.exec_()
