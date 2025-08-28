def find_pair(arr, target):
    seen = set()
    result = []
    for num in arr:
        diff = target - num
        if diff in seen:
            result.append((diff, num))
        seen.add(num)
    return result


print(find_pair([2, 4, 3, 4, 5, 7, 8, 9], 7))
