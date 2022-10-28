a = int(input("a: "))
b = int(input("b: "))

starta = 0
startb = 0
while starta<a:
    while startb<b:
        print('@',end='')
        startb +=1
    startb = 0
    starta+=1
    print()
    
