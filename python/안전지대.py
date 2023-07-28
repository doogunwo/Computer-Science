#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0]
#[0, 0, 1, 1, 0]
#[0, 0, 0, 0, 0]


def solution(board):
    n = len(board)
    dx = [-1,0,1]
    dy = [-1,0,1]
    boom  = []
    for i in range(n):
        for j in range(n):
    
            if board[i][j] == 1:
                boom.append((i,j))
    for x,y, in boom:
        for add_x in dx:
            nx = x+ add_x
            for add_y in dy:
                ny = y+ add_y
                if 0<=nx < n and 0<= ny <n:
                    board[nx][ny] =1
    cnt = sum(row.count(0) for row in board )
    return cnt


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
solution(board)

