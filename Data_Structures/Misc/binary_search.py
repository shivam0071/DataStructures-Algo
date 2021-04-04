def binary_search(ls, start, end, find_me):
    """Recursive"""
    if end >= start:
        mid = start + (end - start) // 2
        # mid = (start + end) // 2

        if ls[mid] == find_me:
            return mid
        elif ls[mid] > find_me:
            return binary_search(ls, start, mid-1, find_me)
        else:
            return binary_search(ls, mid+1, end, find_me)
    else:
        return -1


def binary_search_iterative(ls, find_me):
    """Iterative"""
    start = 0
    end = len(ls) - 1

    while end >= start:
        mid = (start + end) // 2
        if ls[mid] == find_me:
            return mid
        elif ls[mid] > find_me:
            end = mid - 1
        else:
            start = mid + 1

    return -1


lss = [33, 55, 67, 89, 123, 345, 667]
print(binary_search(lss, 0, len(lss)-1, 67))
print(binary_search_iterative(lss, 67))