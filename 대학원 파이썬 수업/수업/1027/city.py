city = ['DC','NY','Seoul', 'Tokyo','Paris']
print("what is the capital of S.Korea?")
for i in range(len(city)):
    print('{}. {}'.format(i+1,city[i]))

answer = int(input('choose an answer: '))
if answer == 3:
    print('correct')
else:
    print('incorrect')
          
