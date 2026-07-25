"""
Given a list of marks create a new list which contains only marks above 75% using the list comprenhension 

"""
marks = [10,78,98,54,67,45,37,99,77,81,82]
new_list = [nums for nums in marks if nums > 75]
print(new_list)
