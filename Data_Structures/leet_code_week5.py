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

@sweet_formatting("HARD", "273 - Integers to English Words")
def numberToWords(num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n//10-2]] + words(n%10)
        if n < 1000:
            return [to19[n//100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n//1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'

@sweet_formatting("SUNIL","")
def shunil():
    print("Type any number here : ")
    user_input = input()
    while not(user_input.isdigit()):
        print("only number are allowed ")
        print("type any number here : ")
        user_input=input()
    ones = {"0":" ","1":"one ","2":"two ","3":"three ","4":"four ","5":"five ","6":"six ",
    "7":"seven ","8":"eight ","9":"nine "}
    tens={"0":"ten ","1":"eleven ","2":"twelve ","3":"thirteen ","4":"fourteen ",
    "5":"fifteen ","6":"sixteen ","7":"seventeen ","8":"eighteen ","9":"nineteen "}
    tens_2={"0":" ","2":"twenty ","3":"thirty ","4":"forty ","5":"fifty "
    ,"6":"sixty ","7":"seventy ","8":"eighty ","9":"ninety "}
    hundred ={"0":" ","1":"one hundred ","2":"two hundred ","3":"three hundred ",
    "4":"four hundred ","5":"five hundred ","6":"six hundred ","7":"seven hundred ",
    "8":"eight hundred ","9":"nine hundred "}
    comma_word = {"3":"thousand ","6":"million ","9":"billion "}

    container = " "
    copy_input = user_input
    index_switch = len(user_input)
    comma_switch = 3
    while index_switch>0:
        if user_input=="0":
            container = "zero"
            break
        if copy_input[index_switch-2]=="1":
            for digit in tens:
                if copy_input[index_switch-1]==digit:
                    container=tens[digit] + container
        else:
            for digit_1 in ones:
                if copy_input[index_switch-1]==digit_1:
                    container=ones[digit_1]+container
            if index_switch>1:
                for digit_2 in tens_2:
                    if copy_input[index_switch-2]==digit_2:
                        container=tens_2[digit_2]+container
        if index_switch>2:
            for digit_3 in hundred:
                if copy_input[index_switch-3]==digit_3:
                    container = hundred[digit_3]+container
        if index_switch>3:
            container = comma_word[str(comma_switch)]+container
        comma_switch=comma_switch+3
        index_switch=index_switch-3

    print(container)

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


    # just adding some easy questions here, WEEK 6 - 27th April 2020 - 03rd May 2020
    
    # 1309. Decrypt String from Alphabet to Integer Mapping
    # Runtime: 20 ms, faster than 98.12% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    # Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    # NICE BOI 

    # 1374. Generate a String With Characters That Have Odd Counts
    # Runtime: 28 ms, faster than 67.23% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
    # Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.


    # 557. Reverse Words in a String III
    # Runtime: 28 ms, faster than 89.84% of Python3 online submissions for Reverse Words in a String III.
    # Memory Usage: 14.3 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.

    # 929. Unique Email Addresses
    #Runtime: 40 ms, faster than 98.11% of Python3 online submissions for Unique Email Addresses.
    # Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Unique Email Addresses.

    # 657. Robot Return to Origin
    # Runtime: 60 ms, faster than 58.78% of Python3 online submissions for Robot Return to Origin.
    # Memory Usage: 13.9 MB, less than 6.90% of Python3 online submissions for Robot Return to Origin.

    # 824. Goat Latin
    # Runtime: 24 ms, faster than 90.41% of Python3 online submissions for Goat Latin.
    # Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Goat Latin.

    # 917. Reverse Only Letters
    # Runtime: 24 ms, faster than 92.69% of Python3 online submissions for Reverse Only Letters.
    # Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Reverse Only Letters.

    # 1417. Reformat The String
    # Runtime: 48 ms, faster than 74.09% of Python3 online submissions for Reformat The String.
    # Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Reformat The String.    

    # 11. Container With Most Water -- Medium -- O(n)
    # Runtime: 128 ms, faster than 77.46% of Python3 online submissions for Container With Most Water.
    # Memory Usage: 15.3 MB, less than 5.26% of Python3 online submissions for Container With Most Water.

    # 1431. Kids With the Greatest Number of Candies - VEry Easy
    # Runtime: 36 ms, faster than 78.44% of Python3 online submissions for Kids With the Greatest Number of Candies.
    # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.

    
    # 167. Two Sum II - Input array is sorted
    # Runtime: 60 ms, faster than 87.02% of Python3 online submissions for Two Sum II - Input array is sorted.
    # Memory Usage: 14.2 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.


    # 14-05-2020 : 10:10 PM
    # 125. Valid Palindrome
    # Runtime: 36 ms, faster than 94.65% of Python3 online submissions for Valid Palindrome.
    # Memory Usage: 15.2 MB, less than 9.52% of Python3 online submissions for Valid Palindrome.

    # 16-05-2020
    # 916. Word Subsets
    # Runtime: 628 ms, faster than 90.14% of Python3 online submissions for Word Subsets.
    # Memory Usage: 17.5 MB, less than 50.00% of Python3 online submissions for Word Subsets.


    numberToWords(1234567891)
    shunil()
