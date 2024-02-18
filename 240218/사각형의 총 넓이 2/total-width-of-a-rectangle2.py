OFFSET = 100
MAX_R = 200

n = int(input())
rects = [ tuple(map(int, input().split())) for _ in range(n) ]

checked = [ [0]*MAX_R for _ in range(MAX_R) ]

for rec in rects:
    x1, y1, x2, y2 = rec
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = 1


res = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if checked[i][j]:
            res += 1


print(res)