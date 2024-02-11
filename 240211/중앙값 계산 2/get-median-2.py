n = int(input())

x = list(map(int, input().split()))


for i in range(n+1):
    if i % 2 == 1:
        index = i//2
        new_part = sorted(x[:i])
        print(new_part[index], end=' ')