yn = input("마음에  드는 옷을 찾았나요? 예.아니오 입력: ")
if yn == "예":
    print("축하")
    cost = int(input("가격?: "))
    if cost <= 100000:
        print("예산 내입니다")
    else:
        print("예산 초과입니다")
elif yn == "아니오":
    print("아쉽군요")
else:
    print("예/아니오로 입력하세요")
