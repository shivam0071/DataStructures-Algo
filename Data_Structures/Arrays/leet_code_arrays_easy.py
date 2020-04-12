import time
import collections
print("Week 4 \nDate 11/04/2020 - 12/04/2020")

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

@sweet_formatting("1. Easy ","1313")
def decompressRLElist(nums):
        output = []
        multiple = 0
        for idx, item in enumerate(nums):
            if idx % 2 == 0:
                multiple = item
            else:
                output.extend([item] * multiple)
        return output

@sweet_formatting("1. Easy Faster than previous solution","1313")
def decompressRLElist_2(nums):
        output = []
        for idx in range(0, len(nums), 2):
            output.extend([nums[idx + 1]] * nums[idx])
        return output

@sweet_formatting("3. o(n^2)","")
def smallerNumbersThanCurrent(nums):
    #  [8,1,2,2,3]
    output = []
    for data in nums:
        count = 0
        for data2 in nums:
            if data2 < data:
               count += 1

        output.append(count)

    print(output)

@sweet_formatting("4. good ans as i used max plus maths acc to TIPS o(N)","1266, Easy")
def minTimeToVisitAllPoints(points):
    total_time = 0

    for idx in range(0 ,len(points) - 1):
        curr = points[idx]
        tar = points[idx + 1]
        total_time += max(abs(tar[0] - curr[0]), abs(tar[1] - curr[1]))

    return total_time

@sweet_formatting("","")
def flipAndInvertImage(A):
    """Everything i did was poor...the simple solution is to iterate over each row in revers and then toggle"""
    # The solution is this
    # result = []
    # for row in A:
    #     result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
    # return result

    if len(A[0]) <= 1:
        for data in A:
            data[0] = 0 if data[0] > 0 else 1
        return A
    for i in range(len(A)):
        # print(f"Before {A} when i = {i}")
        for j in range(0, len(A[0])//2):
            temp = A[i][j]
            temp2 = A[i][len(A[0]) - 1 - j]
            A[i][j] = temp2
            A[i][len(A[0]) - 1 - j] = temp

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = 0 if A[i][j] > 0 else 1

    return A

@sweet_formatting("","")
def commonChars(A):
    # A = ["coooool","loock","cook"]
    base = collections.Counter(A[0])
    res = []
    for idx in range(1, len(A)):
        curr = collections.Counter(A[idx])
        base = curr & base
        print(base)

    # for key, val in base.items():
        # res.extend([key] * val)
    #
    # return res
    return list(base.elements())

if __name__ == "__main__":
    # Arrays - Easy 1
    # Problem - 1313
    # Input: nums = [1,2,3,4]
    # Output: [2,4,4,4]
    # Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
    # The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
    # At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
    num = [1, 2, 3, 4]
    num = [1,1,2,3]
    decompressRLElist(num)
    # Runtime: 72 ms, faster than 37.82% of Python3 online submissions for Decompress Run-Length Encoded List.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.

    decompressRLElist_2(num)
    #Runtime: 64 ms, faster than 85.56% of Python3 online submissions for Decompress Run-Length Encoded List.
    # Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.


    # PROBLEM 2 EASY - Did there only - did in 4 mins
    # 1295 . Runtime: 52 ms, faster than 75.01% of Python3 online submissions for Find Numbers with Even Number of Digits.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.


    # PROBLEM -3
    # 1365  EASY 02:04 PM - Took 8 mins to read, setup(here) ,think and code the solution
    nums = [8,1,2,2,3]
    nums = [6,5,4,8]
    nums = [7,7,7,7]
    smallerNumbersThanCurrent(nums)
    # Runtime: 280 ms, faster than 41.84% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

    # PROBLEM - 4
    # 1266 EASY
    # "Input: points = [[1,1],[3,4],[-1,0]]
    # Output: 7
    # Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
    # Time from [1,1] to [3,4] = 3 seconds
    # Time from [3,4] to [-1,0] = 4 seconds
    # Total time = 7 seconds"
    points = [[1, 1], [3, 4], [-1, 0]]
    points = [[3,2],[-2,2]]
    minTimeToVisitAllPoints(points)
    # "Runtime: 56 ms, faster than 84.29% of Python3 online submissions for Minimum Time Visiting All Points.
    # Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points."

    # Problem - 5
    # 1299 . ran a reverse loop,
    # Runtime: 128 ms, faster than 77.42% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    # Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.

    # Problem - 6
    # 1351 - Iterate over each and every element of matrix
    # Runtime: 128 ms, faster than 59.31% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    # Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

    # Problem 7
    # 1304. Find N Unique Integers Sum up to Zer
    #     Runtime: 32 ms, faster than 62.34% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # IMPROVED
    # Runtime: 28 ms, faster than 86.43% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.

    # EVEN BETTER SOLUTION USING MATHS by SOMEONE
    # range(1 - n, n, 2) <- Solution
    # Runtime: 20 ms, faster than 99.33% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.

    # Problem 8
    # 832. Flipping an Image
    # Input: [[1,1,0],[1,0,1],[0,0,0]]
    # Output: [[1,0,0],[0,1,0],[1,1,1]]
    # Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    # Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
    # A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    # A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    # A = [[1],[0],[1]]]
    A = [[0,1,1,1,1],[0,1,1,0,0],[0,1,1,1,1],[1,0,0,1,0],[0,0,0,0,1]]
    flipAndInvertImage(A)
    # Runtime: 56 ms, faster than 15.39% of Python3 online submissions for Flipping an Image.
    # Memory Usage: 13.8 MB, less than 6.00% of Python3 online submissions for Flipping an Image.

    # Problem 9
    # 905 -- Space complxity is too much
    # Runtime: 68 ms, faster than 99.77% of Python3 online submissions for Sort Array By Parity.
    # Memory Usage: 14.5 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.
    # return ([x for x in A if x % 2 == 0] +
    #     [x for x in A if x % 2 == 1])

    # Problem - 10 - Impressive solution indeed
    # 1380. Lucky Numbers in a Matrix
    # Runtime: 128 ms, faster than 96.15% of Python3 online submissions for Lucky Numbers in a Matrix.
    # Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Lucky Numbers in a Matrix.

    # 12-04-2020 11:52 AM
    # PRoblem 11
    # 977. Squares of a Sorted Array
    # Runtime: 488 ms, faster than 5.18% of Python3 online submissions for Squares of a Sorted Array.
    # Memory Usage: 15.6 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
    # NOTE :- one way to increase speed is to use collections.deque() inorder to insert to left side faster
    # NEW SPEED
    # Runtime: 244 ms, faster than 52.91% of Python3 online submissions for Squares of a Sorted Array.
    # Memory Usage: 16 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.

    # Problem 12
    # 561. Array Partition I
    #Runtime: 448 ms, faster than 5.05% of Python3 online submissions for Array Partition I.
    # Memory Usage: 16.1 MB, less than 6.06% of Python3 online submissions for Array Partition I.

    # Problem 13
    # 1385. Find the Distance Value Between Two Arrays
    # Runtime: 148 ms, faster than 26.32% of Python3 online submissions for Find the Distance Value Between Two Arrays.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.

    # Problem 14
    # 1394. Find Lucky Integer in an Array
    # Runtime: 52 ms, faster than 92.48% of Python3 online submissions for Find Lucky Integer in an Array.
    # Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Find Lucky Integer in an Array.

    # Problem 15
    # 1337. The K Weakest Rows in a Matrix
    # Runtime: 108 ms, faster than 89.55% of Python3 online submissions for The K Weakest Rows in a Matrix.
    # Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.

    # Problem 16
    # 1160. Find Words That Can Be Formed by Characters
    # Runtime: 196 ms, faster than 46.38% of Python3 online submissions for Find Words That Can Be Formed by Characters.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.

    # Problem 17
    # 1122. Relative Sort Array
    # Runtime: 40 ms, faster than 39.12% of Python3 online submissions for Relative Sort Array.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.

    # problem 18 - Fibonaci... :/
    # 509. Fibonacci Number
    # Runtime: 32 ms, faster than 40.82% of Python3 online submissions for Fibonacci Number.
    # Memory Usage: 13.8 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.

    # Problem 19
    # 922. Sort Array By Parity II
    # Using dictionary to store index and then iterating on those indexes...slow solution
    # Runtime: 256 ms, faster than 13.08% of Python3 online submissions for Sort Array By Parity II.
    # Memory Usage: 17.8 MB, less than 8.70% of Python3 online submissions for Sort Array By Parity II.
    # NEW - used Indexing
    # Runtime: 208 ms, faster than 98.17% of Python3 online submissions for Sort Array By Parity II.
    # Memory Usage: 16.5 MB, less than 8.70% of Python3 online submissions for Sort Array By Parity II.

    # Problem 20
    # 1002. Find Common Characters
    A = ["cool","lock","cook"]
    commonChars(A)
    #     Runtime: 44 ms, faster than 78.74% of Python3 online submissions for Find Common Characters.
    # Memory Usage: 13.7 MB, less than 5.55% of Python3 online submissions for Find Common Characters.

