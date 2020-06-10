from typing import List


def getFirstIndex(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            r = m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return r


def getLastIndex(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            l = m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l



def searchRange(nums: List[int], target: int) -> List[int]:
    i1 = getFirstIndex(nums, target)
    i2 = getLastIndex(nums, target)

    return [i1, i2]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
