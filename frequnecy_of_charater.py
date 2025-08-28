mystr = "programming"
freq = {}
for char in mystr:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for k, v in freq.items():
    print(k, v)

from collections import Counter

cc = Counter(mystr)
print(cc)
for k, v in cc.items():
    print(k, v)
