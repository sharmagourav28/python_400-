from collections import Counter

myarr = [1, 3, 4, 2, 2]
freq = Counter(myarr)
for num, count in freq.items():
    if count > 1:
        print(num)
