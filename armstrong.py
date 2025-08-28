def armstrongNumber(num):
    n = num
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem * rem * rem
        n = n // 10

    if sum == num:
        return True


print(armstrongNumber(153))
