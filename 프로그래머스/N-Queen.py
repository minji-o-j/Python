
    
def nqueen(check_nqueen, now_position): # check_nqeen: 지금까지 놓은 위치 // now_position: 내가 새로 놓으려는 위치
    for i in range(len(check_nqueen)):
        if now_position == check_nqueen[i] or (len(check_nqueen)-i)==abs(check_nqueen[i]-now_position):
            return False
    return True 

def dfs(n, check_nqueen):
    if len(check_nqueen)==n:
        return 1 #모두완료
    cnt = 0
    for i in range(n): 
        if nqueen(check_nqueen, i):
            cnt+=dfs(n, check_nqueen+[i])
    return cnt

def solution(n):
    return dfs(n, [])
    
    
    """ #11번 시간초과 코드
    answer = 0
    for i in range(n): # 0행이 0~n-1까지
        is_check = deque([[i]])
        while is_check:
            check_queenlist = is_check.popleft()
            if len(check_queenlist) == n:
                answer+=1
                continue
            for j in range(0, n): # 각 행마다 n번 반복 필요함 - j: 새롭게 검사하는 행의 열 번호
                flag = 0
                for e, k in enumerate(check_queenlist): # 여러개의 k에 대한 체크 필요함 - k: 이전 행에서 queen의 위치, e: 이전 행 중 몇번째 행인지에 대한 번호
                    # len(check_queenlist): 현재 몇 번째 행인지?
                    # 검사해야할 것 : j가 k와 동일하면 안됨(세로검사),  k+-len(check_queenlist-e) 이면 안됨(대각선 검사)
                    if j == k or j == k-(len(check_queenlist)-e) or j == k+(len(check_queenlist)-e) :
                        flag = 1
                        break
                if flag==0:
                    is_check.append(check_queenlist+[j])
            
    return answer
    """


    
