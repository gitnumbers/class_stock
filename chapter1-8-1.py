import time
import random
# from time import *

class MyObject:
    mesu_dict = {}

class MyAPI:
    def __init__(self, value_gubun, value_class):
        print("API")

        if value_gubun == "XAReal":
            print("XAQuary 요청")

            while True:
                time.sleep(0.5)
                value_class.receiveRealData(self)

    def XAReal_fnc(self):

        idx = random.randrange(0, 3)
        stock_names = ["삼성전자", "LG화학", "카카오", "현대차"]
        name = stock_names[idx]

        stock_dict = {"삼성전자": {"일시": 20241014, "시가": 51800, "고가": 55000, "저가": 51700, "종가": random.randrange(54000, 57000), "시가": 51000},
                      "LG화학": {"일시": 20241014, "시가": 399000, "고가": 401500, "저가": 380000, "종가": random.randrange(44000, 47000), "시가": 401000},
                      "카카오": {"일시": 20241014, "시가": 259500, "고가": 359500, "저가": 250500, "종가": random.randrange(24000, 27000), "시가": 258500},
                      "현대차": {"일시": 20241014, "시가": 106000, "고가": 116000, "저가": 105000, "종가": random.randrange(10000, 17000), "시가": 108000}}

        return name, stock_dict[name]["시가"], stock_dict[name]["종가"]


# 데이터를 받을 구역
class TrHandler:
    def receiveRealData(self):
        name, start, end = self.XAReal_fnc()
        
        drate = (end - start) / start * 100
        drate = round(drate,2)
        
        if drate > 5.0 and name not in MyObject.mesu_dict.keys():
            print("======= 매수하는 종목명: %s, 매수가격: %s, 등락율: %s" % (name, end, drate), flush=True) #다음 개행문자
            
            MyObject.mesu_dict[name] = {"매수가격": end}
        elif name in MyObject.mesu_dict.keys():
            mesu_price = MyObject.mesu_dict[name]["매수가격"]
            drate = (end - mesu_price) / mesu_price * 100
            drate = round(drate, 2)

            if drate >= 1.0 or drate <= -1.0:
                print("======= 매도하는 종목명: %s, 매도가격: %s, 매수가격대비등락율: %s" % (name, end, drate), flush=True)

                del MyObject.mesu_dict[name]

# 실행용 클래스
class Main:
    def __init__(self):
        print("프로그램 시작")

        MyAPI(value_gubun="XAReal", value_class=TrHandler)

Main()

