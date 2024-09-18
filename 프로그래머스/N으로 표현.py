def calc(num, N, cal_dict):
    op_result = set([])
    op_result.add(int(str(N)*num))
    # 1, num-1 // 2, num-2 // ... // num-1, 1까지
    for i in range(1, num):
        for c1 in cal_dict[i]:
            for c2 in cal_dict[num-i]:
                op_result.add(c1+c2)
                op_result.add(c1-c2)
                op_result.add(c1*c2)
                if c2 !=0:
                    op_result.add(c1//c2)
    return op_result
                
            
def solution(N, number): # N으로 number를 표현하기
    answer = -1
    
    if N==number:
        return 1
    
    cal_dict = {1:set([N])} 
    
    for i in range(2,9): # 8회까지만 계산함
        cal_dict[i] = calc(i, N, cal_dict) # 새로 선언
        if number in cal_dict[i]:
            return i
    return answer
