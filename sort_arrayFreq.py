from collections import Counter

myarr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
freq = Counter(myarr)
mylen = []
for num,count in freq.items():
    