import sys

save = [-1 for _ in range(12)]

def combination_count(n):
    if save[n] != -1 :
        return save[n]
    
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        result = combination_count(n-1) + combination_count(n-2) + combination_count(n-3)
        save[n] = result
        return result

if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        print(combination_count(n))