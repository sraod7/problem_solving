def maxArea(height) -> int:
    i = 0
    j = len(height) - 1
    max_a = 0
    a = 0

    while j - i >= 1:
        a = min(height[i], height[j]) * (j-i)
        if max_a < a:
            max_a = a

        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1

    return max_a

print(maxArea([1,8,6,2,5,4,8,3,7]))

