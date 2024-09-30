import sys

stair = []

save = []

def count_highest(n):
    
    if save[n] >= 0:
        return save[n]
    
    if n < 0:
        return 0
    
    x = count_highest(n-3) + stair[n-1] + stair[n]
    y = count_highest(n-2) + stair[n]
    
    if x >= y:
        save[n] = x
        return x
    else:
        save[n] = y
        return y
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        stair.append(int(sys.stdin.readline().rstrip()))
        save.append(-1)
    if n == 1:
        print(stair[0])
    elif n == 2:
        print(stair[0] + stair[1])
    else:
        save[0] = stair[0]
        save[1] = stair[0] + stair[1]
        count_highest(n-1)
        print(save[n-1])