#Ask a Number from the user and print all its factors.

num = int(input("Enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1