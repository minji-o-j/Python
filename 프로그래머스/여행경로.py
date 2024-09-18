def solution(tickets):
    # 티켓 dict에 저장
    ticket_dict = dict([])
    for t in tickets:
        try:
            ticket_dict[t[0]].append(t[1])
            ticket_dict[t[0]].sort(reverse=True) # 역정렬 => pop할때 알파벳순으로 하기 위함
        except:
            ticket_dict[t[0]] = [t[1]]
    
    
    stack = ["ICN"] # dfs로 해야지 안되는 경우 이전 분기로 이동 가능하다 (오일러 경로)
    route = [] # 가장 먼저 완료된(탐색이 끝나서 더이상 갈 수 없는) 지점부터 기
    while stack: 
        goto = stack[-1]# 다음 목적지
        if goto not in ticket_dict  : # key가 없으면 (이동불가)
            route.append(stack.pop())
            
        elif len(ticket_dict[goto])==0: # pop불가 (길이0)
            route.append(stack.pop())
            
        else: # 이동 가능
            stack.append(ticket_dict[goto].pop()) # 이동 경로에 추가            

    return route[::-1]
