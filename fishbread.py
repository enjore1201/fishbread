
stock = {
    '팥붕어빵': 10,
    '슈크림붕어빵': 8,
    '초코붕어빵': 5
    }

sales = {
    '팥붕어빵': 0,
    '슈크림붕어빵': 0,
    '초코붕어빵': 0
}

def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코봉붕어빵) 똥는 '뒤로가기'입력 :")
        if bread_type == "뒤로가기":
            break
            #메뉴 주문+
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하새요"))
            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f'{bread_type}을 {bread_count}개 판매했습니다')
            else:
                print(f'재고가 부족합니다, 현재{stock[bread_type]}개만 주문가능합니다')
        else:
            print("팥붕어빵, 슈크림붕어빵, 초코봉붕어빵 중 하나의 맛을 선택해주세요")



#관리자 모드
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코봉붕어빵) 똥는 '종료'입력 :")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 개수를 입력하세요 : "))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다')
        else:
            print("올바른 메뉴 입력해주세요")

#붕어빵 가격이 필요합니다
price = {
    '팥붕어빵': 3000, #10갸
    '슈크림붕어빵': 1000, #5개
    '초코붕어빵': 1500, #6개
}

def calculate_sales():
    bread_sales = 0
    
    for key in sales:
        total_sales += (price[key] * sales[key])
    print(f'오늘의 총 메출은 {total_sales}원 입니다')

#메인 기능 선택
while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자, 종료) : ")
    if mode =="종료":
        print("시스템을 종료합니다")
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()

calculate_sales()