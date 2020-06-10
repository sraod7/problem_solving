class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the pivot -> pivot is the first decreasing digit from the last element
        pivot = -1
        for i in range(1, len(nums))[::-1]:
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

        # if there is no pivot, then return the reversed number
        if pivot == -1:
            nums.reverse()
            return

        # if there is pivot, then swap the pivot with the least least value on the right side
        least_index = -1
        for i in range(pivot + 1, len(nums))[::-1]:
            if nums[i] > nums[pivot]:
                least_index = i
                break

        nums[pivot], nums[least_index] = nums[least_index], nums[pivot]

        i = pivot + 1
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # reverse the right side of the pivot






