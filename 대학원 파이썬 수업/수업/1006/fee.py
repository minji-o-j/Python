age = int(input("나이를 입력하세요: "))
fee = 0

if age>=65:
    fee = 8000
elif 20<=age<65:
    fee = 10000
elif 7<=age<20:
    fee=7000
elif age<7:
    fee = 0

print(fee)
