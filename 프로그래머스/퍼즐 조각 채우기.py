from collections import deque
def count_bfs(n, board):
    """
    n: 어떤 숫자를 찾아 셀것인가? 0 or 1
    board: 격자판
    """
    b_len = len(board)
    visited = [[0 for _ in range(b_len)] for _ in range(b_len)]
    return_list = [] 
    
    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]
    
    for i in range(b_len):
        for j in range(b_len):
            if board[i][j] == n and visited[i][j] == 0: 
                queue = deque([(i,j)])
                board[i][j] = n^1 # nor
                visited[i][j] = 1
                block_list = [(i,j)] # 하나의 블록 좌표

                while queue: # 하나의 블록 탐색
                    x,y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) or visited[nx][ny] == 1:
                            continue
                        elif board[nx][ny] == n: # 연결된 블록
                            queue.append((nx, ny))
                            board[nx][ny] == n^1
                            visited[nx][ny] = 1
                            block_list.append((nx, ny))
                            
                return_list.append(block_list) # 블록 한개
    return return_list

def make_block(table): # 정사각형 배열로 만들어줌
    blocks = []
    for block in table:
        xlist = []
        ylist = []
        for x,y in block:
            xlist.append(x)
            ylist.append(y)
        
        c, r = max(xlist) - min(xlist) + 1 , max(ylist) - min(ylist) + 1
        new_block_table = [[0 for _ in range(r)] for _ in range(c)]
        
        for x, y in block:
            nx, ny = x - min(xlist), y - min(ylist) # 좌표 보정
            new_block_table[nx][ny] = 1
        
        blocks.append(new_block_table)
        
    return blocks
        
    
def rotate(block): # 직사각형, 90도 회전
    rotate_block = [[0 for _ in range(len(block))] for _ in range(len(block[0]))] # 행 열 개수 전환
    count = 0  # 크기 세기
    
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1:
                count += 1
                rotate_block[j][len(block) - 1 - i] = block[i][j]
                
    return rotate_block, count

    
def solution(game_board, table):
    '''
    빈칸 수와 퍼즐 연결된 조각이 딱 맞아야함 
    '''
    empty_gb = count_bfs(0, game_board)
    pieces = count_bfs(1, table)

    board_blocks = make_block(empty_gb)
    table_blocks = make_block(pieces)
    
    count = 0

    for bb in board_blocks:
        bb_flag = 0
        for tb in table_blocks:
            if bb_flag == 1:
                break # 이미 bb자리에 넣어서 tb를 그만 돌게 할 조건 필요
            for _ in range(4):
                if _ == 0:
                    tb2 = tb
                tb2, cnt = rotate(tb2) # 90, 180, 270, 0

                if tb2 == bb:
                    count += cnt
                    table_blocks.remove(tb)
                    bb_flag = 1
                    break
    

    return count
