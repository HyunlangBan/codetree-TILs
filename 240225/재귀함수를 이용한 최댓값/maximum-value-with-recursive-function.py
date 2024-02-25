n = int(input())

# 재귀함수로 최댓값..........?
a = list(map(int, input().split()))

def func(i, max_val):
    if i == n:
        return max_val

    max_val = max(max_val, a[i])
    
    return func(i+1, max_val)

print(func(0, 0))