def find_missing(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


arr = [1, 2, 3, 5, 6]
print(find_missing(arr))
