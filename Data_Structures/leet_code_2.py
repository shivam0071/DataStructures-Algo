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


@sweet_formatting("6. O(3N) using some extra space","Product of array except self")
def product_of_array_except_self(nums):
    """
    The simple sol was to get a total multiplication and divide by each element ( can't use divide)
    So what we can do is for each element calculate right side product and left side product in 2 separate loops
    once we have all the left right product iterate over the array one last time multiplying each element of left right
    :param nums:
    :return:
    """
    # Input - [1, 2, 3, 4]
    left_prod = [None] * len(nums)     # [1, 1, 2, 6]
    right_prod = [None] * len(nums)     # [24, 12, 4, 1]

    left_prod[0] = 1
    right_prod[-1] = 1

    # left products for each element
    left_product = 1
    for idx in range(1, len(nums)):
        left_product *=  nums[idx-1]
        left_prod[idx] = left_product


    # right products for each element
    right_product = 1
    for idx in range(len(nums)-2, -1, -1):
        right_product *= nums[idx + 1]
        right_prod[idx] = right_product

    # modify the actual array
    for idx in range(0, len(nums)):
        nums[idx] = left_prod[idx] * right_prod[idx]

    return nums

@sweet_formatting("7 O(n)","Subproduct less than K")
def numSubarrayProductLessThanK(nums, k):
    """
    Use Sliding window algorithm for this,
    We have a left window and a right window
    """
    if k <= 1:
        return 0

    result = 0
    product = 1

    left = 0
    right = 0

    while right < len(nums):

        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        result += right - left + 1 # It includes current element andall previous subarrays
        print(f"LEFT {left} RIGHT {right} RESULT {result}")
        right += 1

    return result

@sweet_formatting("","")
def maximum69Number(num):
    # 9669
    flag = True
    ls = []
    for n in str(num):
        if n == '6' and flag:
            flag = False
            ls.append('9')
        else:
            ls.append(n)
    # OR
    # return int(str(num).replace('6','9', 1))
    return int(''.join(ls))

@sweet_formatting("9. Trick, Read Question Carefully", "All Duplicate")
def all_duplicates_in_array(nums):
  # this question is same as question 3 of leet_code.py
  # O(n), No Extra Space
  # the integers value of the list should be less than or equal to len(ls)
  # in our example its 6 and mx integer is only 5

  # The solution is start marking integers negative(their repective index) as you visit them.
  # item 3 would mark item 5 as -5 now when we visit 3 again at index[-2] then we know we already visited that
  # item as 2 index(item 5) is marked negative

  # [4, 3, 2, 7, 8, 2, 3, 1]
  result = []
  for idx, data in enumerate(nums):
    data = abs(data)
    print(f"List {nums}, data -> {data}, abs data -> {abs(data)}")
    if nums[data - 1] < 0:
      result.append(data)
    else:
      nums[data - 1] = - nums[data - 1]

  if result:
      return result
  return -1

@sweet_formatting("10. O(n) using maths logic","Subarray Sum")
def subarraySum(nums, k):
    """
    The solution is to use a hashmap and maths logic
    keep doing sum of each element and add it to the dictionary
    so if suppose the sum is 6 and k is 4 then 6-4 would be 2
    this tells us that if the 2 is present in the hash_set then there must exist a subarray that makes 4
    as 4 + 2 = 6 and this subarray can be any thing 2,2 or 3,1 or 1, 3, 0,4 and so on that doesn't matter
    """
    result = 0
    sum = 0
    tracker = {0: 1}

    for data in nums:
        sum += data
        print(f"sum = {sum}, SUM - K = {sum-k}")
        if (sum - k) in tracker:
            result += tracker[sum - k]

        tracker.update({sum:tracker.setdefault(sum, 0) + 1})
        print(tracker)

    return result

@sweet_formatting("10. same same but different Way", "Subarray Sum")
def subarraySum_best(A, K):
    """ A nice way of using dictionary, Counter a subclass of dictionary"""
    count = collections.Counter()
    count[0] = 1
    ans = su = 0
    for x in A:
        su += x
        ans += count[su-K]
        count[su] += 1
    return ans

if __name__ == "__main__":
    # Medium # https://leetcode.com/problems/product-of-array-except-self/
    # 24th March 2020 - 1:08 PM
    # "Given an array nums of n integers where n > 1,
    # return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]."
    # you can't use division

    # Input - [1,2,3,4]
    # Output - [24, 12, 8, 6] -- Sum of all elements except self
    inp = [1,2,3,4]
    product_of_array_except_self(inp)

    # ACCEPTED - Runtime: 128 ms, faster than 54.93% of Python3 online submissions for Product of Array Except Self.
    # Memory Usage: 19.2 MB, less than 98.00% of Python3 online submissions for Product of Array Except Self.


    #************************************************************************************************
    # PROBLEM 7
    # "LeetCode 713. Subarray Product Less Than K"
    # "Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k."
    # [10, 5, 2, 6], k = 100
    # Output - 8
    # "The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    # Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k."
    # 25th March 2020 12:05 PM
    # ls = [10, 5, 2, 6]
    ls = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    # ls = [1,2,3]
    k = 19
    numSubarrayProductLessThanK(ls, k)
    "Accepted	1216 ms	16.7 MB	"

    # 8 1323. Maximum 69 Number EASY
    # "Given a positive integer num consisting only of digits 6 and 9.
    # Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6)."
    # num = 9669
    # num = 9999
    num = 66
    maximum69Number(num)
    # "Runtime: 32 ms, faster than 15.07% of Python3 online submissions for Maximum 69 Number.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number."

    # Problem 9
    # @ 27/03/2020 12:15 PM Friday
    # Medium 442 "Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    # Find all the elements that appear twice in this array."
    ls = [4,3,2,7,8,2,3,1]
    # output = [2,3]
    all_duplicates_in_array(ls)
    # "Runtime: 388 ms, faster than 69.19% of Python3 online submissions for Find All Duplicates in an Array.
    # Memory Usage: 21.3 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array."

    # Problem 10
    # "Given an array of integers and an integer k, you need to find the total number of
    # continuous subarrays whose sum equals to k."
    # Input: nums = [1, 1, 1], k = 2
    # Output: 2
    # 28-03-2020 5:00 PM
    ls = [2, 1, 3, 5, 4, -4, 4]
    k = 4
    subarraySum(ls, k)
    # """Runtime: 116 ms, faster than 61.73% of Python3 online submissions for Subarray Sum Equals K.
    # Memory Usage: 16.3 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K"""
    subarraySum_best(ls,k)