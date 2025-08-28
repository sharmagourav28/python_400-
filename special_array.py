myarr = [1, 2, 3, 4, 5, 6, 8]
flag = True
for i in myarr:
    if i % 2 == i:
        flag = True
    else:
        flag: False
        break
print(flag)
