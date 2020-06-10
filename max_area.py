def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left != right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1

    return max_area

print(maxArea([2,3,4,5,18,17,6]))