#교실 최대 인원수 23971번_ sloved.ac
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)


if __name__ == "__main__" : 
    h,w,n,m = map(int, input().split())
    print((1+((h-1) // (n+1)))*(1+((w-1) // (m+1))))