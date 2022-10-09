strr = input("id를 입력하세요: ")
if strr.lower() == 'admin':
    print("Hi admin! please check log file first.")
else:
    print("welcome {}".format(strr))
