"""
Given a list of numbers, write python code using a loop to find and print the largest element. Do not use the build in max() function.
"""

nums = [3,6,9,1,9,22,4,8,7,11]

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print("The largesr Number from the list is: ",largest)