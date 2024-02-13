a, b = map(int, input().split())
n = int(input())

# 10진수로 바꾸기
leng = len(str(n))

res = 0
for i in range(leng):
    res += a**i

cnt = 0
z = res
trans = []
while z:
    m = z // b
    n = z % b
    trans.append(n)
    z = m

for i in range(len(trans)):
    print(trans[len(trans)-i-1], end='')