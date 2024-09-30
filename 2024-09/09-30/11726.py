import sys

dp = [0 for i in range(1001)]
dp[1] = 1
dp[2] = 2

def construct_block(n):
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = construct_block(n-1) + construct_block(n-2)
    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    
    print(construct_block(n) % 10007)