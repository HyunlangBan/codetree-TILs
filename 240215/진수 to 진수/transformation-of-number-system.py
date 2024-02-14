a, b = map(int, input().split())
n = list(map(int, list(input())))

# step1. a진수 to 10진수
num = 0
for i in range(len(n)):
    num = num*a + n[i]

# step2. 10진수 to b진수
res = []
while True:
    if num < b:
        res.append(num)
        break
    
    res.append(num%b)
    num //= b

for i in res[::-1]:
    print(i, end='')