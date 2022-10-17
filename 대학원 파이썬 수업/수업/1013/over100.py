test = (1,2,4,215,12,4,2,12,21,111,35125,112)
idx = 0
cnt = 0
while idx < len(test):
    if test[idx]>=100:
        cnt += 1
    idx += 1

print('there are {} people over 100'.format(cnt))
