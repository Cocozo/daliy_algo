import sys

# 복습필요! -> sliding window

base = "IOI"

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    string = sys.stdin.readline().rstrip()
    
    matched = 0
    i = 0
    k = 0
    while i < (m - 1):
        if string[i:i+3] == base:
            k += 1
            i += 2
            if k == n:
                matched += 1
                k -= 1
        else:
            k = 0
            i += 1
    
    print(matched)