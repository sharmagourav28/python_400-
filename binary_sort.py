def search(nums, n):
    for i in range(len(nums)):
        if nums[i] >= n:
            return i
    return len(nums)


nums = [1, 3, 5, 6]
n = 7
print(search(nums, n))
