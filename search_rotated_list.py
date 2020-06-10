from typing import List


def search(nums: List[int], target: int) -> int:
    # find the the lowest point

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    start = left
    left = 0
    right = len(nums) - 1

    if target > nums[right]:
        right = start
    else:
        left = start

    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search([4,5,6,7,0,1,2], 0))