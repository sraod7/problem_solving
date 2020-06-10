def mySqrt(x: int) -> int:
    l = list(range(x))

    if x == 0 or x == 1:
        return x

    def binary_search(l, x, left, right):
        if left > right:
            return
        mid = (left + right) // 2

        if l[mid] * l[mid] == x:
            return mid
        if l[mid] * l[mid] > x:
            if mid !=0 and l[mid - 1] * l[mid - 1] < x:
                return mid
            return binary_search(l, x, left, mid - 1)
        if l[mid] * l[mid] < x:
            if mid != len(l) - 1 and l[mid + 1] * l[mid + 1] > x:
                return mid
            else:
                return binary_search(l, x, mid + 1, right)

    res = binary_search(l, x, 0, len(l) - 1)

    if res:
        return res
    else:
        return l[-1]


print(mySqrt(8))