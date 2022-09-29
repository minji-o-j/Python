x = 'I have a {} pen'
print(x.format('green'))

x = 'I have a {:10} pen'
print(x.format('green'))

x = 'I have a {:>10} pen'
print(x.format('green'))

x = 'I have a {:<10} pen'
print(x.format('green'))

x = 'I have a {:^10} pen'
print(x.format('green'))

x = 'I have a {:*<10} pen'
print(x.format('green'))

x = 'I have a {:@^10} pen'
print(x.format('green'))

x = 'I have a {:?>10} pen'
print(x.format('green'))

'''
I have a green pen
I have a green      pen
I have a      green pen
I have a green      pen
I have a   green    pen
I have a green***** pen
I have a @@green@@@ pen
I have a ?????green pen
'''
