def get_closest(arr, target):
    n = len(arr)
    if target < arr[0]:
        return None
    if target > arr[n - 1]:
        return arr[n - 1]

    i = 0
    j = n - 1
    mid = None
    while i <= j:
        mid = (i + j) // 2
        if target > arr[mid] and target < arr[mid + 1]:
            return arr[mid]
        if  target > arr[mid]:
            i = mid
        elif target < arr[mid]:
            j = mid

    return None

arr = [1,5,8,9,11,15,18, 20]
target = 7

print(get_closest(arr, target))
