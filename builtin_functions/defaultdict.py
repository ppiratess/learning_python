from collections import defaultdict


# letters = {}

# for letter in "Mississippi":
#     if letter not in letters:
#         letters[letter] = 1

#     else:
#         letters[letter] += 1

# print(letters)


# ? solution using default dict
letters = defaultdict(int)

for letter in "Mississippi":
    letters[letter] += 1

print(letters)
