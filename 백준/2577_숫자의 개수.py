a=int(input())
b=int(input())
c=int(input())
mul=str(a*b*c)

count=[0 for i in range(10)]
for j in mul:
    count[int(j)]+=1

#출력

for k in count:
    print(k)
