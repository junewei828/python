def b_search(array, target):
    if len(array) == 0:
        return None

    mid = len(array) // 2
    if array[mid] == target:
        return mid

    left = array[:mid]
    right = array[mid+1:]

    if target > array[mid]:
        next_search = b_search(right, target)
        if not next_search:
            return None
        return mid + next_search + 1

    else:
        return b_search(left, target)


print(b_search([1, 2, 3, 4, 5], 5))
