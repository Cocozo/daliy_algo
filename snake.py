#그래프 탐색이론 1012번_ sloved.ac
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)

#위부터 탐색 위, 오, 아래
MAX = 50

direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


board = [ [0]*MAX for i in range( MAX ) ]
#checked = [ [0]*MAX for i in range( MAX ) ]

#그래프 탐색
def search_graph(y, x):
    
    board[y][x] = 0
    for (ay, ax) in direction:
        if y+ay == 50 or y+ay == -1 or x+ax == 50 or x+ax == -1 :
            continue
        if board[y+ay][x+ax] == 1 :
            search_graph(y+ay, x+ax)


#해당 함수가 메인일 시 실행
if __name__ == "__main__" :
    epoch = int(input())

    for _ in range(epoch):
        board = [ [0]*MAX for i in range( MAX ) ]
        num = 0
        m, n, k = map(int, input().split())
        for _ in range(k) :
            xTemp, yTemp = map(int, input().split())
            board[yTemp][xTemp] = 1

        for y in range(n):
            for x in range(m):
                if board[y][x] == 1 :
                    search_graph(y, x)
                    num = num + 1

        print(num)
