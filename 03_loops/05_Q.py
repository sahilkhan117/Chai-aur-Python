# find first non repeated character

word = "teeter"

for c in word:
    if word.count(c) == 1:
        print(c, "is the non repeated word")
        break