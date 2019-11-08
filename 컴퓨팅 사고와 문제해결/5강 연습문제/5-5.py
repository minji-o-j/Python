import random
a=random.randint(1,100)
b=random.randint(1,100)

s=a-b
print(a,"-",b, end=' ')
user=int(input("= "))
if user==s:
    print("맞았습니다.")
else:
    print("답이 틀렸습니다.")
