# [PCCP 기출문제] 2번 / 석유 시추

from collections import deque

# 1 일 경우 거기서 시작하는 bfs 실행
def oil_bfs(start_x, start_y, graph, visited):
    # 탐색용
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    oil_queue = deque([(start_x, start_y)]) 
    
    count=1
    dy_set = set([start_y]) # 방문한 y set    
    while oil_queue:
        x, y = oil_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and (nx, ny) not in visited :
                if graph[nx][ny]==1:
                    oil_queue.append((nx, ny))
                    visited.add((nx, ny))
                    count+=1
                    dy_set.add(ny)

    return count, dy_set, visited


# 전체 땅을 훑는다
def check_ground(graph):
    # y 합 구할 배열 생성
    y_sum =  [0]*len(graph[0])
    visited = set([])
    
    for nx in range(len(graph)):
        for ny in range(len(graph[0])):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
            
                if graph[nx][ny]==1:
                    count,dy_set,visited = oil_bfs(nx, ny, graph, visited)
                    for yy in dy_set:
                        y_sum[yy] += count

    return max(y_sum)

def solution(land):
    answer = check_ground(land)
    return answer
