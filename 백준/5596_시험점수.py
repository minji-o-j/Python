mink=list(map(int,input().split()))
mans=list(map(int,input().split()))
mink_sum=sum(mink)
mans_sum=sum(mans)

if mans_sum>mink_sum:
    print(mans_sum)
else:
    print(mink_sum)
