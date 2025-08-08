if a % 2 == 0:
    limit = a - 1
else:
    limit = a

i = 1
while i <= 2 * (limit // 2) + 1:
    print(i, end=", " if i < 2 * (limit // 2) + 1 else "")
    i += 2
