import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        queue = deque()
        printed = 0
        n, m = map(int, sys.stdin.readline().split())
        queue = deque(list(map(int, sys.stdin.readline().split())))
        while True:
            high = max(queue)
            if queue[0] < high:
                temp = queue.popleft()
                queue.append(temp)
                if m == 0:
                    m = len(queue)-1
                else:
                    m -= 1
            else:
                queue.popleft()
                printed += 1
                if m == 0:
                    print(printed)
                    break
                m -= 1