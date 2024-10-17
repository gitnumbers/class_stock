### 함수 정의
def mesu_check():
    print("매수할지 정하는 함수")

# 함수는 괄호를 붙여야 활성화됨
mesu_check()

def mesu_check(price=0):
    print("현재 받은 가격: %s" % price)

mesu_check()
mesu_check(price=1000)

def mesu_check(stock_name=None, price=0):
    if price > 5000:
        print("매수 가능, 종목명: %s, 종목가격: %s" % (stock_name, price))

mesu_check(stock_name="삼성전자", price=9999)

def mesu_check(stock_name=None, price=0):
    if price > 3000:
        print("매수 불가, 종목명: %s, 종목가격: %s" % (stock_name, price))
    elif price < 100000:
        print("매수 가능, 종목명: %s, 종목가격: %s" % (stock_name, price))

mesu_check(stock_name="원풍물산", price=2000)
mesu_check(stock_name="카카오", price=10000)


def mesu_check(stock_name=None, price=0):
    if price > 3000:
        return 0
    elif price < 10000:
        return 1
    else:
        return 2

result = mesu_check(stock_name="원풍물산", price=2000)
print("매수 가능 여부: %s" % result)

stock_dict = {"삼성전자":{"일시":20241014, "시가":51800, "고가":55000, "저가":51700, "종가":51000, "시가":51000},
              "LG화학":{"일시":20241014, "시가":399000, "고가":401500, "저가":380000, "종가":401000, "시가":401000}}


def mesu_check(stock_name=None, price=0):
    if price > 3000:
        return True, stock_name, price
    else:
        return False, None, None

for name in stock_dict.keys():
    price = stock_dict[name]["종가"]

    mesu_go, mesu_name, mesu_price = mesu_check(stock_name=name, price=price)
    if mesu_go is True:
        print("매수하자: %s, 종목명: %s, 가격: %s" % (mesu_go, mesu_name, mesu_price))

