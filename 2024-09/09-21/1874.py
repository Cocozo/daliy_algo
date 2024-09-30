import sys

arr = []
num = []
stack = []
action = []
if __name__ == "__main__" :
    n = int(sys.stdin.readline().rstrip())
    
    for i in range(0, n):
        arr.append(int(sys.stdin.readline().rstrip()))
        num.append(n - i)
    
    check = 0
    while True:
        if len(stack) == 0:
            temp = num.pop()
            stack.append(temp)
            action.append('+')
            continue
        
        if stack[-1] == arr[check]:
            stack.pop()
            check += 1
            action.append("-")
        else:
            if len(num) == 0:
                break
            temp = num.pop()
            stack.append(temp)
            action.append("+")
            
        
        if check == len(arr): 
            break
    
    if check == len(arr):
        for i in action:
            print(i)
    else:
        print("NO")