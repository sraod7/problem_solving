from typing import List


def largest_number(nums: List[int]) -> str:
    res = ''
    for num in nums:
        res += str(num)
    return res


print(largest_number([3, 30, 34, 5, 9]))
