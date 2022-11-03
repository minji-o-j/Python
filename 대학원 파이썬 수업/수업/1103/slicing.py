color = ['r','b','g','w','or','p']
color[2:5]=['g','y']
print(color)
color[1:5] = 'brown'
print(color)

color[1:5] = (100,77,50)
print(color)
color[4:6] = {1,2,3}
print(color)
color[1:5] = {'NY':'ny','CA':'ca'}
print(color)

#color[3:5]=100 # error

score = [8,9,10,11,12,13,14,15,16]
score[2:9:3] = [100,99,98]
print(score)
