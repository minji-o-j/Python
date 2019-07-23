#연습문제 2번

counters=[0,0,0,0,0,0]
import random
for i in range(60):
    value=random.randint(0,5)

    counters[value]=counters[value]+1
    
print('주사위가 1인 경우는 '+str(counters[0]))
print('주사위가 2인 경우는 '+str(counters[1]))
print('주사위가 3인 경우는 '+str(counters[2]))
print('주사위가 4인 경우는 '+str(counters[3]))
print('주사위가 5인 경우는 '+str(counters[4]))
print('주사위가 6인 경우는 '+str(counters[5]))

