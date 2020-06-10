def productExceptSelf(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):  # from left to right
        res[i] = res[i - 1] * nums[i - 1]
    tmp = 1
    for i in range(len(nums) - 2, -1, -1):  # from right to left
        tmp = tmp * nums[i + 1]
        res[i] = res[i] * tmp
    return res


print(productExceptSelf([1,2,3]))