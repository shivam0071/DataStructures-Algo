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

@sweet_formatting("525. Medium, O(N) ","525. Contiguous Array")
def findMaxLength(nums):
    """
    Add +1 when u see a 1 and add -1 when you see a 0 and save this info in a dictionary
    so if a count appears twice one in small index and one in large idx then we know some subarray exist
    so update the max_count based on large_idx - small_idx and get the results, initally add a 0 count in the dict
    for any 0 sum
    """

    # [1, 1, 1, 0, 1, 1, 0, 0, 0, 1]

    max_count = 0;
    counts = {0 : -1} # for any subarray with 0 count
    count = 0
    for idx, num in enumerate(nums):
        if num == 0:
            count += -1
        else:
            count += 1

        if count in counts:
            max_count = max(max_count, idx - counts[count]) # current idx - old idx
        else:
            counts.update({count: idx})
        # print(f"Count {count} -- idx {idx} -- max counts {max_count} -- input {nums}")
        # print(counts)

    return max_count

@sweet_formatting("","621")
def leastInterval(tasks, n):
    # n = 2
    # ["A", "A", "A", "B", "B", "B"]
    from collections import Counter
    total = Counter(tasks)
    max_value = total.most_common()[0][-1] - 1
    idle_slots = max_value * n

    for data in total.most_common()[:0:-1]:
        idle_slots -= min(data[-1], max_value)

    if idle_slots > 0:
        return idle_slots + len(tasks)
    else:
        return len(tasks)

@sweet_formatting("","")
def searchRange(nums, target):
    result = [-1, -1]

    result[0] = search_left_target(nums, target)
    result[1] = search_right_target(nums, target)

    return result

def search_left_target(nums, target):
    start = 0
    end = len(nums) - 1
    res = -1
    while start <= end:
        mid_point = start + (end - start) // 2
        if nums[mid_point] >= target: #Note : there is no equals in Binary Search
            end  = mid_point - 1
        else:
            start = mid_point + 1

        if nums[mid_point] == target :
            res = mid_point

    return res

def search_right_target(nums, target):
    start = 0
    end = len(nums) - 1
    res = -1
    while start <= end:
        mid_point = start + (end - start) // 2
        if nums[mid_point] <= target:  # Note : there is no equals in Binary Search
            start = mid_point + 1
        else:
            end = mid_point - 1

        if nums[mid_point] == target:
            res = mid_point

    return res

@sweet_formatting("O(n)","56. Merge Intervals")
def merge(intervals):
    """The trick here is to keep a current interval saved and update it according to the next element"""

    if not intervals:
        return []
    result = []
    intervals = sorted(intervals)
    current_interval = intervals[0]
    result.append(current_interval)
    for idx in range(0, len(intervals)):
        current_begin = current_interval[0]
        current_end = current_interval[1]
        next_begin = intervals[idx][0]
        next_end = intervals[idx][1]
        if current_end >= next_begin:
            current_interval[1] = max(current_end, next_end)
        else:
            current_interval = intervals[idx]
            result.append(current_interval)

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

    # Problem 12
    # 4/4/2020 - -11:45 AM
    # 525 Contiguous Array
    # "Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1."
    # "Input: [0,1]
    # Output: 2
    # Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1."
    # ls = [1,1,1,0,1,1,0,0,0,1]
    ls = [1, 0, 1, 0]
    findMaxLength(ls)
    # "Runtime: 888 ms, faster than 92.64% of Python3 online submissions for Contiguous Array.
    # Memory Usage: 18.2 MB, less than 16.67% of Python3 online submissions for Contiguous Array."

    # Problem 13
    # "621. Task Scheduler"
    # https: // leetcode.com / problems / task - scheduler /
    # Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
    # Output: 8
    # Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
    # tasks = ["A", "A", "A", "B", "B", "B"]
    # tasks = ["A", "A", "A", "A","A", "B", "B", "B"]
    tasks = ["C", "C", "C", "C","C", "B", "B", "B","B", "B", "A", "A","A", "D","D","E","E","F"]
    n = 4
    leastInterval(tasks, n)
    # "Runtime: 412 ms, faster than 84.24% of Python3 online submissions for Task Scheduler.
    # Memory Usage: 13.9 MB, less than 5.00% of Python3 online submissions for Task Scheduler."


    # 04/04/2020 8:00 PM
    # Problem 14
    # "34. Find First and Last Position of Element in Sorted Array"
    # https: // leetcode.com / problems / find - first - and -last - position - of - element - in -sorted - array /
    # Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    # Output: [3, 4]
    # Input: nums = [5, 7, 7, 8, 8, 10], target = 6
    # Output: [-1, -1]

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    searchRange(nums, target)
    # "Runtime: 76 ms, faster than 99.27% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    # Memory Usage: 15.3 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array."


    # Problem 15, 56 Leetcode
    # "Given a collection of intervals, merge all overlapping intervals.
    # Example 1:
    #
    # Input: [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]."
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1,4],[0,4]]
    merge(intervals)
    # "Runtime: 80 ms, faster than 96.10% of Python3 online submissions for Merge Intervals.
    # Memory Usage: 15.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals."