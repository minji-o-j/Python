fn = input("enter first name: ")
ln = input("enter last name: ")
id_ = (fn[0]+ln).lower()
print("welcome, your id is... {}".format(id_))


print("="/*32)
print("다음 기준에 따라 pw를만드시오\n--8자리이상\n--알파벳과 숫자만 가능")
print("="/*32)

pw = input("input new pw: ")
if len(pw)>=8:
    if pw.isalnum():
        print('good pw')
    else:
        print("알파벳과 숫자만 가능합니다")
else:
    print("비밀번호가 짧습니다 8자리 이상 입력하세요")
