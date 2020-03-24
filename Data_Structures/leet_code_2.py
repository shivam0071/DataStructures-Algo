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


