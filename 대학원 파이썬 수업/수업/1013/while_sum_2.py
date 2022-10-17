sum_ = 0
n = int(input("몇까지? "))
x=1
while x<=n:
    if x%2==0:
        sum_+=x
    x+=1

print("1부터 {}까지 짝수의 합: {}".format(n,sum_))
