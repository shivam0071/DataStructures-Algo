# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/
# My Current best is
# 1.49 sec 6372 Kib
import array
end = "\n" + "*" * 20 + " {} " + "*" * 20 + "\n"

# if __name__ == "__main__":
# N = int(input())
# A = array.array('i', (map(int, input().split())))
# B = array.array('i', (map(int, input().split())))
# print(' '.join([str(sum(data)) for data in zip(A, B)]))
#
# def fastest():
#   N = int(input())
#   A = (int(item) for item in input().split())
#   B = (int(item) for item in input().split())
#   for _ in range(N):
#     print (next(A) + next(B), end = ' ')
#
# fastest()

# 18th Jan 2020 , 12:41
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
print(end.format("QUESTION 2"))
# test_cases = int(input())
# while test_cases > 0:
#   N,K = map(int,input().split())
#   A = tuple(map(int, input().split()))
#   if min(A) > K:
#     print(0)
#   else:
#     print(K - min(A))
#   test_cases -= 1

# Results : - Accepted
# Time(sec) - 3.41287
# Memory(KiB) - 19548


# ATTEMPT 2
# test_cases = int(input())
# while test_cases > 0:
#   N,K = map(int, input().split())
#   A = min(map(int, input().split())) # this has changed
#   if A > K:
#     print(0)
#   else:
#     print(K - A)
#   test_cases -= 1

# Time(sec) - 3.40075
# Memory(KiB) - 11460



# THE BEST ANSWER ON SITE
# for _ in range(int(input())): # <-- SO does this makes a difference? ...lets find out
#     n, k = map(int, input().split(' '))
#     l = min(map(int, input().split(' ')))
#     #sm = min(n_list)
#     if l < k: print(k - l)
#     else: print(0)
# RESULT
# Time(sec) - 3.29964
# Memory(KiB) - 11468
# Well not much...

# PROBLEM 3
# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/

inp = int(input())
data = tuple(map(int, input().split()))
relation = []
for idx, elem in enumerate(data):
  # print()
  for sub_idx in range(idx+1, len(data)):
    # print(elem, data[sub_idx], end = '||')
    if abs(elem - data[sub_idx]) == 1:
      # relation.append(sorted((elem, data[sub_idx])))
      print(elem, data[sub_idx], end = ' || ')
      # print(relation)