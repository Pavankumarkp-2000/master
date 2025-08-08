i = 1
while i <= 9:
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    result[i] = count
    i += 1

print(result)
