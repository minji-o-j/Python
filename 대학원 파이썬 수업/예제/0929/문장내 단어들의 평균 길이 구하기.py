x = input('문장을 입력하세요: ')
split_x = x.split()
print(split_x)
n_word = len(split_x)

print('단어의 평균 길이는 {}개 입니다'.format(len(x.replace(' ',''))/n_word))
