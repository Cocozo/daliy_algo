import sys

if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    
    for _ in range(n):
        comb = {}
        m = int(sys.stdin.readline().rstrip())
        
        for _ in range(m):
            val, key = map(str, sys.stdin.readline().split())
            if key in comb:
                comb[key].append(val)
            else:
                comb[key] = [val]

        sum = 1
        for k in comb:
            sum *= len(comb[k]) + 1
        
        sum = sum - 1
        print(sum)