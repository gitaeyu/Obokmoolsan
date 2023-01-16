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

form_class=uic.loadUiType("smartappg.ui")[0]
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
        self.admin_signal=False # 처음에 로그인 안되어있을때
        self.user_signal=False # 처음에 로그인 안되어있을때
        #로그아웃
        self.user_logout_btn.clicked.connect(self.log_out)
        self.admin_logout_btn.clicked.connect(self.log_out)

        #관리자 관련
        self.add_menu_btn.clicked.connect(self.menu_add)# 상품등록 페이지로
        self.adding_menu_btn.clicked.connect(self.plus_menu)# #상품등록 버튼
        self.insert_btn.clicked.connect(self.add_bom)# bom등록하기

        #관리자 페이지에서 이동
        self.bom_btn.clicked.connect(self.bom_page) # bom 창으로 이동

        #사용자 페이지로 이동
        self.user_page_btn3.clicked.connect(self.user_page)
        self.user_page_btn4.clicked.connect(self.user_page)

        #관리자 페이지로 이등
        self.admin_page_btn_6.clicked.connect(self.admin_page)
        self.admin_page_btn_7.clicked.connect(self.admin_page)
        self.admin_page_btn_8.clicked.connect(self.admin_page)
        self.admin_page_btn_9.clicked.connect(self.admin_page)
        self.admin_page_btn_10.clicked.connect(self.admin_page)

#=================================기태======================================
        #기본 페이지 지정 (관리자 페이지)
        self.login_stackedWidget.setCurrentIndex(5)
        #상호작용 버튼
        self.see_order_btn.clicked.connect(self.move_order_manage)
        self.inventory_btn.clicked.connect(self.move_inventory)
        self.login_stackedWidget.setCurrentIndex(5)
        self.admin_page_btn_6.clicked.connect(self.move_admin_page)
        self.admin_page_btn_7.clicked.connect(self.move_admin_page)
        self.admin_page_btn_9.clicked.connect(self.move_admin_page)
        self.see_not_receive_btn.clicked.connect(self.see_not_received_order)
        self.see_qna_btn.clicked.connect(self.see_qna_manage)
        self.renew_order_manage_btn.clicked.connect(self.renew_order_manage_list)
        self.order_status_change_btn.clicked.connect(self.order_status_change)
        self.see_not_receive_btn.clicked.connect(self.see_not_received_order) # 접수되지 않은 주문 확인하기
        self.order_status_change_btn.clicked.connect(self.order_status_change) # 주문 상태 변경 시켜줌 (주문,접수,완료)
        # qna창에서 주문번호가 있는 항목 선택하여 버튼 누르면 이동
        self.see_selected_order_btn.clicked.connect(self.see_selected_order)
        self.inventory_cb.currentIndexChanged.connect(self.calculate_min_item)
        self.ingredient_order_btn.clicked.connect(self.order_ingredient)
        self.ira = inventory_renew_alarm(self)

        self.inventory_cb.currentIndexChanged.connect(self.calculate_min_item) # 최대 개수 계산
        self.ingredient_order_btn.clicked.connect(self.order_ingredient) #재고 발주
        self.ira = inventory_renew_alarm(self) # 재고 부족 알림 스레드 생성
        self.inventorySignal = True
        self.ira.start() #재고 부족 알림 스레드 시작
#====================================기태====================================================







    def bom_page(self): # bom으로 이동
        self.add_code_comboBox.clear()
        self.login_stackedWidget.setCurrentIndex(8)
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute("SELECT 메뉴코드 FROM menulist")
        menu_code=c.fetchall()
        print(menu_code)
        for i in menu_code:
            self.add_code_comboBox.addItem(i[0])
        conn.close()

    def add_bom(self): #bom 추가하기
        add_code=self.add_code_comboBox.currentText()
        print(add_code)
        menuname=self.menuname_lineEdit.text()
        print(menuname)
        add_ingre=self.ingredient_lineEdit.text()
        print(add_ingre)
        ingre_code=self.ingre_code_lineEdit.text()
        print(ingre_code)
        unit_name=self.quantity_lineEdit.text()
        print(unit_name)
        unit_combo=self.unit_comboBox.currentText()
        print(unit_combo)
        price_name=self.price_lineEdit.text()
        print(price_name)
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT count(*) FROM bom WHERE 메뉴코드='{self.add_code_comboBox.currentText()}' AND 요리='{self.menuname_lineEdit.text()}' AND 재료이름='{self.ingredient_lineEdit.text()}' ")
        bom_data=c.fetchall()
        print(bom_data[0][0])
        if bom_data[0][0] == 0:
            if add_code != "" and menuname != "" and add_ingre != "" and ingre_code != "" and unit_name != "" and unit_combo != "" and price_name != "":
                print('hoi')
                c.execute(f"INSERT INTO bom (메뉴코드, 요리, 재료이름, 재료코드, 수량, 단위, 단가) VALUES ('{add_code}', '{menuname}', '{add_ingre}', '{ingre_code}', '{unit_name}', '{unit_combo}', '{price_name}')");
                print('sb')
            else:
                QMessageBox.about(self, "알림", "빈칸 입력하세요")
                # pass
        elif bom_data[0][0] == 1:
            QMessageBox.about(self, "알림", "존재하는 내용입니다")
        conn.commit()
        conn.close()
    def admin_page(self): # 관리자 페이지로 이동
        self.login_stackedWidget.setCurrentIndex(5)

    def user_page(self):
        self.login_stackedWidget.setCurrentIndex(2)


    def menu_add(self): # 상품등록 페이지로
        self.login_stackedWidget.setCurrentIndex(10)
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute("SELECT *FROM menulist")
        self.menu=c.fetchall()
        print(self.menu)
        self.add_menu_tableWidget.setRowCount(len(self.menu))  # 행 개수
        self.add_menu_tableWidget.setColumnCount(3)  # 컬럼 개수
        for i in range(len(self.menu)):
            for j in range(3):
                self.add_menu_tableWidget.setItem(i, j, QTableWidgetItem(str(self.menu[i][j])))
        conn.close()

    def plus_menu(self): # 상품등록
        add_code=self.add_menucode_lineEdit.text() # 등록할 메뉴코드
        add_name=self.add_menuname_lineEdit.text() # 등록할 메뉴이름
        add_price=int(self.add_price_lineEdit.text()) # 등록할 메뉴가격
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute("SELECT *FROM menulist")
        first_data=c.fetchall()
        c.execute(f'''INSERT INTO menulist (메뉴코드, 메뉴명, 가격) VALUES ("{add_code}","{add_name}",{add_price})''');
        c.execute("SELECT *FROM menulist")
        self.show_menu=c.fetchall()
        self.add_menu_tableWidget.setRowCount(len(self.show_menu))  # 행 개수
        self.add_menu_tableWidget.setColumnCount(3)  # 컬럼 개수
        for i in range(len(self.show_menu)):
            for j in range(3):
                self.add_menu_tableWidget.setItem(i, j, QTableWidgetItem(str(self.show_menu[i][j]))) #테이블 위젯에 menulist 표시
        # if first_data != show_menu:
        #     self.login_stackedWidget.setCurrentIndex(8)
        conn.commit()
        conn.close()

        h1=Alarm_Menu(self)
        h1.start()

    def login_page(self):#로그인창으로
        self.login_stackedWidget.setCurrentIndex(0)

    def log_in(self): # 로그인창에서 로그인버튼 눌렀을때
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",
                               charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT id FROM user_info WHERE BINARY id='{self.id_lineEdit.text()}' and password='{self.password_lineEdit.text()}'");
        id_count=c.fetchall()
        c.execute(f"SELECT name FROM user_info WHERE BINARY id='{self.id_lineEdit.text()}'")
        # print(id_count[0][0])
        admin=c.fetchall()
        if id_count !=() and self.id_lineEdit.text()==id_count[0][0]:
            if admin[0][0]=="관리자":
                QMessageBox.about(self, "알림", "관리자 로그인")
                self.admin_signal=True
                self.login_stackedWidget.setCurrentIndex(5)
            else:
                QMessageBox.about(self, "알림", "로그인 성공")
                self.user_signal=True
                self.login_stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.about(self, "알림", "아이디나 비밀번호가 틀립니다")

    def log_out(self):# 로그아웃
        if self.user_signal==True:
            self.id_lineEdit.clear()
            self.password_lineEdit.clear()
            self.user_signal=False
            self.login_stackedWidget.setCurrentIndex(0)
        elif self.admin_signal==True:
            self.id_lineEdit.clear()
            self.password_lineEdit.clear()
            self.admin_signal=False
            self.login_stackedWidget.setCurrentIndex(0)

    def signup(self): # 회원가입창
        self.login_stackedWidget.setCurrentIndex(1)
        self.id_input_lineEdit.clear()
        self.password_input_lineEdit.clear()
        self.re_password_lineEdit.clear()
        self.name_lineEdit.clear()
        self.address_lineEdit.clear()

    def confirm_id(self): # 아이디 중복 확인
        conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT COUNT(id) from user_info WHERE id='{self.id_input_lineEdit.text()}'");
        id_compare=c.fetchall()
        print(id_compare)
        if id_compare[0][0] == 1:
            QMessageBox.about(self, "알림", "아이디 중복")
        else:
            if self.id_input_lineEdit.text() != "":
                QMessageBox.about(self, "알림", "사용가능한 아이디")
            else:
                QMessageBox.about(self, "알림", "아이디를 입력하세요")
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
                if self.sign_password == self.re_password: # 비밀번호, 비밀번호 확인 다를때
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

class Alarm_Menu(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent

    def run(self):# 쓰레드로 동작 시킬 함수
        print('된다')
        # conn = pymysql.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        # c = conn.cursor()
        while True:
            if self.parent.menu != self.parent.show_menu:
                self.parent.new_menu_label.setText('신메뉴 출시')
            else:
                pass
            time.sleep(0.5)
            # if self.parent.user_signal==False:
            #     break


if __name__=="__main__":
    app=QApplication(sys.argv)
    popup=Smart_App()
    popup.show()
    app.exec_()
