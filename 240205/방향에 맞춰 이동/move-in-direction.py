n = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
x, y = (0, 0)
# 북(N), 남(S), 동(E), 서(W)
for i in range(n):
    p, num = input().split()
    num = int(num)
    if p == 'N':
        x, y = x + (dx[0]*num), y + (dy[0]*num)
    elif p == 'S':
        x, y = x + (dx[1]*num), y + (dy[1]*num)
    elif p == 'E':
        x, y = x + (dx[2]*num), y + (dy[2]*num)
    elif p == 'W':
        x, y = x + (dx[3]*num), y + (dy[3]*num)


print(x, y)