letters = {}

for letter in "Mississippi":
    if letter not in letters:
        letters[letter] = 1

    else:
        letters[letter] += 1

print(letters)
