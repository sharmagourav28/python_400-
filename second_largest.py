def second_max(myarr):
    firstmax = float("-inf")
    secondmax = float("-inf")

    for i in myarr:
        if i > firstmax:
            secondmax = firstmax
            firstmax = i
        elif i != firstmax and i > secondmax:
            secondmax = i

    return secondmax


# Example
myarr = [1, 2, 41, 4, 5, 24, 2]
print("Second max:", second_max(myarr))  # Output: 24
