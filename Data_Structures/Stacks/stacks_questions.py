# QUESTION 1
# 23/01/2020
# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/
#
# from collections import deque
#
# data = {"[":"]", "(":")", "{":"}"}
# stack = deque()
#
# for _ in range(int(input())):
#   stack.clear()
#   stack_inp = input()
#   if not (len(stack_inp) % 2 == 0):
#     print("NO")
#   else:
#     for bracket in stack_inp:
#       if bracket in data:
#         stack.append(bracket)
#       else:
#         if stack:
#           top_bracket = stack.pop()
#           if data[top_bracket] == bracket:
#             continue
#           else:
#             print("NO")
#             break
#     else:
#         if len(stack) == 0:
#           print("YES")
#         else:
#           print("NO")

# QUESTION 2 :
# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/staque-1-e790a29f/
from collections import deque
N, K = 10, 5
# N, K = map(int,input().split())
# ls = list(map(int,input().split()))
ls = [10,9,1,2,3,4,5,6,7,8]
sum_stack = sum(ls[:K])

for i in range(K-1,0 ,-1):
  if ls[-1] > ls[i]:
    print(ls[-1], ls[i], sum_stack)
    sum_stack = sum_stack + (ls.pop() - ls[i])
    print("New Sum",sum_stack)

print(sum_stack)