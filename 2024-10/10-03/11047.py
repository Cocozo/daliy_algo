import sys

conins = []

if __name__ == "__main__" : 
    n, k = map(int, sys.stdin.readline().split())
    
    for i in range(n) :
        conins.append(int(sys.stdin.readline().rstrip()))
    conins.reverse()
    
    nums = 0
    for coin in conins :
        while k >= coin:
            nums += k // coin
            k = k % coin
    
    print(nums)