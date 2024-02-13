n = 29
digits = []

if n == 0:
    print(0)
    exit

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n%2)
    n //= 2

for i in digits[::-1]:
    print(i, end="")