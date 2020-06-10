from typing import List


def singleNumber(nums) -> int:
    a = 0
    for i in nums:
        a = a ^ i
    return a

# print(singleNumber([2,2,1,4,5,4,5]))


def checkIfExist(arr: List[int]) -> bool:
    d = set()

    for val in arr:
        double = val * 2
        if double in d:
            return True
        d.add(val)

        if val % 2 == 0 and val != 0:
            half = val // 2
            if half in d:
                return True

    return False


print(checkIfExist([-2,0,10,-19,4,6,-8]))