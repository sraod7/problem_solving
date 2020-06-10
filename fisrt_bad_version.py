def isBadVersion(n):
    return n > 3

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    r = n

    while l < r:
        m = (l + r) // 2
        res = isBadVersion(m)

        if res:
            r = m
        else:
            l = m + 1

    return l

print(firstBadVersion(5))