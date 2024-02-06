n, m = map(int, input().split())

# 공통된 최대 공약수로 나누고 몫을 각각 곱함

def func(n, m):
    max_i = 0
    for i in range (1, n//2+1):
        if n % i == 0 and m % i ==0:
            max_i = i

    x = n // max_i
    y = m // max_i

    print(max_i * x * y)

func(n, m)