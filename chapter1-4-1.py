### 리스트 : 순서가 있음
stock_list = ["삼성전자", "LG화학", "카카오", "원풍물산", "싸이토젠", "현대차"]
print("오늘 매수할 종목 %s" % stock_list)

# 매수할 종목 추가하기
stock_list.append("현대")
print("추가된 종목 %s" % stock_list)

# 종목 삭제하기
del stock_list[0]
print("인덱스 0번째 삭제: %s" % stock_list)

### dictionary : 순서가 없는 대신 키값
# 종목에 여러가지 데이터를 동시에 담기
stock_dict = {"현재가": 6000, "등락율": 2.42}
print("현재가와 등락율을 담은 딕셔너리: %s" % stock_dict)
print("현재가: %s, 등락율: %s" % (stock_dict["현재가"], stock_dict["등락율"]))

# 종목별로 데이터 담아주기
stock_dict = {"삼성전자": stock_dict}
print("삼성전자에 현재가와 등락율 담아 주기: %s" % stock_dict)

# 데이터 추가하기
stock_dict["삼성전자"]["거래량"] = 230000
print("거래량 데이터 추가: %s" % stock_dict)

# 데이터 삭제하기
del stock_dict["삼성전자"]["거래량"]
print("데이터 삭제 %s" % stock_dict)

### 튜플 :  속도 빠름, 추가 및 삭제 안됨 
stock_list = ("삼성전자", "LG화학", "카카오", "원풍물산", "싸이토젠", "현대차")
print(stock_list)
