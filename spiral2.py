def getSpiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    #Заполняем массив значениями нужного размера
    spiralArray = [[None] * n for j in range(n)]

    for i in range(1, n ** 2 + 1):
        myarray[x][y] = i
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and spiralArray[nx][ny] == None:
            x = nx
            y = ny
        else:
            dx = -dy
            dy = dx
            x = x + dx
            y = y + dy
    return spiralArray


def printSpiral(spiralArray):
    n = range(len(spiralArray))
    for y in n:
        for x in n:
            print(spiralArray[x][y], end=' ')
        print()

try:
    n = int(input())
except Exception:
    printSpiral(getSpiral(n))