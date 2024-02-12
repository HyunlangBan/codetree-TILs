# 키가 더 작은 학생이 앞
# 키가 동일하다면 몸무게가 더 큰 학생이 앞
n = int(input())
res = []


for i in range(n):
    h, w = map(int, input().split())
    res.append((h,w, i+1))