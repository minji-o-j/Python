# 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    sum_all = sum(queue1) + sum(queue2)
    sum_all_div2 = sum_all//2
    
    real_queue1 = deque(queue1)
    real_queue2 = deque(queue2)
    
    cnt = 0
    nowsum = sum(queue1)
    
    while len(real_queue1)>0 and len(real_queue2)>0:
        if cnt > max(len(queue1), len(queue2))*2+min(len(queue1), len(queue2)): #무한루프 제거용, 
            break
        
        if nowsum == sum_all_div2:
            return cnt
        
        elif (nowsum > sum_all_div2) : # queue1값이 더 큼
            n = real_queue1.popleft()
            nowsum -= n
            real_queue2.append(n)
            cnt+=1
            
        elif (nowsum < sum_all_div2) :
            n = real_queue2.popleft()
            nowsum += n
            real_queue1.append(n)
            cnt+=1

        else:
            break
            
    return -1
