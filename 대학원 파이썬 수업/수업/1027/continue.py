cnt = 0
while cnt<3:
    word = input("enter: ")
#    if word.isalnum():
#        print('word:{}'.format(word))
#        cnt+=1

    if not word.isalnum():
        continue
    print('word:{}'.format(word))
    cnt+=1
