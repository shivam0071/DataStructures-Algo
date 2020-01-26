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
def looper():
  for idx, data in enumerate(ls):
    for idx2, d in enumerate(ls[idx+1:]):
      if data + d == target :
        print([idx, (idx + 1) + idx2])
        return [idx, (idx + 1) + idx2]
        # break

looper()

## BEST SOLUTION -- > MEMOIZATION ##
def twoSumBest(ls):
  h = {}
  for i, num in enumerate(ls):
    n = target - num
    if n not in h:
      h[num] = i
    else:
      return [h[n], i]
print(twoSumBest(ls))

# What have you learnt from this ?
#   1.) Observe if there is any maths involved
#   2.) Think if this can be memoized