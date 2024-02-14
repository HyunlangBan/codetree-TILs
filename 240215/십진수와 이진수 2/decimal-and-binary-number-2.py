n = input()
decimal = 0

for i in range(len(n)):
    decimal = decimal * 2 + int(n[i])

decimal = decimal * 17
bi = []
while True:
    if decimal < 2:
        bi.append(decimal)
        break
    
    bi.append(decimal%2)
    decimal = decimal // 2

for i in bi[::-1]:
    print(i, end="")