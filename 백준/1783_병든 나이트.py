n,m=map(int,input().split(' '))
if n<=2 and m<=2: #이동못함
    print (1)

elif n<=1: #이동못함
    print(1)
elif m<=1: #이동못함
    print(1)
    
elif n==2: #2가지 방법으로만 이동 가능
    if m<=8:
        print((m-1)//2+1)
    else:
        print(4)
    
elif m==2: #이동 1회 가능
    print(2)
    
elif m<=4:
    print(m)
    
elif 4<m<7:
    print(4)
    
    
else:# m>=7:
    print(m-2)
