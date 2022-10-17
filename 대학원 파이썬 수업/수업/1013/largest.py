large = -99999999999999

cnt = 1

while cnt<=10:
    num = int(input("enter number {}: ".format(cnt)))
    if num > large:
        large = num
    cnt +=1

print('the largest value is {}'.format(large))
