age = int(input("나이: "))

if age<8:
    print("8세 이상이어야 가능합니다")
elif age >=8:
    height = int(input("키를 입력하세요"))

    if height >=120:
        print("입장가능")
    elif height <120:
        print("키가 120이상이어야지 입장가능")
