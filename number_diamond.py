num = 5
for i in range(1, num + 1):
    print(" " * (num - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
