listt = ['hello','computer','chair','zero sugar','pepsi']
max_len = 0
max_word = ''
for w in listt:
    len_ = len(w)
    if max_len<len_:
        max_len = len_
        max_word = w

print('가장 긴 단어 {}'.format(max_word))
print('길이 {}'.format(max_len))
