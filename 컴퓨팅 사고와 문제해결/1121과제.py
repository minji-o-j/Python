def countLine(word, counter):
                if word in counter:
                        counter[word] = counter[word] + 1
                else:
                        counter[word] = 1




infile = open("C:\\Users\정민지\Desktop\　　\컴퓨팅사고와문제해결\proverbs.txt", "r")

my_dict = { } 
for line in infile:
    line = line.rstrip()
    word_list = line.split()

    for word in word_list:
        word=word.replace(".", "")
        countLine(word, my_dict)


print(my_dict)
for key in sorted(my_dict.keys()):
    print(key,my_dict[key])
infile.close()

