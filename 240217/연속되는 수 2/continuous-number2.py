n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))

cnt = 1
cnts = []
for i in range(n-1):
    if res[i] == res[i+1]:
        cnt += 1

    else:
        cnts.append(cnt)
        cnt = 1

print(max(cnts))