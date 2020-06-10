def maxPathSum(self, root: TreeNode) -> int:
    res = float('-inf')

    def helper(node):
        nonlocal res
        if not node:
            return 0

        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        res = max(res, left_sum + right_sum + node.val)

        return max(left_sum, right_sum) + node.val

    helper(root)

    return res