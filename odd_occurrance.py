mynumber = [1, 2, 31, 1, 31, 1, 31, 3, 4, 32, 2]
freq = {}
for i in mynumber:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for k, v in freq.items():
    if v % 2 != 0:
        print(k, v)
