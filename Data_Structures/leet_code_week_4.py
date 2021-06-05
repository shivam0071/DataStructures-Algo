import time
import collections

print("Week 4 \nDate 06/04/2020 - 12/04/2020")


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


@sweet_formatting("o(N)", "1189. EASY")
def maxNumberOfBalloons(text):
    count = collections.Counter(text)
    minimum = count.get('b', 0)
    minimum = min(minimum, count.get('a', 0))
    minimum = min(minimum, count.get('l', 0) // 2)
    minimum = min(minimum, count.get('o', 0) // 2)
    minimum = min(minimum, count.get('n', 0))

    return minimum


@sweet_formatting("Still Incorrect", ":(")
def reverseInParentheses(inp):
    # "foo(bar(baz))blim(data)"
    loop = 0
    output = ''
    while loop < len(inp):
        data = []
        # print(f"LOOP - {loop}, Inp - {inp[loop]}")
        if inp[loop] == '(':
            data.append(inp[loop])  # "("
            while True:
                loop += 1
                # print(f"LOOP - {loop}, Inp - {inp[loop]}")
                if inp[loop] == ')':
                    break
                elif inp[loop] == '(':
                    data.append(inp[loop])
                else:
                    data.append(inp[loop])
            # print(f"data {data}, output - {output}")
            sub_str = ''
            while data:
                sub_data = data.pop()
                if sub_data == "(" and len(data) == 0:
                    break
                elif sub_data == "(":
                    data.extend(sub_str)
                    sub_str = ''
                    # print(data, len(data))
                else:
                    # print(f"LEN - {len(data)} ")
                    sub_str += sub_data
                # print(f"sub_str -- {sub_str}")
            output += sub_str
            # print(f"NEW output - {output}")

        elif inp[loop] == ')':
            pass
        else:
            output += inp[loop]
            # print(output)
        loop += 1

    return output


@sweet_formatting("Very Smart , O(n) Time and space complexity ", "Code Signal, Hash Tables")
def containsCloseNums(nums, k):
    # nums = [0, 1, 2, 3, 5, 2,.,.,2]
    # k = 3
    data = {}
    for idx, ele in enumerate(nums):
        if ele not in data:
            data.update({ele: idx + k})
        elif data[ele] >= idx:
            return True
        else:
            data.update({ele: idx + k})
    return False


@sweet_formatting("Medium", "55. Jump Game")
def canJump(nums):
    """We will iterate from the backwards and see if we can reach the end from the begin"""
    # [2,3,1,1,4]
    last_valid_index = len(nums) - 1  # We have to reach the last element
    for idx in range(len(nums) - 1, -1, -1):
        print(f"IDX - {idx}, SUM - {idx + nums[idx]}, LAST INX - {last_valid_index}")
        if idx + nums[idx] >= last_valid_index:  # greater because a 4 can make jumps 4,3,2,1
            last_valid_index = idx
            print(last_valid_index)

    return last_valid_index == 0


@sweet_formatting("Constant Time, USing string in hash sets", "")
def isValidSudoku(board):
    seen = set()
    for i in range(len(board)):
        for j in range(len(board)):
            current_val = board[i][j]
            if current_val != '.':
                if current_val + " is in row " + str(i) not in seen and current_val + " is in column " + str(
                        j) not in seen and current_val + " is in box " + str(i // 3) + "-" + str(j // 3) not in seen:
                    seen.add(current_val + " is in row " + str(i))
                    seen.add(current_val + " is in column " + str(j))
                    seen.add(current_val + " is in box " + str(i // 3) + "-" + str(j // 3))

                else:
                    return False

    return True


@sweet_formatting("EASY", "")
def distributeCandies(candies: int, num_people: int):
    output = [0] * num_people
    counter = 0
    while candies > 0:
        counter += 1
        temp = candies
        candies -= counter
        if candies > 0:
            if counter % num_people == 0:
                output[num_people - 1] += counter
            else:
                output[counter % num_people - 1] += counter
        else:
            if counter % num_people == 0:
                output[num_people - 1] += temp
            else:
                output[counter % num_people - 1] += temp

    print(output)
    return output


@sweet_formatting("EASY, Better way", "")
def distributeCandies_2(candies: int, num_people: int):
    # output = [0] * num_people
    # counter = 0
    # i = 0
    # while candies > 0:
    #     counter += 1
    #     temp = candies
    #     candies -= counter
    #     if i == num_people:
    #         i = 0
    #     if candies > 0:
    #         output[i] += counter
    #     else:
    #         output[i] += temp
    #     i += 1
    # print(output)
    # return output
    out = [0] * num_people
    counter = 0
    while candies > 0:
        out[counter % num_people] += min(candies, counter + 1)
        candies -= counter + 1
        counter += 1
    print(out)


@sweet_formatting("Sliding window O(n)", "3. Medium")
def lengthOfLongestSubstring(s: str):
    # "abcabcbb"
    left = 0
    right = 0
    max_s = 0
    hash_set = set()
    while right < len(s):
        if s[right] not in hash_set:
            hash_set.add(s[right])
            right += 1
            max_s = max(len(hash_set), max_s)
        else:
            hash_set.remove(s[left])
            left += 1
    print(max_s)


def some_ques():
    input = "219"
    if input[0] == '0' or input is None:
        return 0

    left, right = 1, 1
    for i in range(1, len(input)):
        if input[i] == '0':
            left = 0
        if input[i - 1] == '1' or (input[i - 1] == '2' and input[i] <= '6'):
            left += right  # 2
            right = left - right  # 1
        else:
            right = left

    print(left)
    return left


def productExceptSelf(nums):
    # [5, 2, 3, 4]
    LEFT = [1, 5, 10, 30]
    RIGHT = [24, 12, 4, 1]
    MERGE = [24, 60, 40, 30]


    track = 1
    n = len(nums)
    output = []
    import pdb
    pdb.set_trace()
    for i in range(0, n):
        output.append(track)
        track = track * nums[i]
    track = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * track
        track = track * nums[i]
    print(output)
    return output


if __name__ == "__main__":
    # problem 16 - EASY
    # 06/04/2020 11:36 PM
    # https: // leetcode.com / problems / maximum - number - of - balloons /
    # "Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible."
    # Input: text = "nlaebolko"
    # Output: 1
    text = "nlaebolko"
    text = "balloonballoon"
    maxNumberOfBalloons(text)
    # "Runtime: 24 ms, faster than 94.17% of Python3 online submissions for Maximum Number of Balloons.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons."

    # Code Signal - reverse in paranthesis
    # "Write a function that reverses characters in (possibly nested) parentheses in the input string.
    # Input strings will always be well-formed with matching ()s."
    inp = "foo(bar(baz))blim(data)"
    reverseInParentheses(inp)
    # Testcases FAILED

    # Problem 17 80/04/2020 12:49 PM
    # "Given an array of integers nums and an integer k, determine whether there are two distinct indices
    # i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than
    # or equal to k."
    # "For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
    # containsCloseNums(nums, k) = true.
    # There are two 2s in nums, and the absolute difference between their positions is exactly 3."
    # nums = [0, 1, 2, 3, 5, 2]
    nums = [1, 0, 1, 1]
    k = 1
    # k = 3
    containsCloseNums(nums, k)
    # ACC

    # Problem 18 08/04/2020
    # Leet Code 55
    # "Given an array of non-negative integers, you are initially positioned at the first index of the array.

    # Each element in the array represents your maximum jump length at that position.
    #
    # Determine if you are able to reach the last index.
    #
    # Example 1:
    #
    # Input: [2,3,1,1,4]
    # Output: true
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index."
    ls = [2, 0, 0]
    canJump(ls)
    # "Runtime: 80 ms, faster than 98.36% of Python3 online submissions for Jump Game.
    # Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Jump Game."

    # problem 19
    # 36.Valid Sudoku
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    isValidSudoku(board)
    # "Runtime: 104 ms, faster than 35.37% of Python3 online submissions for Valid Sudoku.
    # Memory Usage: 13.6 MB, less than 5.88% of Python3 online submissions for Valid Sudoku."

    # problem 20
    # Problem 1103 EASY
    # "Input: candies = 7, num_people = 4
    # Output: [1,2,3,1]
    # Explanation:
    # On the first turn, ans[0] += 1, and the array is [1,0,0,0].
    # On the second turn, ans[1] += 2, and the array is [1,2,0,0].
    # On the third turn, ans[2] += 3, and the array is [1,2,3,0].
    # On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1]."
    # candies = 7
    # num_people = 4
    candies = 10
    num_people = 3
    distributeCandies(candies, num_people)
    # "Runtime: 44 ms, faster than 20.55% of Python3 online submissions for Distribute Candies to People.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People."

    distributeCandies_2(candies, num_people)
    # Runtime: 40 ms, faster than 40.18% of Python3 online submissions for Distribute Candies to People.
    # Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.

    # Problem 21 11/04/2020 12:42 PM
    # 3. Longest Substring Without Repeating Characters
    # Input: "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.
    s = "pwwkew"
    lengthOfLongestSubstring(s)
    # Runtime: 72 ms, faster than 46.13% of Python3 online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.

    some_ques()

    productExceptSelf([5, 2, 3, 4])
