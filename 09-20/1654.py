import sys

MAX = 1000000
Wires = []

if __name__ == "__main__":
    k, n = map(int, sys.stdin.readline().split())
    for i in range(k):
        Wires.append(int(sys.stdin.readline().rstrip()))
    
    
    low = 1
    high = max(Wires)
    mid = 0
    target = mid
    while high >= low:
        mid = (low + high) // 2
        
        sum = 0
        
        for i in range(k):
            sum += Wires[i] // mid
            
        if sum >= n:
            target = mid
            low = mid + 1
        else :
            high = mid - 1
        
    print(target)