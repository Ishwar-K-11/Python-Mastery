# Take a Year as input. Check if it is a leap year. A Year is a leap year if it is divisible by 4
# but not by 100, unless it is also divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
