n = int(input("enter n: "))

cnt = 1
sum_ = 0
while cnt<=n:
    input_num = int(input("enter number: "))
    sum_+=input_num
    cnt+=1

print("average is {:<0.2f}".format(sum_/n))
