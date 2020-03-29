import time
import collections

def sweet_formatting(*deco_args):
  def normal_decorator(fun):
    def format_this(*args):
      print("Question no {}, Problem Name - {}".format(*deco_args))
      print(f"SOLUTION for INPUT - {args}")
      t1 = time.time()
      print(fun(*args))
      print(f"Time Taken {time.time() - t1} sec")
      print("*" * 20)

    return format_this
  return normal_decorator

@sweet_formatting("11.Sliding Window O(N) time and space complexity", "Sorted Squared Array")
def sortedSquaredArray(array):
    """This is solved by Sliding Window, keep a window at both ends and run a while loop"""
    # Inp [-6, -4, 1, 2, 3, 5]
    # Out - [1, 4, 9, 16, 25, 36]

    left = 0
    right = len(array) - 1
    result = [None] * len(array)
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            result[right - left] = array[left] ** 2
            left += 1
        else:
            result[right - left] = array[right] ** 2
            right -= 1
        print(result)
    return result

@sweet_formatting("Just a qustion from Code Signal O(n)","Matrix Element Sum")
def matrixElementsSum(matrix):
    avoid = set()
    result = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if j in avoid:
                continue
            if matrix[i][j] == 0:
                avoid.add(j)
                continue
            result += matrix[i][j]

    return result

@sweet_formatting("Brute force O(2N)","")
def allLongestStrings(inputArray):
    maxi = max([len(data) for data in inputArray])
    result = []
    for data in inputArray:
        if len(data) == maxi:
            result.append(data)

    return result
if __name__ == "__main__":
    # PROBLEM 11, code Signal Sorting
    # "You have a sorted array of integers. Write a function that returns a sorted array
    # containing the squares of those integers."
    # "For array = [-6, -4, 1, 2, 3, 5], the output should be
    # sortedSquaredArray(array) = [1, 4, 9, 16, 25, 36].
    # The array of squared integers from array is: [36, 16, 1, 4, 9, 25]. When sorted, it becomes: [1, 4, 9, 16, 25, 36]."
    array = [-6, -4, 1, 2, 3, 5]
    sortedSquaredArray(array)

    ls = [[0,1,1,2],
         [0,5,0,0],
         [2,0,3,3]]

    matrixElementsSum(ls)
    # Accepted

    ls = ["aa", "ab", "aba", "aa", "ad", "vcd", "aba"]
    allLongestStrings(ls)