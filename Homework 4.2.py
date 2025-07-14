lst = [1, 3, 5]
def lst(nums):
    if not nums:
        return 0
    sum_even_index = sum(nums[::2])
    result = sum_even_index * nums[-1]
    return result
print(lst([1, 3, 5]))


lst = [6]
def lst(nums):
    if not nums:
        return 0
    sum_even_index = sum(nums[::2])
    result = sum_even_index * nums[-1]
    return result
print(lst([6]))


lst = []
def lst(nums):
    if not nums:
        return 0
    sum_even_index = sum(nums[::2])
    result = sum_even_index * nums[-1]
    return result
print(lst([]))