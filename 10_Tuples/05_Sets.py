# Looping through the sets

fruits = {"Apple", "Mango", "Watermelon", "Banana"}

for a in fruits:
    print(a)

print()
for b, fruits in enumerate(fruits, start=1):
    print(f"{b}  {fruits}")