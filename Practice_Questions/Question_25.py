"""
Write a program to print the following pattern:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

"""
if you are printing the j value 
and suppose you didn't get the correct output
then instead of increasing the value of i just reduce it as like 
instead of going from 1 to 5 you can go from 5 to 1 and then print the j value from 1 to i
and keep in mind the loop goes from 1 to i+1 because the range function is exclusive of the last value
"""