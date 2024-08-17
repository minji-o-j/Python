global answer
answer= []
def hanoi(n, start, sub, end):
    """
    start: 출발 기둥
    sub: 서브 기둥
    end: 종료 기둥
    n: 원판의 개수
    """
    if n==1:
        answer.append([start,end])
    else:
        hanoi (n-1, start, end, sub)   # n-1이동
        answer.append([start,end]) # n 이동
        hanoi (n-1, sub, start, end) # sub에 모여있던거를 end (n번째 원판 위)로 이동
        
def solution(n):
    hanoi(n,1,2,3)
    return answer
