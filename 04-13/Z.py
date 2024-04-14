#분할정복 1074번_ sloved.ac
import sys
limitNumber = 15000
sys.setrecursionlimit(limitNumber)

def square_index(n, r, c, index_sum):
 
    if n == 0 :
        return index_sum

    a = pow(2, n) // 2
    if r < a : 
        if c < a :
            # 1사분면
            return square_index(n-1, r, c, index_sum)
        else :
            # 2사분면
            index_sum = index_sum + (pow(a, 2) * 1)
            return square_index(n-1, r, c-a, index_sum)
    else :
        if c < a :
            # 3사분면
            index_sum = index_sum + (pow(a, 2) * 2)
            return square_index(n-1, r-a, c, index_sum)
        else :
            # 4사분면
            index_sum = index_sum + (pow(a, 2) * 3)
            return square_index(n-1, r-a, c-a, index_sum)

if __name__ == "__main__" : 
    N, r, c = map(int, input().split())    
    print(square_index(N, r, c, 0))
