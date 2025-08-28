rows = int(input("Enter the number"))
for i in range(1, rows + 1):
    print("_" * (rows - i) + "*" * (2 * i - 1))
