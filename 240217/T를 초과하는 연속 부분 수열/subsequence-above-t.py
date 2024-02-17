n, t = map(int, input().split())

a = list(map(int, input().split()))

res, cnt = 0, 0
for i in range(n):
    if i >= 1 and a[i] > t:
        cnt += 1
    else:
        cnt = 0

    # print(cnt)

    res = max(res, cnt)

print(res)