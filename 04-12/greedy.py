def cal_distance(distance):
    n = 1
    bound_distance = 0
    while True:
        bound_distance = bound_distance + (n // 2) + (n % 2)
        if bound_distance >= distance :
            break
        else :
            n = n + 1

    print(n)


epoch = int(input())

x = []
y = []
for i in range(epoch):
    x_temp, y_temp = map(int, input().split())
    x.append(x_temp)
    y.append(y_temp)

for x_temp, y_temp in zip(x, y) : 
    cal_distance(y_temp - x_temp)
