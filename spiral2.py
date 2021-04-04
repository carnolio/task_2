def getSpiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        myarray[x][y] = i
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x = nx
            y = ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    return myarray


def printSpiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()

try:
    print("Введите целое положительное число:")
    n = int(input())
    printSpiral(getSpiral(n))
except Exception:
    print("Вероятно ввели не число")