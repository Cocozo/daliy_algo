import sys

board = []

oragami = [0 for _ in range(2)]

def cut_oragami(startX, startY, n):
    k = board[startY][startX]
    check = False
    for i in range(startY, startY + n):
        if not check:
            for j in range(startX, startX + n):
                if board[i][j] != k:
                    check = True
                    break
        else:
            break
    
    if check:
        cut_oragami(startX, startY, n // 2)
        cut_oragami(startX + (n // 2), startY, n // 2)
        cut_oragami(startX, startY + (n // 2), n // 2)
        cut_oragami(startX + (n // 2), startY + (n // 2), n // 2)
    else:
        oragami[k] += 1
    

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    cut_oragami(0, 0, n)
    
    for i in oragami:
        print(i)