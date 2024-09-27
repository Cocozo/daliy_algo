import sys
from collections import deque



if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        intro = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline().rstrip())
        queue = deque(sys.stdin.readline().split(','))
        
        if n != 0:
            first = queue.popleft()
            first = first[1:]
            queue.appendleft(first)
            
            last = queue.pop()
            last = last[:-2]
            queue.append(last)
        else:
            queue.pop()
        
        reverse = False
        checksum = True
        for i in intro:
            if i == "R":
                reverse = not reverse
            if i == "D":
                if len(queue) == 0:
                    checksum = not checksum
                    break
                if reverse:
                    queue.pop()
                else:
                    queue.popleft()
        
        if checksum:
            if reverse:
                queue.reverse()
            print('[' + ",".join(queue)+']')
        else:
            print("error")