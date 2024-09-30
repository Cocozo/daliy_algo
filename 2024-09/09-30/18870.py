import sys

dic = {}

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    k = list(map(int, sys.stdin.readline().split()))
    elemet = set(k)

    acc = 0
    for i in sorted(elemet):
        dic[i] = acc
        acc += 1
    
    for i in range(len(k)): 
        k[i] = dic[k[i]]
    
    print(" ".join(list(map(str, k))))