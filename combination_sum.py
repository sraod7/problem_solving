def combinationSum(candidates, target: int):
    # candidates.sort()
    res = []

    def helper(curr_arr, index, remaining_target):
        if remaining_target < 0:
            return
        if index == len(candidates):
            return
        if remaining_target == 0:
            res.append(curr_arr)
            return

        for i in range(index, len(candidates)):
            helper(curr_arr + [candidates[i]], i, remaining_target - candidates[i])

    helper([], 0, target)
    return res