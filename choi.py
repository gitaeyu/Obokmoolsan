import random
import sys
import time
import ast
import pymysql as p
import matplotlib
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtGui import QIntValidator # 큐인트
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("smartappg.ui")[0]
class Smart_App(QMainWindow, form_class):
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

        self.admin_page_btn_6.clicked.connect(self.move_admin_page)
        self.admin_page_btn_7.clicked.connect(self.move_admin_page)
        self.admin_page_btn_8.clicked.connect(self.move_admin_page)
        self.admin_page_btn_9.clicked.connect(self.move_admin_page)
        self.admin_page_btn_10.clicked.connect(self.move_admin_page)
        self.admin_page_btn_11.clicked.connect(self.move_admin_page)

        #테스트 페이지로
        self.Testpage_btn.clicked.connect(self.move_test_page)
        #사용자 주문하기
        self.order_btn.clicked.connect(self.user_order)
        # validator = QIntValidator(0,100,self) # 정수만 입력가능
        # self.count_lineEdit.setValidator(QIntValidator(1,100,self)) # 정수만 입력가능  그런데 범위를 지정 해줫는데 범위를 벗어난 3자리 정수도 입력이됨 ??????
        self.user_order_item_btn.clicked.connect(self.select_menu)
        # 콤보박스 선택 글자 바뀌면 최대개수 바뀜
        self.menu_comboBox.currentTextChanged.connect(self.change_num)

        # 자동 주문
        self.order_start_btn.clicked.connect(self.order_test)
        self.order_stop_btn.clicked.connect(self.auto_order_stop)
        # 그래프 관련
        self.sales_btn.clicked.connect(self.make_graph)
        self.netprofit_btn.clicked.connect(self.netsales_graph)



# #=================================기태======================================
        #기본 페이지 지정 (관리자 페이지)
        # self.login_stackedWidget.setCurrentIndex(5)
        #상호작용 버튼
        self.Testpage_btn.clicked.connect(self.move_test_page)
        self.admin_page_btn_11.clicked.connect(self.move_admin_page)
        self.see_order_btn.clicked.connect(self.move_order_manage)
        self.inventory_btn.clicked.connect(self.move_inventory)

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
        self.inventory_cb.currentIndexChanged.connect(self.calculate_min_item) # 최대 개수 계산
        self.ingredient_order_btn.clicked.connect(self.order_ingredient) #재고 발주
        #재고부족 알림 스레드
        self.ira = inventory_renew_alarm(self) # 재고 부족 알림 스레드 생성
        self.inventorySignal = True
        self.ira.start() #재고 부족 알림 스레드 시작

        #자동 주문상태 변경 스레드 기능
        self.order_status_start_btn.clicked.connect(self.auto_order_change_start)
        self.order_status_stop_btn.clicked.connect(self.auto_order_change_stop)
        self.aot = Auto_order_thread(self)
        #자동 문의 등록 스레드 기능
        self.qna_start_btn.clicked.connect(self.auto_qna_start)
        self.qna_stop_btn.clicked.connect(self.auto_qna_stop)
        self.aqt = Auto_qna_thread(self)
    def netsales_graph(self): # 순이익 막대그래프
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan", charset="utf8")
        c = conn.cursor()
        c.execute("SELECT *FROM balance_sheet")
        self.net_sales=c.fetchall()
        year_list=[]
        x_list=[]
        for i in self.net_sales:
            year_list.append(i[3])
        for j in self.net_sales:
            x_list.append(int(j[0]))
        x=np.arange(2)
        plt.bar(x,x_list)
        plt.xticks(x,year_list)
        plt.show()
    def make_graph(self): # 매출액 막대 그래프
        print('gogogo')
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan", charset="utf8")
        c = conn.cursor()
        c.execute("SELECT *FROM balance_sheet")
        self.sales = c.fetchall()
        print(self.sales)
        year_list=[]
        x_list=[]
        for i in self.sales:
            year_list.append(i[3])
        for j in self.sales:
            x_list.append(int(j[0]))
        x=np.arange(2)
        plt.bar(x,x_list)
        plt.xticks(x,year_list)
        plt.show()

    def auto_qna_start(self):
        self.Auto_qna_Signal = True
        self.aqt.start()
        self.qna_start_btn.setDisabled(True)
    def auto_qna_stop(self):
        self.Auto_qna_Signal = False
        self.aqt.stop()
        self.qna_start_btn.setEnabled(True)

    def auto_qna_register(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute("select * from ordermanage order by rand() limit 1;")
        a = c.fetchall()
        ordernumber = a[0][0]
        menuname = a[0][1]
        orderid = a[0][2]
        menucode = a[0][6]
        c.execute(f"insert into inquiry_manage (주문번호,제품명,제품코드,상태,회원ID,문의내용,답장내용)\
                    values ('{ordernumber}','{menuname}','{menucode}','접수','{orderid}','Test','Test')")
        conn.commit()
        conn.close()

    def auto_order_change_start(self):
        self.Auto_order_Signal = True
        self.aot.start()
        self.order_status_start_btn.setDisabled(True)
    def auto_order_change_stop(self):
        self.Auto_order_Signal = False
        self.aot.stop()
        self.order_status_start_btn.setEnabled(True)

#====================================기태====================================================
    def move_test_page(self):
        self.login_stackedWidget.setCurrentIndex(11)

    # 재고 부족시 버튼 누를시 부족한 물품 자동발주
    def order_ingredient(self):

        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"select * from (select 요리,min(a.남은수량/b.수량) as 최대개수 \
                    from inventory a inner join bom b on a.재료코드 = b.재료코드 group by 요리) as temp\
                      order by 최대개수 limit 1")
        tempitem = c.fetchall()
        print(tempitem[0][0])
        # 프로시져 호출하여 최대개수가 1개 이하라면 부족한 물품을 채워줌. SQL 참조 바람.
        c.execute(f"call check_inventory('{tempitem[0][0]}')")
        conn.commit()
        conn.close()

    # 각각 Item별 생산가능 최대개수 계산
    def calculate_min_item(self):
        item = self.inventory_cb.currentText() #콤보박스 아이템의 텍스트를 가져옴 (쿼리문에 쓰기위함)
        #처음 페이지로 이동시에 간장게장이지만 add_item을 통해 콤보박스 물품이 정해져서 임의로 정해둠
        if item == '':
            item = '간장게장'

        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        # 각 요리별로 최대 개수 계산 쿼리문  (어쩔수 없이 이중쿼리문을 사용하게 됬다.)
        c.execute(f"select min(c.d) from (select (a.남은수량 / b.수량)as d \
                    from inventory a inner join bom b on a.재료코드 = b.재료코드 where 요리 = '{item}') as c;")
        minvalue = c.fetchone()
        #bom이 등록되지 않은 상황을 대비하기 위해 만든 조건문
        if minvalue == None:
            return
        self.inventory_min_value_lbl.setText(f'{int(minvalue[0])} 개')

    # 주문 완료시 재고 소모 메서드
    def consume_inventory_item(self):
        # 현재 선택한 항목의 요리이름을 쿼리문에 사용하기 위하여 가져옴.
        orderitem = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 1).text()
        orderqty = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 3).text()
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        # 재료 소모 쿼리문
        c.execute(f"update inventory as a inner join bom as b on a.재료코드 = b.재료코드 \
                    set a.남은수량 = (a.남은수량 - (b.수량 * {orderqty}))  where b.요리 = '{orderitem}'")
        conn.commit()
        conn.close()

    # 문의관리에서 선택한 주문을 주문관리페이지에서 보게해주는 메서드
    def see_selected_order(self):
        try:
            #현재 선택한 행의 두번째 항목의 텍스트를 ordernumber로 받는다
            ordernumber = self.qna_tableWidget.item(self.qna_tableWidget.currentRow(), 1).text()
        except:
            return
        if ordernumber == '':
            QMessageBox.critical(self, "주문 정보 없음", "주문정보가 없습니다.")
            return
        self.login_stackedWidget.setCurrentIndex(6)
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM ORDERMANAGE where 주문번호 = '{ordernumber}'")
        order_manage_list = c.fetchall()
        conn.close()
        self.order_tableWidget.clearContents()
        self.order_tableWidget.setRowCount(len(order_manage_list))
        self.order_tableWidget.setColumnCount(len(order_manage_list[0]))
        for j in range(len(order_manage_list)):
            for k in range(len(order_manage_list[j])):
                self.order_tableWidget.setItem(j, k, QTableWidgetItem(str(order_manage_list[j][k])))
        for i in range(len(order_manage_list[0])):
            self.order_tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    #문의관리 항목들을 보여주는 메서드
    def renew_qna_manage_list(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM inquiry_manage")
        qna_manage_list = c.fetchall()
        conn.close()
        self.qna_tableWidget.clearContents()
        self.qna_tableWidget.setRowCount(len(qna_manage_list))
        self.qna_tableWidget.setColumnCount(len(qna_manage_list[0]))
        for j in range(len(qna_manage_list)):
            for k in range(len(qna_manage_list[j])):
                self.qna_tableWidget.setItem(j, k, QTableWidgetItem(str(qna_manage_list[j][k])))
        for i in range(len(qna_manage_list[0])):
            self.qna_tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    #문의관리 페이지로 이동하는 메서드
    def see_qna_manage(self):
        self.login_stackedWidget.setCurrentIndex(7)
        self.renew_qna_manage_list()

    #주문 상태를 변경해주는 메서드
    #주문 상태를 변경해주는 메서드
    def order_status_change(self):
        status = self.order_status_change_cb.currentText()
        if status == '선택 안함':
            return
        try :
            orderstatus = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 4).text()
            orderqty = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 3).text()
            orderitem = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 1).text()
        #행을 선택하지 않고 버튼 실행했을시 오류를 방지하기위해 Return해줌
        except :
            return
        if orderstatus == '완료':
            QMessageBox.critical(self, "완료 상품입니다", "완료상태에서는 변경할 수 없습니다.")
            return
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        # 수량이 물품의 제작가능한 최대 개수보다 많으면 return 해버린다 2023.01.18 1225 초안
        c.execute(f"select min(c.d) from (select (a.남은수량 / b.수량)as d \
                    from inventory a inner join bom b on a.재료코드 = b.재료코드 where 요리 = '{orderitem}') as c")
        max_value = c.fetchall()
        print(max_value)
        if int(orderqty) > int(max_value[0][0]):
            QMessageBox.critical(self, "재고 부족", "재고를 주문해주세요.")
            return
        # 선택한 행의 가장 첫번쨰 값이 주문번호이므로 이걸 텍스트로 받아와서 SQL 쿼리문에 활용한다.
        ordernumber = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 0).text()
        c.execute(f"update ordermanage set 상태 = '{status}' where 주문번호 = '{ordernumber}'")
        conn.commit()
        conn.close()
        if status == '완료':
            QMessageBox.information(self, "제작 완료", "재고에서 재료가 소모됩니다.")
            self.consume_inventory_item()
        self.renew_order_manage_list()

    #접수되지 않은 주문리스트를 보는 메서드
    def see_not_received_order(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM ORDERMANAGE where 상태 = '주문'")
        order_manage_list = c.fetchall()
        conn.close()
        self.order_tableWidget.clearContents()
        self.order_tableWidget.setRowCount(len(order_manage_list))
        self.order_tableWidget.setColumnCount(len(order_manage_list[0]))
        for j in range(len(order_manage_list)):
            for k in range(len(order_manage_list[j])):
                self.order_tableWidget.setItem(j, k, QTableWidgetItem(str(order_manage_list[j][k])))
        for i in range(len(order_manage_list[0])):
            self.order_tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # 관리자 페이지로 이동하는 메서드 #스레드가 다시 시작된다.
    def move_admin_page(self):
        self.login_stackedWidget.setCurrentIndex(5)
        self.inventorySignal = True
        self.ira.start()

    # 주문관리 리스트를 갱신해주는 메서드
    def renew_order_manage_list(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM ORDERMANAGE")
        order_manage_list = c.fetchall()
        conn.close()
        self.order_tableWidget.clearContents()
        self.order_tableWidget.setRowCount(len(order_manage_list))
        self.order_tableWidget.setColumnCount(len(order_manage_list[0]))
        for j in range(len(order_manage_list)):
            for k in range(len(order_manage_list[j])):
                self.order_tableWidget.setItem(j, k, QTableWidgetItem(str(order_manage_list[j][k])))
        for i in range(len(order_manage_list[0])):
            self.order_tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    #재고관리 페이지로 이동하는 메서드 # 잠시동안 재고 부족 알림 스레드가 중단된다.
    def move_inventory(self):
        self.inventorySignal = False
        self.ira.stop()
        self.login_stackedWidget.setCurrentIndex(9)
        self.renew_inventory_list()
        #현재 등록된 상품 리스트에 따라 콤보박스 아이템들이 결정된다.
        self.inventory_cb.clear()
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM menulist")
        menu_list = c.fetchall()
        for i in menu_list:
            self.inventory_cb.addItem(i[1])
    # 재고 갱신 메서드
    def renew_inventory_list(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"SELECT * FROM inventory")
        inventory_list = c.fetchall()
        conn.close()
        self.inventory_tableWidget.clearContents()
        self.inventory_tableWidget.setRowCount(len(inventory_list))
        self.inventory_tableWidget.setColumnCount(len(inventory_list[0]))
        for j in range(len(inventory_list)):
            for k in range(len(inventory_list[j])):
                self.inventory_tableWidget.setItem(j, k, QTableWidgetItem(str(inventory_list[j][k])))
        for i in range(len(inventory_list[0])):
            self.inventory_tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # 주문관리 페이지로 이동 메서드
    def move_order_manage(self):
        self.login_stackedWidget.setCurrentIndex(6)
        self.renew_order_manage_list()
##==========================================기태 ====================================================
##====================================지혁==========================================================
    def user_order(self):# 주문하기 버튼 눌럿을때
        self.traffic_signal=0
        self.login_stackedWidget.setCurrentIndex(3)
        # validator=QIntValidator(self)
        # self.count_lineEdit.setValidator(validator) # QlineEdit에 숫자만 입력
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan", charset="utf8")
        c = conn.cursor()
        self.menu_comboBox.clear()
        c.execute(f"SELECT 메뉴명 FROM menulist")
        menu_list=c.fetchall()
        for i in menu_list:
            self.menu_comboBox.addItem(i[0])

        c.execute("SELECT A.메뉴코드, A.재료이름, A.수량, A.재료이름, A.재료코드, B.재료코드, B.재료이름, B.남은수량 FROM bom A INNER JOIN inventory B ON A.재료코드 = B.재료코드");
        # c.execute("CREATE VIEW OBOKMOOLSAN.MAX_MENU AS SELECT A.메뉴코드, A.재료이름, A.수량, A.재료코드, B.남은수량, B.남은수량/A.수량 AS 최대개수 FROM bom A INNER JOIN inventory B ON A.재료코드 = B.재료코드");
        c.execute("SELECT *FROM MAX_MENU");
        max_num = c.fetchall()
        print(max_num)
        c.execute(f"SELECT 메뉴코드 FROM menulist WHERE 메뉴명 = '{self.menu_comboBox.currentText()}'")
        find_code = c.fetchall()
        print(find_code,'gdgddg')
        c.execute(f"SELECT MIN(최대개수) FROM max_menu WHERE 메뉴코드='{find_code[0][0]}'");
        self.max_order = c.fetchone()
        print(self.max_order[0])
        # self.count_lineEdit.setValidator(QIntValidator(1,int(max_order[0]),self))  # 정수만 입력가능  그런데 범위를 지정 해줫는데 범위를 벗어난 3자리 정수도 입력이됨 ??????
        for i in range(1, int(self.max_order[0])+1):
            self.maxmenu_comboBox.addItem(str(i))

        # max_order=c.fetchone()
        # print(max_order)
        conn.close()
        # item_count = self.menu_comboBox.count()
        # print(item_count)
        # self.item_list=[]
        # for i in range(item_count):
        #     a=self.menu_comboBox.itemText(i)
        #     self.item_list.append(a)
        # print(self.item_list)

    #
    def change_num(self): #  메뉴 선택에 따라서 최대 선택 개수 다르게
        self.maxmenu_comboBox.clear()
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan", charset="utf8")
        c = conn.cursor()
        c.execute(f"SELECT 메뉴코드 FROM menulist WHERE 메뉴명 = '{self.menu_comboBox.currentText()}'")
        find_code2 = c.fetchall()
        print(find_code2)
        c.execute("SELECT *FROM ordermanage");
        self.compare_order1=c.fetchall()
        if find_code2 == ():
            pass
        else:
            c.execute(f"SELECT MIN(최대개수) FROM max_menu WHERE 메뉴코드='{find_code2[0][0]}'");
            max_order2 = c.fetchone()
            print(max_order2)
            for i in range(1, int(max_order2[0])+1):
                self.maxmenu_comboBox.addItem(str(i))
        conn.close()





    def select_menu(self): # 고객 주문내용 db에 추가
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan", charset="utf8")
        c = conn.cursor()

        print(self.compare_order1,'비교1')
        c.execute("SELECT DATE_FORMAT(now(), '%Y-%m-%d')");
        order_date=c.fetchall()
        c.execute(f"SELECT 메뉴코드 FROM menulist WHERE 메뉴명 = '{self.menu_comboBox.currentText()}'");
        self.input_code=c.fetchall()
        c.execute(f"INSERT INTO ordermanage (메뉴명, 주문ID, 수량, 상태, 취소여부, 메뉴코드, 날짜) VALUES ('{self.menu_comboBox.currentText()}','{self.id_lineEdit.text()}',"
                  f"'{self.maxmenu_comboBox.currentText()}', '주문', 'N', '{self.input_code[0][0]}','{order_date[0][0]}')");
        c.execute("SELECT *FROM ordermanage");
        self.compare_order2=c.fetchall()
        print(self.compare_order2,'비교2')
        conn.commit()
        conn.close()
        self.traffic_signal = 1
        h2=Alarm_Order(self)
        h2.start()
    def order_test(self):
        self.user_order_signal = True
        self.auto_order_starting=Auto_Order(self)
        self.auto_order_starting.start()
    def auto_order_stop(self):
        self.user_order_signal = False
        self.auto_order_starting.stop()

    def bom_page(self): # bom으로 이동
        self.add_code_comboBox.clear()
        self.login_stackedWidget.setCurrentIndex(8)
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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

    def user_page(self):
        self.login_stackedWidget.setCurrentIndex(2)
    def menu_add(self): # 상품등록 페이지로
        self.login_stackedWidget.setCurrentIndex(10)
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",
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
                self.user_order_signal = True
            else:
                QMessageBox.about(self, "알림", "로그인 성공")
                self.user_signal=True
                self.login_stackedWidget.setCurrentIndex(2)
                self.user_order_signal = True
        else:
            QMessageBox.about(self, "알림", "아이디나 비밀번호가 틀립니다")


    def log_out(self):# 로그아웃
        if self.user_signal==True:
            self.id_lineEdit.clear()
            self.password_lineEdit.clear()
            self.user_signal=False
            self.traffic_signal = 0  # 주문 알림  시그널
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
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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
        conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
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
        # conn = p.connect(host="10.10.21.105", user="wlgur", password="chlwlgur1234", db="obokmoolsan",charset="utf8")
        # c = conn.cursor()
        while True:
            if self.parent.menu != self.parent.show_menu:
                self.parent.new_menu_label.setText('신메뉴 출시')
            else:
                pass
            time.sleep(0.5)
            # if self.parent.user_signal==False:
            #     break
#####=======================================지혁=============================================

#====================기태 스레드=================================================
# 인벤토리 갱신 스레드
class inventory_renew_alarm(QThread):
    # 매개변수로 스레드가 선언되는 클래스에서 inventory_renew_alarm(self)라고 하여 상위 클래스를 부모로 지정
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        #inventorySignal이라는 bool 변수를 주어 True일때만 스레드가 계속해서 돌게 한다.
        while self.parent.inventorySignal:
            #DB 연결
            conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                             db='obokmoolsan', charset='utf8')
            c = conn.cursor()
            # 현재 있는 재료 중에서 가장 적게 만들어지는 메뉴의 이름과 개수를 찾기 위한 쿼리문
            c.execute(f"select * from (select 요리,min(a.남은수량/b.수량) as 최대개수 \
                        from inventory a inner join bom b on a.재료코드 = b.재료코드 group by 요리) as temp\
                          order by 최대개수 limit 1")
            #예시 min_value = ((해물찜,5.0),)
            min_value = c.fetchall()
            conn.commit()
            conn.close()
            time.sleep(0.5)
            # 만들어질수 있는 최대 개수가 1 이하라면 알람 생성
            if int(min_value[0][1]) < 1:
                self.parent.inventory_alarm_level_lbl.setText(f'{min_value[0][0]}의 재료가 부족합니다')
                self.parent.inventory_alarm_lbl.setText(f'{min_value[0][0]}의 재료가 부족합니다')
            else:
                self.parent.inventory_alarm_level_lbl.setText('')
                self.parent.inventory_alarm_lbl.setText(f'재고는 충분합니다')
            time.sleep(2)
    #스레드의 정지를 위한 메서드
    def stop(self):
        self.quit()
        self.wait(100)  # 5000ms = 5s


class Alarm_Order(QThread):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent

    def run(self):
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                          db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute("SELECT *FROM ordermanage");
        compare_order3=c.fetchall()
        conn.close()
        while True:
            print('쓰레드 알림창')
            if self.parent.compare_order1 != compare_order3:
                print("비교하기")
                self.parent.order_alarm_lbl.setText('주문도착')
                print('상태변경')
                time.sleep(10)




class Auto_order_thread(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        while self.parent.Auto_order_Signal:
            # DB 연결
            conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                             db='obokmoolsan', charset='utf8')
            c = conn.cursor()
            # Auto_order 프로시저 콜링
            c.execute(f"call Auto_order()")
            conn.commit()
            conn.close()
            print('Auto_order 스레드 작동중')
            self.parent.renew_order_manage_list()
            time.sleep(20)

    # 스레드의 정지를 위한 메서드
    def stop(self):
        print('Auto_order 스레드 정지')
        self.quit()
        self.wait(100)  # 5000ms = 5s


class Auto_Order(QThread): # 자동 주문 쓰레드
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent

    def run(self):
        while self.parent.user_order_signal:
            conn=p.connect(host='10.10.21.105', user='wlgur', password='chlwlgur1234', db='obokmoolsan', charset='utf8')
            c=conn.cursor()
            c.execute("SELECT DATE_FORMAT(now(), '%Y-%m-%d')"); #현재 날짜
            order_date2 = c.fetchall()
            print(order_date2)
            c.execute("SELECT 메뉴명 FROM menulist")
            auto_menu=c.fetchall()
            print(auto_menu,'히히')
            # print(auto_menu[0],'히히')
            choice_menu=random.choice(auto_menu) # 랜덤 선택 메뉴
            print(choice_menu[0],'호호')
            c.execute(f"SELECT 메뉴코드 FROM menulist WHERE 메뉴명 = '{choice_menu[0]}'");
            choice_code=c.fetchall()
            print(choice_code,'zz')
            c.execute(f"SELECT MIN(최대개수) FROM max_menu WHERE 메뉴코드 = '{choice_code[0][0]}'");
            num=c.fetchone()
            choice_num=random.randrange(1,int(num[0])+1)  # 랜덤 선택 개수
            print(choice_num,'gogo')
            c.execute(
                f"INSERT INTO ordermanage (메뉴명, 주문ID, 수량, 상태, 취소여부, 메뉴코드, 날짜) VALUES ('{choice_menu[0]}','{self.parent.id_lineEdit.text()}'\
                ,'{choice_num}', '주문', 'N', '{choice_code[0][0]}', '{order_date2[0][0]}')");
            conn.commit()
            conn.close()
            time.sleep(20)

    def stop(self):
        self.quit()
        self.wait(100)  # 5000ms = 5s

class Auto_qna_thread(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    def run(self):
        while self.parent.Auto_qna_Signal:
            self.parent.auto_qna_register()
            self.parent.renew_qna_manage_list()
            print('문의가 등록 되었습니다')

if __name__=="__main__":
    app=QApplication(sys.argv)
    popup=Smart_App()
    popup.show()
    app.exec_()
