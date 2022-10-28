string = input("enter string: ")
new_string = ''
for s in string:
    if s.islower():
        new_string += s.upper()
    else:
        new_string += s.lower()

print(new_string)
