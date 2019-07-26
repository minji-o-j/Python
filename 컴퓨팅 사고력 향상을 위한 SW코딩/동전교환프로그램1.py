money=int(input("교환할 금액을 입력해 주세요 : "))

c5000=money/5000
money%=5000

c1000=money/1000
money%=1000

c500=money/500
money%=500

c100=money/100
money%=100

c50=money/50
money%=50

c10=money/10
money%=10

print("\n")
print("오천원짜리 : %d 개" % c5000)
print("천원짜리 : %d 개" % c1000)
print("오백원짜리 : %d 개" % c500)
print("백원짜리 : %d 개" % c100)
print("오십원짜리 : %d 개" % c50)
print("십원짜리 : %d 개" % c10)
print("바꾸지 못한 잔돈 : %d 원" % money)
