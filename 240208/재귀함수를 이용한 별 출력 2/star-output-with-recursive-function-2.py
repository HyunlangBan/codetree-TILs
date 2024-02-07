n = int(input())

def star(x):
    print("* "*x)

for i in range(n*2):
    if i < n:
        star(n-i)
    else:
        x = i-n+1
        star(x)