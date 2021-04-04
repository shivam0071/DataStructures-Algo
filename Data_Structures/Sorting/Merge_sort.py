def merge_sort(arr, call='Parent'):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, 'LEFT')
        merge_sort(right, 'RIGHT')

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    else:
        # print(f'Outside {arr}, Call - {call}')
        pass


ls = [12, 13, 11, 7, 6, 5, 14]
print(f'Before Sort {ls}')
merge_sort(ls)
print(f"After Sort {ls}")
