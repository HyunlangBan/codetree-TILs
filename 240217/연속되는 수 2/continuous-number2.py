n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))

cnt = 0
cnts = []
for i in range(n):
    if i==0 or res[i] == res[i-1]:
        cnt += 1

    elif:
        cnts.append(cnt)
        cnt = 0

print(max(cnts))