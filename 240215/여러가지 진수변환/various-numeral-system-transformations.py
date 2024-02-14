n, b = map(int, input().split())

res = []
while True:
    if n < b:
        res.append(n)
        break
    res.append(n % b)
    n = n // b

for i in res[::-1]:
    print(i, end='')