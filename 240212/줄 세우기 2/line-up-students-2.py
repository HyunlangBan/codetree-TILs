# 키가 더 작은 학생이 앞
# 키가 동일하다면 몸무게가 더 큰 학생이 앞
n = int(input())
res = []
heights = []


for i in range(n):
    h, w = map(int, input().split())
    res.append((w,h, i+1))
    heights.append(h)

res = sorted(res, reverse=True)
heights = sorted(list(set(heights)))

for height in heights:
    for r in res:
        w, h, n = r
        if h == height:
            print(h, w, n)