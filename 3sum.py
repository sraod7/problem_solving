from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i == 0 or nums[i] != nums[i - 1]:
            low = i + 1
            high = len(nums) - 1
            target = 0 - nums[i]

            while low < high:
                if nums[low] + nums[high] == target:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1

    return res


print(threeSum([-1,0,1,2,-1,-4]))


# [[-1,-1,2],[-1,0,1]]
