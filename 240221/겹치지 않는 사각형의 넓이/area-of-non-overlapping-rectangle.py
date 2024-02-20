# ax1, ay1, ax2, ay2 = map(int, input().split())
# bx1, by1, bx2, by2 = map(int, input().split())
# mx1, my1, mx2, my2 = map(int, input().split())

OFFSET = 1000
rects = [ tuple(map(int, input().split())) for _ in range(3) ]

checked = [ [0] * 2001 for _ in range(2001)]

for rec in rects:
    x1, y1, x2, y2 = rec
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] += 1

res = 0
for rec in rects[:2]:
    x1, y1, x2, y2 = rec
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            if checked[i][j] == 1:
                res += 1

print(res)