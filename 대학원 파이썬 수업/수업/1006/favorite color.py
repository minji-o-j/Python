color = ("blue","green","purple")

input_c = input("what is ur favorite color?: ")

if input_c.lower() in color:
    print('yes {} is also my favorite color'.format(input_c.title()))
else:
    print("{} is not my favorite color".format(input_c.title()))
