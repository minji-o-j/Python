def solution(scores):
    wan1, wan2 = scores[0]
    wan_sum = sum(scores[0])
    scores.sort(key = lambda x:(-x[0], x[1]))
    
    min_s2 = 0
    answer = 1 # 등수
    
    for s1, s2 in scores:
        if wan1 < s1 and wan2 < s2:
            return -1
        # s2의 최소
        if s2 < min_s2:
            continue  # 제외
        else:
            min_s2 = s2 # 최솟값 update
            if wan_sum < s1+s2:
                answer +=1 # 순위 뒤로 밀림
            
    return answer
