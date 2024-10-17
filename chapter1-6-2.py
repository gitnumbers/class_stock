### 클래스
class MyXingAPI:
    mesu_ok = False
    mesu_price = 2000

mesu = MyXingAPI.mesu_ok
price = MyXingAPI.mesu_price
print("1.테스트 매수여부: %s, 매수가격: %s" % (mesu, price))

# 객체화
myXingAPI = MyXingAPI()
mesu = myXingAPI.mesu_ok
price = myXingAPI.mesu_price
print("2.테스트 매수여부: %s, 매수가격: %s" % (mesu, price))

myXingAPI.mesu_ok = True
myXingAPI.mesu_price = 500000
mesu = myXingAPI.mesu_ok
price = myXingAPI.mesu_price
print("3.테스트 매수여부: %s, 매수가격: %s" % (mesu, price))

class MyXingAPI_2:
    mesu_ok = False

    # __init__ 클래스가 활성화되면 무조건 실행되는 초기함수
    def __init__(self):
        self.stock_name = None
        self.stock_price = 0

        stock_drate = 0.0 #등락율

        print("self에 담긴 데이터들 확인: %s" % dir(self))


test_stock_name = MyXingAPI_2().stock_name
print("class안에 del함수에 있는 변수에 접근 %s" % test_stock_name)

myXingAPI_2 = MyXingAPI_2()
test_stock_name_2 = myXingAPI_2.stock_name
print("class를 변수로 만들 때 뒤에 ()를 붙여주면 클래스 활성화된다 %s" % test_stock_name_2)

myXingAPI_2.stock_name = "삼성전자"
myXingAPI_2.stock_price = 90000
print("종목명: %s, 종목가격: %s" % (myXingAPI_2.stock_name, myXingAPI_2.stock_price))

class MyXingAPI_3:
    mesu_ok = False

    # __init__ 클래스가 활성화되면 무조건 실행되는 초기함수
    def __init__(self):
        self.stock_name = "삼성전자"
        self.stock_price = 5000

    # def mesu_check도 self변수에 담긴다
    def mesu_check(self, check_name=None, check_price=0):
        #print(def mesu_check 함수도 self 변수에 담긴다: %s" % dir(self))
        if self.stock_name == check_name:
            print("%s 종목 찾음" % check_name)
            if self.stock_price < check_price:
                print("지정한 가격 넘어서 매수시작: %s" % check_price)
                return True
            return False

myXingAPI_3 = MyXingAPI_3()

stock_dict = {"삼성전자":{"일시":20241014, "시가":51800, "고가":55000, "저가":51700, "종가":51000, "시가":51000},
              "LG화학":{"일시":20241014, "시가":399000, "고가":401500, "저가":380000, "종가":401000, "시가":401000},
              "카카오":{"일시":20241014, "시가":259500, "고가":359500, "저가":250500, "종가":259500, "시가":258500},
              "현대차":{"일시":20241014, "시가":106000, "고가":116000, "저가":105000, "종가":106000, "시가":108000}}

for name in stock_dict.keys():
    price = stock_dict[name]["종가"]

    result = myXingAPI_3.mesu_check(check_name=name, check_price=price)
    if result is True:
        print("%s 종목 매수 시작" % name)