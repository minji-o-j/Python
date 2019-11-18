## 변수 선언 부분
select, answer, numStr, num1, num2, a, b, ch,i, k, guguLine, dan1, dan2 = 0, 0, "", 0, 0, 0, 0, "", 0, 0, "", 0, 0

## 메인(main) 코드 부분
while True :
    select=int(input("\n1. 간단한 계산기  2. 수식 계산기  3. 두수 사이 합계 4. 구구단 출력기: "))

    if select == 1 :
        a=int(input("첫번째 수를 입력하세요 : "))
        ch=input("계산할 연산자를  입력하세요 : ")
        b=int(input("두번째 수를 입력하세요 : "))

        if ch == "+" :
            print(" %d + %d = %d 입니다. " % (a, b, a + b))
        elif ch == "-" :
            print(" %d - %d = %d 입니다. " % (a, b, a - b))
        elif ch == "*" :
            print(" %d * %d = %d 입니다. " % (a, b, a * b))
        elif ch == "/" :
            print(" %d / %d = %f 입니다. " % (a, b, a / b))    
        elif ch == "%" :
            print(" %d %% %d = %d 입니다. " % (a, b, a % b))
        elif ch == "//" :
            print(" %d // %d = %d 입니다. " % (a, b, a // b))
        elif ch == "**" :
            print(" %d ** %d = %d 입니다. " % (a, b, a ** b))    
        else :
            print(" 알 수 없는 연산자 입니다." ) 
    elif select == 2 :
        numStr=input(" *** 수식을 입력하세요  : ")
        answer = eval(numStr)
        print(" %s 결과는 %5.1f 입니다. " % (numStr, answer))
    elif select == 3 :
        num1=int(input(" *** 첫번째 숫자를 입력하세요  : "))
        num2=int(input(" *** 두번째 숫자를 입력하세요  : "))
        for i in range(num1, num2+1) :
            answer = answer + i
        print(" %d+...+%d는  %d입니다. " % (num1, num2, answer))
    elif select == 4 :
        dan1 = int(input("몇 단 부터?"))
        dan2 = int(input("몇 단 까지?"))

        for i in range(dan1, dan2+1) :
             guguLine = guguLine + ("   # %d단 #  " % i)

        print(guguLine)

        if dan2<10 :
            for i in range(2, 10) :
                guguLine=""
                for k in range(dan1, dan2+1) :
                    guguLine = guguLine + str("%4dX%2d=%4d" % (k, i, k*i))
                print(guguLine)

        else :
            for i in range(2, dan2+1) :
                guguLine=""
                for k in range(dan1, dan2+1) :
                    guguLine = guguLine + str("%4dX%2d=%4d" % (k, i, k*i))
                print(guguLine)


    else :
        print("1, 2, 3, 4중 하나만 입력해야 합니다.")

