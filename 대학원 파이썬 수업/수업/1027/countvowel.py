str_ = input('enter string: ')
cnt1 = 0
cnt2 = 0 # 모음
vowel = 'aieouAIEOU'
for i in str_:
    if i in vowel:
        cnt2 += 1

    else:
        cnt1 += 1

print(cnt1, cnt2)
