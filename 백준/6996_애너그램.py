n=int(input()) #개수
for _ in range(n):
    a,b=input().split(' ')
    #print(a,b)
    a_a=sorted(list(a))
    b_a=sorted(list(b))

    if a_a==b_a:
        print(a+' & '+b+' are anagrams.')
    else:
        print(a+' & '+b+' are NOT anagrams.')

    
