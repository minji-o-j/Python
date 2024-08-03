def check_win(board): 
    win_O = -1
    win_X = -1
    
    for i in range(3):
        # 가로 확인
        if board[i][0]==board[i][1]==board[i][2]=='O':
            win_O = 1
        if board[i][0]==board[i][1]==board[i][2]=='X':
            win_X = 1
        
        # 세로 확인
        if board[0][i]==board[1][i]==board[2][i]=='O':
            win_O = 1
        if board[0][i]==board[1][i]==board[2][i]=='X':
            win_X = 1

    # 대각선 확인
    if (board[0][0]==board[1][1]==board[2][2]=='O') or (board[0][2]==board[1][1]==board[2][0]=='O'): 
        win_O = 1
    elif (board[0][0]==board[1][1]==board[2][2]=='X') or (board[0][2]==board[1][1]==board[2][0]=='X'): 
        win_X = 1
    return win_O, win_X # x랑 y의 승리여부 return, 이기면 1 지면 0


def solution(board):
    # count
    count_O = 0
    count_X = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                count_O+=1
            elif board[i][j]=='X':
                count_X +=1
                
    '''종료하지 않을 조건
    O의 개수 = X의 개수 또는
    O의 개수 = X의 개수 + 1
    '''
    if not (count_O == count_X or count_O == count_X+1):
        return 0 # 종료

    ''' 종료 조건
    O가 승리 조건을 만족했는데 X랑 개수가 똑같은 경우
    X가 승리 조건을 만족했는데 O의 개수가 1개 더 많은 경우
    '''
    win_O, win_X = check_win(board)

    if win_O==win_X==1:
        return 0 # 둘다 이길 순 없음    
    if win_O==1 and count_O==count_X:
        return 0
    if win_X==1 and count_O==count_X+1:
        return 0
    
    
    return 1
