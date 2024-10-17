# 초깃값
샘플 = None

# 변수명 지정하기
종목명 = "삼성전자"
stock_name = "삼성전자"
stockName = "삼성전자"
print("종목명: %s" % stock_name)
print(type(stock_name))

stock_price = 56000
stock_rate = -0.72
mesu_ok = False
print("현재가: %s, 등락율: %s%%, 매수여부: %s" % (stock_name, stock_rate, mesu_ok))
print("현재가: %s, 등락율: %s%s, 매수여부: %s" % (stock_name, stock_rate, "%", mesu_ok))