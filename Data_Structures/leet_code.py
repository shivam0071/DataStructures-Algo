import time

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

# 26th Jan 2020
# 7:10 Pm
# https://leetcode.com/problemset/all/

# PROBLEM 1
# https://leetcode.com/problems/two-sum/
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# ls = [3,3]
ls = [1, 3, 4, 6, 12, 334,98,34,4]
target = 8
# ls.sort()
# index = ls.index()
# BRUTE FORCE
@sweet_formatting("1. Brute Force Solution", "TwoSum")
def looper(ls, target):
  for idx, data in enumerate(ls):
    for idx2, d in enumerate(ls[idx+1:]):
      if data + d == target :
        return [idx, (idx + 1) + idx2]
        # break

## BEST SOLUTION -- > MEMOIZATION ##
@sweet_formatting("1. Best Solution", "TwoSum")
def twoSumBest(ls, target):
  h = {}
  for i, num in enumerate(ls):
    n = target - num
    if n not in h:
      h[num] = i
    else:
      return [h[n], i]

# What have you learnt from this ?
#   1.) Observe if there is any maths involved
#   2.) Think if this can be memoized

# ANSWER 2
@sweet_formatting("Using Kadanes Algo Time and Space Complexity O(N)","2. Max Sum Subarray")
def maximum_subarray(nums):
  """
  We can do it using Kadane's Algorithm
  """
  # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  maximum = nums[0]
  current = maximum
  for idx in range(1, len(nums)):
    current = max(current + nums[idx], nums[idx])
    maximum = max(maximum, current)

  return maximum

# Answer 3
@sweet_formatting("3. Memoize Solution", "First Duplicate")
def first_duplicate(a):
  # O(n), Takes extra Space
  remember = {}
  for data in a:
    if data not in remember:
      remember.update({data:-1})
    else:
      return data
  return -1

@sweet_formatting("3. Trick, Read Question Carefully", "First Duplicate")
def first_duplicate_trick(a):
  # O(n), No Extra Space
  # the integers value of the list should be less than or equal to len(ls)
  # in our example its 6 and mx integer is only 5

  # The solution is start marking integers negative(their repective index) as you visit them.
  # item 3 would mark item 5 as -5 now when we visit 3 again at index[-2] then we know we already visited that
  # item as 2 index(item 5) is marked negative

  # [2, 1, 3, 5, 3, 2]
  for idx, data in enumerate(a):
    data = abs(data)
    print(f"List {a}, data -> {data}, abs data -> {abs(data)}")
    if a[data - 1] < 0:
      return data
    else:
      a[data - 1] = - a[data - 1]

  return -1


# Answer 4
@sweet_formatting("4. Memoize Sol, O(n)", "First Non Repeating Char")
def first_not_repeating_character(s):
  # abacabad
  data = {}
  for idx, character in enumerate(s):
    if character not in data:
      data.update({character: idx})
    else:
      # data[character][0] += 1
      # data.update({character: data[character]})
      data.update({character: None})

 
  index = None
  result = '_'
  for k, v in data.items():
    if v != None and index == None:
      index = v
      result = k
    elif v:
      if v < index:
        index = v
        result = k

  return result

@sweet_formatting("5. sol with O(1) space complexity and o(2N)", "image rotation")
def rotateImage(a):
  # a = [[1, 2, 3],
  #      [4, 5, 6],
  #      [7, 8, 9]]

    # [[1,4,7],
    # [2,5,8],
    # [3,6,9]]

    # [[7,4,1],
    # [8,5,2],
    # [9,6,3]]

  # Transpose of a matrix
  # the diagonal always remains the same while the other elements exchange...with their diagonal partner
  for i in range(0, len(a)):
    for j in range(i, len(a)):
      temp = a[i][j]
      a[i][j]  = a[j][i]
      a[j][i] = temp


  print("Transpose",a)
  # mirror image of a matrix...move column wise using i and replace each row using j
  N = len(a)
  for i in range(0, N):
    for j in range(0, N//2):
      temp = a[i][j]
      a[i][j] = a[i][N-1-j]
      a[i][N-1-j] = temp

  return a



if __name__ == "__main__":
  # 26th Jan 2020
  # 7:10 Pm
  # https://leetcode.com/problemset/all/

  # PROBLEM 1
  # https://leetcode.com/problems/two-sum/
  # Given nums = [2, 7, 11, 15], target = 9,
  #
  # Because nums[0] + nums[1] = 2 + 7 = 9,
  # return [0, 1].
  looper(ls, target)
  twoSumBest(ls, target)


  # *************************************************
  # PROBLEM 2 . 22/03/2020 Sunday, Corona Curfew 10:23 AM
  # Leet Code Easy "53. Maximum Subarray"
  # "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum."
  # [-2,1,-3,4,-1,2,1,-5,4] Output - 6 ,
  #  Explanation [4,-1,2,1] has the largest sum = 6.
  ls = [-2,1,-3,4,-1,2,1,-5,4]
  maximum_subarray(ls)
  # "Runtime: 56 ms, faster than 98.84% of Python3 online submissions for Maximum Subarray.
  # Memory Usage: 13.6 MB, less than 71.54% of Python3 online submissions for Maximum Subarray."



  #********************************************
  # 3. First Duplicate
  # https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

  # "Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which
  # the second occurrence has the minimal index."

  # For example
  # a = [2, 1, 3, 5, 3, 2], then
  # output # should # be # firstDuplicate(a) = 3.

  # There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the
  # second occurrence of 2 does, so the answer is 3. [ -1 for no duplicates ]
  # fd = [2, 1, 3, 5, 3, 2]
  # fd = [2, 1, 4, 2]
  #
  fd = [1, 3, 2]
  first_duplicate(fd)
  first_duplicate_trick(fd)


  # 4. First Non Repeating character
  # "Given a string s consisting of small English letters, find and return the first instance of a
  # non-repeating character in it. If there is no such character, return '_'."

  # "For s = "abacabad", the output should be
  # firstNotRepeatingCharacter(s) = 'c'."

  first_not_repeating_character("z")

  # 5 Image Rotation
  a = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

  rotateImage(a)
