def solution(temperature, t1, t2, a, b, onboard):
    """
    temperature: 실외 온도
    t1, t2: 쾌적한 실내 온도의 범위 (t1, t2포함)
    a: 희망온도, 실내온도 다를 때 전력 소비량
    b: 희망온도, 실내온도 같을 때 전력 소비량
    onboard: 승객이 탑승중인 시간
    """
    

    if temperature < t1: # 외부 온도가 더 낮을 경우
        temperature *= -1
        t1, t2 = -t2, -t1
                
    ob_len = len(onboard)
    
    dp = [[1e9]*100 for i in range(ob_len)]
    dp[0][temperature]=0
    
    for obt in range(1, ob_len):
        for t in range(t1, temperature+1):
            if onboard[obt] and not t1<=t<=t2: # 사람이 타있는데 온도범위가 아닐때
                continue
            # 시간과 온도별로 드는 최소 비용 계산    
            dp[obt][t] = min(dp[obt-1][t-1], dp[obt-1][t+1]+a, dp[obt-1][t]+b) 
        
        if not onboard[obt]:
            dp[obt][temperature] = min(dp[obt][temperature], dp[obt-1][temperature])
            
    answer = min(dp[-1])
    return answer
