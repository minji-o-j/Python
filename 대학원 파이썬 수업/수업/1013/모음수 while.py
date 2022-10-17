find = 'aieou'

word = input('enter word')

idx = 0
cnt = 0
while idx<len(word):
    if word[idx] in find:
        cnt += 1
    idx += 1

print(f"모음 수 {cnt}")
