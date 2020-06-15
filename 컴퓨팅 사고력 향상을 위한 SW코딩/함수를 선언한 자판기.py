##함수

def machine():
    start,money,drink,many=1000,0,0,0
    kind,much="",0
    print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %(((start+money)-(much*many))))
    if start+money>=0:
        money=int(input("투입 금액을 입력하세요: "))
        drink=int(input("음료를 선택하세요: "))
        many=int(input("수량을 선택하세요: "))

        if drink==1:
            kind=="캔커피"
            much==800
        elif drink==2:
            kind=="소다"
            much==600
        elif drink==3:
            kind=="생수"
            much==500
        
        print("당신은 %s %d개를 주문하셨습니다." %(kind,many))

        if start+money>=much*many:
            print("%s %d개를 판매하였습니다. 거스름돈은 %d원입니다. 판매를 종료합니다." %(kind,many,((start+money)-(much*many))))
            print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %(((start+money)-(much*many))))
            start=((start+money)-(much*many))
            
        elif (start+money)-(much*many)<0:
            print("당신은 %s %d개를 선택하셨습니다. 거스름돈이 부족하여 판매할 수 없습니다." %(kind,many))
            start+=money
            print("\n1.캔커피(800원) 2.소다(600원) 3.생수(500원) 4.현재 잔액(%d원)" %start)
            money=int(input("투입 금액을 입력하세요: "))
            drink=int(input("음료를 선택하세요: "))
            many=int(input("수량을 선택하세요: "))
        
        
    
##메인 코드 부분

while True:
    machine()
