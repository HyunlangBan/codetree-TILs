n = int(input())

res = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    res += abs((x2-x1)*(y2-y1)+'a')

print(res)