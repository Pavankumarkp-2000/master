a = 4  # example input

i = 0
count = 0
while count < a:
    print(2 * count + 1, end=", " if count < a - 1 else "")
    count += 1
