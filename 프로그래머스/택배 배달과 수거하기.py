def solution(cap, n, deliveries, pickups):
    answer = 0
    can_d = 0
    can_p = 0
    """
    역순으로 배달 or 수거 탐색
    """
    
    for i in range(n-1, -1, -1):
        can_d += deliveries[i]
        can_p += pickups[i]
        
        while can_d >0 or can_p >0: # 가야함
            answer += 2*(i+1)
            can_d -= cap
            can_p -= cap
        
    return answer
