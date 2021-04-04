# 1 -- Reverse a list in place
ls = [33, 44, 52, 3, 2, 311,11]
print(ls)

# Inbuilt Method to do this
# print(ls.reverse())
# print(ls)


# Using Indices
left = 0
right = len(ls) - 1
while left < right:
    ls[left], ls[right] = ls[right], ls[left]
    left += 1
    right -= 1

print(ls)

# *************************************************************************************************
# 2 Check if string is palindrome
strs = "MADAM"
print(strs)
# Pythonic Solution
print(strs[::-1] == strs)

# Using Indexes
left = 0
right = len(strs) - 1
while left <= right:
    if strs[left] != strs[right]:
        print(False)
        break
    left += 1
    right -= 1
else:
    print(True)


# *************************************************************************************************
# 3 reverse an Integer

num = 1234112233445566
# res = 4321
# pyhtonic
print(int(str(num)[::-1]))

# Using Maths
res = 0

while num > 0:
    res = res * 10 + num % 10
    num = num // 10

print(res)


# *************************************************************************************************
# 4 ANAGRAM -- restful vs fluster

def is_anagram(str1, str2):
     if len(str1) != len(str2):
         return False

    # pythonnic
    #  print(''.join(sorted(str1)) == ''.join(sorted(str2)))
     for x, y in zip(sorted(str1), sorted(str2)):
         if x != y:
             return False
     return True

print(is_anagram('restful', 'fluster'))


# *************************************************************************************************
# 5 Duplicate in array

ls = [33, 44, 55, 66, 33]
def find_duplicates(ls):
    store_res = set()
    for data in ls:
        if data not in store_res:
            store_res.add(data)
        else:
            return data
    return "404 Duplicate Not Found"

print(find_duplicates(ls))

