f = ['Garen','Teemo','Alice','Teemo','Rakan','Jinx','Alice','Teemo']
name = input('enter name: ')
idx = 0
flen = len(f)
cnt = 0
while idx < flen:
    if name == f[idx]:
        cnt += 1
    idx += 1

if cnt ==0:
    print('there no {} in friends list'.format(name))
else:
    print("there are {} {} in friends list.".format(cnt,name))
