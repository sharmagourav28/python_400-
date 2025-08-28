from collections import Counter


def majority_element(myarr):
    freq = Counter(myarr)
    n = len(myarr)
    for num, count in freq.items():
        if count > n // 2:
            return num
    return None


myarr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(myarr))
