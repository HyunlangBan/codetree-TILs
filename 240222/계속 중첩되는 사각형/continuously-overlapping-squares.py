# 빨: 1
# 파: 2

OFFSET = 10
MAX_R = 200

n = int(input())
rects = [ tuple(map(int, input().split())) for _ in range(n)]
checked = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]

for i, rec in enumerate(rects, start=1):
    x1, y1, x2, y2 = rec
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET

    # i가 홀수이면 빨강, 짝수이면 파랑
    if i%2 == 1:
        value = 1
    else:
        value = 2

    for p in range(x1, x2):
        for q in range(y1, y2):
            checked[p][q] = value


res = 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if checked[i][j] == 2:
            res += 1

print(res)