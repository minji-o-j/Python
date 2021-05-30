n=int(input())
numlist=list(map(int,input().split(' ')))
#print(numlist)
max_n=0
cnt_d=0
cnt_i=0
for i in range(1,len(numlist)):
    dd=numlist[i-1]>=numlist[i]
    if dd==0:#false
        cnt_d=0
    else: #true
        cnt_d+=1
        if max_n<cnt_d:
            max_n=cnt_d
            

    ii=numlist[i-1]<=numlist[i]
    if ii==0:#false
        cnt_i=0
        
    else: #true
        cnt_i+=1
        if max_n<cnt_i:
            max_n=cnt_i

print(max_n+1)

            
