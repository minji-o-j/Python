def solution(n, tops):
    dp1 = [0] * n # 오른쪽 아래 세모 찬 경우
    dp2 = [0] * n # 오른쪽 아래 세모 안 찬 경우
    
    dp1[0] = 1
    dp2[0] = 2 + tops[0]
    
    for i in range(1, n):
        dp1[i] = (dp1[i-1] + dp2[i-1]) % 10007
        dp2[i] = (dp1[i-1] * (tops[i] + 1) + dp2[i-1] * (tops[i]+2)) % 10007
    
    #print(dp1, dp2)
    answer = (dp1[-1] + dp2[-1]) % 10007
    return answer
