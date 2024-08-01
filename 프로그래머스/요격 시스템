def solution(targets):
    # e가 큰순 -> s가 큰순 정렬
    targets.sort(key = lambda x:(x[1],x[0]))

    answer = 0
    last_s = 0
    last_e = 0
    
    for t_s, t_e in targets:
        if last_e <= t_s: # 다음 s가 더 클 때 (안겹치는 경우 포함)
            answer +=1
            last_e = t_e
            
    return answer
