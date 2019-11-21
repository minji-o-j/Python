import random
a=random.randint(10,99)
b=int(input("복권번호를 입력하세요(10에서 99사이):"))
r1=a//10
r2=a%10
u1=b//10
u2=b%10
print("당첨번호는 %d입니다." %a)

if (a==b)or((r1==u2)and(r2==u1)):
    print("상금은 100만원입니다.")
    
elif ((r1==u1)or(r2==u1)or(r1==u2)or(r2==u2)):
    print("상금은 50만원입니다.")
    
else:
    print("상금은 0원입니다.")
