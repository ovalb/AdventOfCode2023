
input = open('in').read().split('\n')
board = [list(inp) for inp in input]

dirs = [
    (0, 1),
    (0, -1), 
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (-1, 1), 
    (1, -1)
]

def check_xmas(i, y, b):
    inbound = lambda x,y: 0 <= x < len(b) and 0 <= y < len(b[0])
    ans = 0
    for dx, dy in dirs:
        if inbound(i+3*dx, y+3*dy) and ''.join([b[i+k*dx][y+k*dy] for k in range(4)]) == "XMAS":
            ans += 1
    return ans

def p1():
    ans = 0
    for i in range(len(board)): 
        for y in range(len(board[0])):
            if board[i][y] == 'X':
                ans += check_xmas(i, y, board)
    return ans

def p2():
    def check_x_mas(i, y, b):
        inbound = 0 < i < len(b)-1 and 0 < y < len(b[0])-1
        x_mas = inbound and b[i-1][y-1] + b[i-1][y+1] + b[i+1][y-1] + b[i+1][y+1]
        return 1 if x_mas in {"MMSS", "SSMM", "MSMS", "SMSM"} else 0

    ans = 0
    for i in range(len(board)): 
        for y in range(len(board[0])):
            if board[i][y] == 'A':
                ans += check_x_mas(i, y, board)
    return ans


print(p1())
print(p2())



        
