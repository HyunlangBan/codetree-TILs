a, b = map(int, input().split())

def func(a, b):
    if a > b:
        # a가 큰 값, b가 작은 값
        a = a * 2
        b = b + 10
    else:
        # b가 큰 값, a가 작은 값
        a = a + 10
        b = b * 2

    print(a, b)

func(a, b)