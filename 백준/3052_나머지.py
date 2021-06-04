#배열에 10개 수 입력받음
numlist=[]
for i in range(10):
    numlist.append(int(input()))
    
#나머지를 set 배열에 저장
rlist=set([])
for j in range(10):
    rlist.add(numlist[j]%42)
#배열 출력
print(len(rlist))
