n = int(input())

def func(n):
    if n < 10:
        return n*n

    return func(n//10) + ((n%10)*(n%10))

print(func(n))