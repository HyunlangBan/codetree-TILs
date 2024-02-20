MAX_R = 200
OFFSET = 100
n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
checked = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]

for (x, y) in rects:
    x, y = x+OFFSET, y+OFFSET
    for i in range(8):
        x1 = x + i
        for j in range(8):
            y1 = y + j
            checked[x1][y1] += 1

area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if checked[i][j] > 0:
            area += 1
print(area)