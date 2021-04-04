# Python program for implementation of MergeSort

def mergeSort(arr, call='Parent'):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2
        print(f"Arr  --- {arr}  Mid - {mid}, CALL - {call}")
        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L, 'LEFT')

        # Sorting the second half
        mergeSort(R, 'RIGHT')

        print(f"ARRRR  --- {arr}, Mid - {mid}, CALL - {call}")
        print(f"New ARR 0 - {arr}, Mid - {mid}, CALL - {call}, L - {L}, R - {R}")
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        print(f"NEW ARR 1- {arr}, {i}, {j}, {k}")
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        print(f"NEW ARR 2- {arr}, {i}, {j}, {k}")
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(f"NEW ARR 3- {arr}, {i}, {j}, {k}")
    else:
        print(f"OUT  --- {arr}, CALL - {call}")


# Code to print the list

# Driver code to test above
arr = [12, 13, 11, 7, 6, 5, 14]
n = len(arr)
print("Given array is")
for i in range(n):
    print(arr[i], end=",")

mergeSort(arr)
print("\nSorted array is")
for i in range(n):
    print(arr[i], end=",")
