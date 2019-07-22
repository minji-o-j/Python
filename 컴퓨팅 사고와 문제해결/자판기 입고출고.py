items = { "커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5 }


item = input("물건의 이름을 입력하시오: ");
print ('현재 '+str(items[item])+'개 있습니다.\n\n')
a=int(input("입고/출고:"))
items[item]=items[item]+a
print ('현재 '+str(items[item])+'개 있습니다.')
