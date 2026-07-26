# Q - Create a tuple of 5 movie names and using indexing print frist, middle and last name

movie_name = ("Thor", "Iron Man", "Spider Man", "Hulk", "Ant man")
print(movie_name[0])
print(movie_name[2])
print(movie_name[4])

# Q Create a tuple of 8 numbers using slicing print the frist 3, last 3 and alternate 

nums =(10,20,44,54,1,23,98,54)
print(nums[:3])
print(nums[5:8])
print(nums[0:7:2]) 



# Q Create a list of marks of 6 students and print the highest, Lowest and avg of marks without using the methods

marks = (78, 92, 65, 88, 74, 95)

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total = total + mark

average = total / len(marks)

print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)



# Take 5 numbers as input from the user store them as a tuple and print min and max of that tuple

print()
print()

numbers = ()
print("Enter a five Numbers")
for i in range(5):
    num = int(input(f"Enter a {i+1} Number: "))
    numbers = numbers + (num,)

high = numbers[0]
low = numbers[0]

for num in numbers:
    if num > high:
        high = num

    if num < low:
        low = num

print("Numbers:", numbers)
print("Highest Number:", high)
print("Lowest Number:", low)






