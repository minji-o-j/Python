word = input('enter word: ')

len_word = len(word)
reverse = ""

while len_word>0:
    reverse += word[len_word-1]
    len_word-=1

print(reverse)
