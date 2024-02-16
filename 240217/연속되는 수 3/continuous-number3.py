n = int(input())
a = [ int(input()) for _ in range(n) ]

res, cnt = 0, 0
for i in range(n):
    if i >= 1 and (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
        cnt += 1

    else:
        cnt = 1

    res = max(res, cnt)

print(res)