# Permutation means to find the "NO OF WAYS" to arrange a given set/num/str
# here the order does matter and is consider a unique permutation... ABC, BCA, ACB are all acceptable
# Example -- You do a permutation when you want to crack a password


# COMBINATION is to combine
# That means we order doesn't matter and ABC, BCA, ACB meant the same thing as ABC is present in all of them
# Example -

# http://www.pythontutor.com/visualize.html#mode=display
from itertools import permutations
from itertools import combinations
inp = ["A", "B", "C"]

# print(set(permutations(inp, 3)))
# print(list(combinations(inp, 2)))


def permutation_rec(inp):
    result = []

    if len(inp) == 0:
        result = [inp]

    for i, num in enumerate(inp):
        for prem in permutation_rec(inp[:i] + inp[i+1:]):
            result += [num + prem]

    return result


print(permutation_rec("abcd"))

def adjacent(ls):
    size = len(ls)
    left = 0
    right = 1
    max_len = float('-inf')
    while right < size:
        max_len = max(max_len, ls[left] * ls[right])
        left += 1
        right += 1

    return max_len


print(adjacent([4, 10, 3, -4, -5, 3]))


def beautiful_array(ls):

    if len(ls) < 2:
        return ls

    left = 0
    right = len(ls) - 1

    while left < right:
        if ls[left] == ls[right]:
            if left == right:
                return [ls[left]]
            return ls[left:right+1]
        else:
            left += 1
            right -= 1

    return []

print(beautiful_array([3, 4, 5, 7, 4, 1]))
print(beautiful_array([3, 2, 5, 7, 4, 1]))
print(beautiful_array([3]))
print(beautiful_array([3, 1]))
print(beautiful_array([3, 3]))

