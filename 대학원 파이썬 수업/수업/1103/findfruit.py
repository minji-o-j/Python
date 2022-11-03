L = ['apple','APPle','Melon','mElON','apPLE','kiwi','KiWI']
word = input('enter lowercase: ')

for i in range(len(L)):
    if L[i].lower() == word:
        print('{}--{}'.format(i,L[i]))
