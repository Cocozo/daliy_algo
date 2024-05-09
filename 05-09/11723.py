#집합 - 11723번 - 실버5
import sys

S = [0 for i in range(21)]

epoch = int(sys.stdin.readline().rstrip())

for i in range(epoch):
    args = sys.stdin.readline().split()
    if len(args) == 2:
        command = args[0]
        num = int(args[1])
        if command == 'add':
            S[num] = 1
        elif command == 'check':
            print(S[num])
        elif command == 'remove':
            S[num] = 0
        elif command == 'toggle':
            if S[num] == 0:
                S[num] = 1
            else:
                S[num] = 0
    else:
        command = args[0]
        if command == 'all':
            S = [1 for i in range(21)]
        elif command == 'empty':
            S = [0 for i in range(21)]
        