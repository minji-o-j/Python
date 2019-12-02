i, k, guguLine, dan1, dan2 = 0, 0, "", 0, 0

dan1 = int(input("몇 단 부터?"))
dan2 = int(input("몇 단 까지?"))

for i in range(dan1, dan2+1) :
     guguLine = guguLine + ("   # %d단 #  " % i)

print(guguLine)

if dan2<10 :
    for i in range(2, 10) :
        guguLine=""
        for k in range(dan1, dan2+1) :
            guguLine = guguLine + str("  %2dX%2d=%2d  " % (k, i, k*i))
        print(guguLine)

else :
    for i in range(2, dan2+1) :
        guguLine=""
        for k in range(dan1, dan2+1) :
            guguLine = guguLine + str("  %2dX%2d=%2d  " % (k, i, k*i))
        print(guguLine)

