mystr = "swiss"
from collections import Counter

my = Counter(mystr)
print(my)
for i, j in my.items():
    if j == 1:
        print(i)
