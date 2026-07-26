# Ask a number from the user and print the multiplication table upto 10.

num = int(input("Enter a number To print its table upto 10: "))
i = 1
while i<= 10:
    print(f"{num} X {i} = {num*i}")
    i += 1