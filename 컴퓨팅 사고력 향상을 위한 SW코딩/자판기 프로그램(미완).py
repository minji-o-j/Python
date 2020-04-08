##변수 선언 부분
start,money,drink,many=1000,0,0,0

##함수 정의 부분
def drink_machine(button):

    if button==1:
        print("당신은 캔커피 %d개를 주문하셨습니다." %many)
        if start+money>=800*many:
            print("캔커피 %d개를 판매하였습니다. 거스름돈은 %d원입니다. 판매를 종료합니다." %(many,((start+money)-(800*many))))
            print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %(((start+money)-(800*many))))
            start=((start+money)-(800*many))
            
        elif (start+money)-(800*many)<0:
            print("당신은 캔커피 %d개를 선택하셨습니다. 거스름돈이 부족하여 판매할 수 없습니다." %many)

    
    elif button==2:
        print("당신은 소다 %d개를 주문하셨습니다." %many)
        if start+money>=600*many:
            start=((start+money)-(600*many))
            print("소다 %d개를 판매하였습니다. 거스름돈은 %d원입니다. 판매를 종료합니다." %(many,((start+money)-(600*many))))
            print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %(((start+money)-(600*many))))

        elif (start+money)-(600*many)<0:
            print("당신은 소다 %d개를 선택하셨습니다. 거스름돈이 부족하여 판매할 수 없습니다." %many)
            

    
    elif button==3:
        print("당신은 생수 %d개를 주문하셨습니다." %many)
        if start+money>=500*many:
            start=((start+money)-(500*many))
            print("생수 %d개를 판매하였습니다. 거스름돈은 %d원입니다. 판매를 종료합니다." %(many,((start+money)-(500*many))))
            print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %(((start+money)-(500*many))))


        elif (start+money)-(500*many)<0:
            print("당신은 생수 %d개를 선택하셨습니다. 거스름돈이 부족하여 판매할 수 없습니다." %many)
    


##메인 코드 부분
print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %start)
while True:

    if start+money>=0:
        money=int(input("투입 금액을 입력하세요: "))
        drink=int(input("음료를 선택하세요: "))
        many=int(input("수량을 선택하세요: "))
        drink_machine(drink)

    elif (start+money)<0:
        print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %start)
        money=int(input("투입 금액을 입력하세요: "))
        drink=int(input("음료를 선택하세요: "))
        many=int(input("수량을 선택하세요: "))
