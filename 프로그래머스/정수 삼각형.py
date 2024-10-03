def solution(triangle):
    lt = len(triangle)
    dp = [[0 for i in range(lt)] for j in range(lt)]
    
    for i in range(lt): # 행
        if i==0: # 첫 값 저장용
            dp[0][0] = triangle[0][0]
            continue
        else:
            for j in range(i+1): # 열
                if j == 0:
                    dp[i][0] = dp[i-1][0] + triangle[i][0]
                else:
                    dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j]) # 위의 값 또는 위의 대각선 왼쪽 값

    answer = max(dp[-1])
    return answer
