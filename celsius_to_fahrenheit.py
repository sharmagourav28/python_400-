def celsius_to_fahrenheit(c):
    tem = (c * 9 / 5) + 32
    return tem


def fahreneit_to_celis(f):
    tem = (f - 32) * 5 / 9
    return tem


temp = int(input("Enter the temperature"))
print(celsius_to_fahrenheit(temp))
print(fahreneit_to_celis(temp))
