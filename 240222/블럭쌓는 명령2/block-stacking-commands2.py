n, k = map(int, input().split())
checked = [0] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        checked[i] += 1

print(max(checked))