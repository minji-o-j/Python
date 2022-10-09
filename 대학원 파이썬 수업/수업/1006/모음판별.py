strr = input("알파벳을 하나 입력하세요: ")

check = "aeiou"

if strr.lower() in check:
    print("{}는 모음".format(strr))
else:
    print("{}는 자음".format(strr))
