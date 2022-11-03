a = {'a','b','c'}
b = {'c','d','e'}

for i in a:
    for j in b:
        if i==j:
            print('we both like {}'.format(i))
