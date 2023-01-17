import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui
from datetime import datetime
import time


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


# UI
form_class = uic.loadUiType('./smartappg.ui')[0]


class Main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #기본 페이지 지정 (관리자 페이지)
        self.login_stackedWidget.setCurrentIndex(5)
        #상호작용 버튼
        self.see_order_btn.clicked.connect(self.move_order_manage)
        self.inventory_btn.clicked.connect(self.move_inventory)
        self.admin_page_btn_6.clicked.connect(self.move_admin_page)
        self.admin_page_btn_7.clicked.connect(self.move_admin_page)
        self.admin_page_btn_9.clicked.connect(self.move_admin_page)
        self.see_qna_btn.clicked.connect(self.see_qna_manage)
        self.renew_order_manage_btn.clicked.connect(self.renew_order_manage_list)
        self.see_not_receive_btn.clicked.connect(self.see_not_received_order) # 접수되지 않은 주문 확인하기
        self.order_status_change_btn.clicked.connect(self.order_status_change) # 주문 상태 변경 시켜줌 (주문,접수,완료)
        # qna창에서 주문번호가 있는 항목 선택하여 버튼 누르면 이동
        self.see_selected_order_btn.clicked.connect(self.see_selected_order)

        self.inventory_cb.currentIndexChanged.connect(self.calculate_min_item) # 최대 개수 계산
        self.ingredient_order_btn.clicked.connect(self.order_ingredient) #재고 발주
        self.ira = inventory_renew_alarm(self) # 재고 부족 알림 스레드 생성
        self.inventorySignal = True
        self.ira.start() #재고 부족 알림 스레드 시작

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
    def order_status_change(self):

        status = self.order_status_change_cb.currentText()
        if status == '선택 안함':
            return
        try :
            orderstatus = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 4).text()
        #행을 선택하지 않고 버튼 실행했을시 오류를 방지하기위해 Return해줌
        except :
            return
        if orderstatus == '완료':
            QMessageBox.critical(self, "완료 상품입니다", "완료상태에서는 변경할 수 없습니다.")
            return
        # 선택한 행의 가장 첫번쨰 값이 주문번호이므로 이걸 텍스트로 받아와서 SQL 쿼리문에 활용한다.
        ordernumber = self.order_tableWidget.item(self.order_tableWidget.currentRow(), 0).text()
        conn = p.connect(host='10.10.21.105', port=3306, user='wlgur', password='chlwlgur1234',
                         db='obokmoolsan', charset='utf8')
        c = conn.cursor()
        c.execute(f"update ordermanage set 상태 = '{status}' where 주문번호 = '{ordernumber}'")
        conn.commit()
        conn.close()
        if status == '완료':
            QMessageBox.information(self, "제작 완료", "재고에서 재료가 소모됩니다.")
            self.consume_inventory_item()  # 아직 실행안해봄 ㅎ.. 주문등록 테스트 기능 만들고 테스트 예정
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

    # 로그아웃
    def logout(self):
        self.Signal_login = False
        self.Stack_W_login.setCurrentIndex(0)
        self.logon_label.setText("")
        self.signal = False
        self.notification.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.setFixedHeight(600)
    mainWindow.setFixedWidth(600)
    mainWindow.show()
    app.exec_()
