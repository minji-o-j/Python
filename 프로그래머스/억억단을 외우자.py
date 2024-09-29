def solution(e, starts):
    # 약수 개수 = 억억단 등장 개수
    min_s = min(starts)
    d = [0 for i in range(e+1)] #약수 -- index e번 까지 저장
    for i in range(1, e+1): # 최소 s부터 e까지
        # 직접 약수가 되어서 개수를 센다
        if i*i <= e:
            d[i*i] += 1
        for j in range(i+1, e+1):
            ij = i*j
            if ij > e:
                break
            d[ij] += 2
            
    max_div_list = [0 for i in range(e+1)] # 특정 구간 내에 가장 많이 등장한 수 찾기
    max_div_list[-1] = e 
    
    for i in range(e-1, min_s-1, -1) :
        if d[max_div_list[i+1]] <= d[i] : # 현재 숫자의 약수 개수가 더 많은 경우
            max_div_list[i] = i
        else :
            max_div_list[i] = max_div_list[i+1]

    answer = [max_div_list[s] for s in starts]
    return answer
