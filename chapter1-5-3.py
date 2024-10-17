# 제어문
# while문은 여러가지 데이터를 순차적으로 다루게 해준다

while True:
    print("계속 돈다")
    break

stock_list = ["삼성전자", "LG화학", "카카오", "현대차"]

cnt = len(stock_list)
while cnt != 0:
    print(stock_list[cnt -1])
    cnt -= 1
