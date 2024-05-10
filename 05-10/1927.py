#최소힙 - 1927번 - 실버2
import sys
import heapq


heap = []

epoch = int(sys.stdin.readline().rstrip())

for i in range(epoch):
    com = int(sys.stdin.readline().rstrip())
    if com == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, com)
    