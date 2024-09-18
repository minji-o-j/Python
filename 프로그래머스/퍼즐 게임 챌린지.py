def solution(diffs, times, limit):
    min_ = 1
    max_ = 1000000
    min_check = 1000000
    
    last_save = -1 # (무한루프 방지용)
    
    while min_ < max_:
        level = (min_+max_)//2
        
        if last_save == level:
            break
        last_save = level    
        
        # 계산
        cal_time = 0
        for i, diff in enumerate(diffs):
            if diff<=level:
                cal_time += times[i]
            else:
                err = diff - level
                cal_time += (times[i-1] + times[i])*err + times[i]
        
        if limit < cal_time: # 시간초과, level이 늘어야함
            min_ = level
            
        else: # 성공했음, 최솟값 저장
            if level < min_check:
                min_check = level
            max_ = level

    return min_check
