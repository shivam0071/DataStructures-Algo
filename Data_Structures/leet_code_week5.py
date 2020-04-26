import time
import collections
print("Week 5 \nDate 13/04/2020 - 19/04/2020")

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

@sweet_formatting("O(n) but still really slow","128. HARD")
def longestConsecutive(nums) -> int:
    track = set(nums)
    result = 0

    for idx, data in enumerate(nums):
        count = 0
        if (data - 1) not in track:
            while data in track:
                data += 1
                count += 1

        result = max(result, count)
    return result

@sweet_formatting("res * 10 + temp","7. Reverse Integer")
def reverse(x: int):
    res = 0
    flag = False
    if x < 0:
        x = abs(x)
        flag = True

    while x > 0:
        temp1 = x % 10
        x = x // 10
        res = res * 10 + temp1

    if flag:
        if -res < -(2 ** 31):
            return 0
        return -res

    if res > (2 ** 31) -1:
        return 0
    return res

if __name__ == "__main__":
    # 18/04/2020
    # Problem 22
    # 128. Longest Consecutive Sequence - HARD
    # Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    # Input: [100, 4, 200, 1, 3, 2]
    # Output: 4
    # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    num = [100, 4, 200, 1, 3, 2]
    longestConsecutive(num)
    # Runtime: 96 ms, faster than 15.14% of Python3 online submissions for Longest Consecutive Sequence.
    # Memory Usage: 15.1 MB, less than 7.41% of Python3 online submissions for Longest Consecutive Sequence.
    # REALYY SLOW MAN
    # Changing nums to sets
    # Runtime: 60 ms, faster than 42.41% of Python3 online submissions for Longest Consecutive Sequence.
    # Memory Usage: 15.1 MB, less than 7.41% of Python3 online submissions for Longest Consecutive Sequence.

    # [[1, 2], [3, 2], [1, 3], [4, 1], [3, 1], [2, 1], [2, 3], [4, 3], [4, 2], [3, 4], [2, 4]]

    # Problem 23 - EASY
    # 997. Find the Town Judge
    # Runtime: 1272 ms, faster than 7.33% of Python3 online submissions for Find the Town Judge.
    # Memory Usage: 18.4 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
    # I couldn't figure it out...eventhough i understand it now...still very slow solution

    # Problem 24 - MEDIUM
    # 856. Score of Parentheses
    #Runtime: 32 ms, faster than 29.36% of Python3 online submissions for Score of Parentheses.
    # Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Score of Parentheses.
    
    
    # Problem 25 - EASY
    # 155. Min Stack
    # Runtime: 56 ms, faster than 93.46% of Python3 online submissions for Min Stack.
    # Memory Usage: 17.5 MB, less than 5.36% of Python3 online submissions for Min Stack.
    # Done by making 2 stacks

    # PROBLEM 26 - EASY DP [IMP]
    # 198. House Robber
    # Runtime: 20 ms, faster than 98.42% of Python3 online submissions for House Robber.
    # Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.


    # *************************************************************************************
    # *************************************************************************************
    # *************************************************************************************
    # *************************************************************************************
    # *************************************************************************************

    # just adding some easy questions here, WEEK 6 - 20th April 2020 - 26th April 2020

    # 1108. Defanging an IP Address - Very Easy
    #     Runtime: 28 ms, faster than 64.54% of Python3 online submissions for Defanging an IP Address.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.


    # 349. Intersection of Two Arrays -- EASY
    # Runtime: 44 ms, faster than 74.47% of Python3 online submissions for Intersection of Two Arrays.
    # Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Intersection of Two Arrays.

    # 7. Reverse Integer
    reverse(-1534236469)
    # ACCEPTED

    # 1342. Number of Steps to Reduce a Number to Zero - Very Very Easy
    # Runtime: 28 ms, faster than 68.08% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    # Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero
    # Others have converted the num into binary and for every 0 count += 1 and for every 1 , count += 2 (subtract and divide)
    # except for the first 1...that will be 1-1 ...hence count = 1
    # Runtime - Runtime: 24 ms, faster than 89.61% of Python3 online submissions for Number of Steps to Reduce a Number to Zero