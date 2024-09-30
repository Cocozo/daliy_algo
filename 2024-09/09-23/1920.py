import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    
    arr.sort()
    

    
    for i in nums:
        low = 0
        high = len(arr) - 1
        found = False
        while low <= high:
            mid = (low+high) // 2
            if i > arr[mid]:
                low = mid + 1
            elif i < arr[mid]:
                high = mid - 1
            elif i == arr[mid]:
                found = True
                break
        if found:
            print(1)
        else:
            print(0)