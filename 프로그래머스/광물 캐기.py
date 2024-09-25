def solution(picks, minerals):
    """
    picks =  [dia, iron, stone] # 곡괭이의 개수
    minerals
    """
    rock_tired_list = []
    
    # 곡괭이로 광물을 끝까지 캘 수 있는 경우
    if sum(picks)*5 >= len(minerals):
        for n, i in enumerate(range(0,len(minerals),5)): # 5씩 잘라서 계산한다, n: index
            # 돌 피로도 계산
            rock_tired = 0
            for m in minerals[i:i+5]:
                if m == "diamond":
                    rock_tired += 25
                elif m == "iron":
                    rock_tired += 5
                else:
                    rock_tired += 1
            rock_tired_list.append((rock_tired, n))
        
    # 곡괭이로 광물을 끝까지 캘 수 없는 경우
    else:
        for n, i in enumerate(range(0,sum(picks)*5,5)): # 최대 캘 수 있는 곳까지, 5씩 잘라서 계산한다, n: index
            # 돌 피로도 계산
            rock_tired = 0
            for m in minerals[i:i+5]:
                if m == "diamond":
                    rock_tired += 25
                elif m == "iron":
                    rock_tired += 5
                else:
                    rock_tired += 1
            rock_tired_list.append((rock_tired, n))
        
    rock_tired_list.sort(reverse = True) # 순서대로 인덱스 활용하는 용도
    
    total_tired = 0
    r_idx = 0 # rock_tired_list_idx
    
    # 돌 피로도가 큰 순으로 다이아 -> 철 -> 돌 배분
    for d in range(picks[0]):
        try:
            r_idx_5 = rock_tired_list[r_idx][1]*5 
            total_tired += len(minerals[r_idx_5:r_idx_5+5])
            r_idx += 1
        except IndexError:  # 곡괭이 개수가 광물보다 많은경우
            pass

    
    for i in range(picks[1]):
        try:
            r_idx_5 = rock_tired_list[r_idx][1]*5 
            for m in minerals[r_idx_5:r_idx_5+5]:
                if m == "diamond":
                    total_tired += 5
                elif m == "iron":
                    total_tired += 1
                else:
                    total_tired += 1
            r_idx += 1
        except IndexError: 
            pass
        
    for s in range(picks[2]):
        try:
            r_idx_5 = rock_tired_list[r_idx][1]*5 
            for m in minerals[r_idx_5:r_idx_5+5]:
                if m == "diamond":
                    total_tired += 25
                elif m == "iron":
                    total_tired += 5
                else:
                    total_tired += 1
            r_idx += 1
        except IndexError: 
            pass
        
    return total_tired
