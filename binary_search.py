def binary_search_i(vals, target):
    left = 0
    right = len(vals) - 1
    while left <= right:
        mid = (left + right) // 2
        if vals[mid] == target:
            return mid, True
        elif vals[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None, False


# print(binary_search_i([1, 2, 3, 4, 5, 6, 7, 9], 1))


def binary_search_t(vals, target):
    def binary_search(vals, target, left, right):
        if left >= right:
            return None, False
        mid = (left + right) // 2
        if vals[mid] == target:
            return mid, True
        elif vals[mid] > target:
            return binary_search(vals, target, left, mid - 1)
        return binary_search(vals, target, mid + 1, right)

    return binary_search(vals, target, 0, len(vals) - 1)


# print(binary_search_t([5], -5))


def fixedPoint(A) -> int:
    def search(A, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            search(A, left, mid - 1)
        search(A, mid + 1, right)

    return search(A, 0, len(A) - 1)


print(fixedPoint([-10, -5, 0, 3, 7]))
