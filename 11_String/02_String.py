# Vowels program 


text = "Python Programming"

total = 0

check = "aeiouAEIOU"

for i in range(0, len(text)):
    if text[i] in check:
        total += 1

print(total)


# progrm for Vowels in most effecirent way
total2 = 0
for ch in text.lower():
    if ch in "aeiou":
        total2 += 1

print(total2)





