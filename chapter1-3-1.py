add = 5000 + 3000
print("총 매입금액: %s" % add)

# 예수금이 10만원이 있다. LG상사 14800원에 매수할 수 있는 수량은?
account = 100000
price = 14800
quantity_1 = account / price # 1000 / 10 = 100.0
quantity_2 = account // price # 1000 / 10 = 100
print("예수금: %s, 현재가: %s, 수량1: %s, 수량2: %s" % (account, price, quantity_1, quantity_2))

leave = account % price
print("남은 예수금: %s" % leave)
