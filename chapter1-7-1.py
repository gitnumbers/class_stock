class MyAPI:
    def __init__(self, value_gubun, value_class):
        print("API")

        if value_gubun == "XAQuary":
            print("XAQuary 요청")
            value_class.receiveData(self)

    def XAQuary_fnc(self, name, value):
        stock_dict = {"삼성전자": {"일시": 20241014, "시가": 51800, "고가": 55000, "저가": 51700, "종가": 51000, "시가": 51000},
                      "LG화학": {"일시": 20241014, "시가": 399000, "고가": 401500, "저가": 380000, "종가": 401000, "시가": 401000},
                      "카카오": {"일시": 20241014, "시가": 259500, "고가": 359500, "저가": 250500, "종가": 259500, "시가": 258500},
                      "현대차": {"일시": 20241014, "시가": 106000, "고가": 116000, "저가": 105000, "종가": 106000, "시가": 108000}}

        result = stock_dict[name][value]
        return result

#데이터를 받을 구역
class TrHandler:
    def receiveData(self):
        print("수신 준비 완료")
        print(self)
        print(dir(self))
        date = self.XAQuary_fnc("삼성전자", "일시")
        print("요청해서 받아온 날짜: %s" % date)
        price = self.XAQuary_fnc("삼성전자", "시가")
        print("요청해서 받아온 시가: %s" % price)

#실행용 클래스
class Main:
    def __init__(self):
        print("프로그램 시작")

        MyAPI(value_gubun="XAQuary", value_class=TrHandler)

Main()

