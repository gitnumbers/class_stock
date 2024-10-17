# 제어문

if True:
    print(("True 통과"))

if False:
    print("False 통과")
else:
    print("통과")

stock_dict = {"삼성전자":{"일시":20241014, "시가":51800, "고가":55000, "저가":51700, "종가":51000, "시가":51000},
              "LG화학":{"일시":20241014, "시가":399000, "고가":401500, "저가":380000, "종가":401000, "시가":401000}}

if "카카오" in stock_dict.keys():
    print("카카오 종목 존재: %s" % stock_dict["카카오"])
    
elif "삼성전자" in stock_dict.keys():
    print("삼성전자 종목 존재: %s" % stock_dict["삼성전자"])
    
else:
    print("둘 다 존재 안함")

if 100000 > stock_dict["삼성전자"]["시가"] and 100000 <= stock_dict["LG화학"]["시가"]:
    print("매수 가능")

if 50000 > stock_dict["삼성전자"]["시가"] or 100000 <= stock_dict["LG화학"]["시가"]:
    print("매수 가능")
else:
    print("매수 불가능")


