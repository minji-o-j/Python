id = input("id: ")
if id.lower() == 'admin':
    pw = input('password: ')
    if pw == '1234':
        print("welcome admin")
    else:
        print('wrong pw')
else:
    print("you are not admin")
