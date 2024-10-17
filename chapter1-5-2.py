# 제어문
# for문은 여러가지 데이터를 순차적으로 다루게 해준다.

stock_list = ["태웅로직스", "코오롱글로벌", "제노포커스", "부산주공", "한국팩키지"]

for stock_name in stock_list:
    print("종목명: %s" % stock_name)


for stock_name in stock_list:
    print("브레이크 이후에 종목명: %s" % stock_name)
    break

stock_dict = {"삼성전자":{"일시":20241014, "시가":51800, "고가":55000, "저가":51700, "종가":51000, "시가":51000},
              "LG화학":{"일시":20241014, "시가":399000, "고가":401500, "저가":380000, "종가":401000, "시가":401000}}

for stock_name in stock_dict.keys():
    end = stock_dict[stock_name]["종가"]

    if 10000 < end:
        print("조건계산 통과, 종목명: %s, 종가: %s" % (stock_name, end))


for stock_name in stock_dict.keys():
    end = stock_dict[stock_name]["종가"]

    if 10000 < end:
        continue
    else:
        print("조건계산 통과안됨, 종목명: %s, 종가: %s" % (stock_name, end))




