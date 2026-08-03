# Pass by Value

def pass_by_value(x):
    x = x + 100
    print(f"The inside Function is: {x}")

num = 99
pass_by_value(num)
print(f"The Outside Function: {num}")


#So when the immutable data type is there then by automatically python passes the value by pass by Value



# Pass By refrence

def pass_by_refrence(y):
    y.append(9987)
    print(f"The inside function is: {y}")

num2 = [10,20,30,40]
pass_by_refrence(num2)
print(f"The outside function :{num2}")

# As here you can see that the value is get passsed by the pass by refrence because of mutable data type
# if some one ask for the proof of it then print the id of the function 


# But if you want to make two functions seperate that is the inside one and the outside 

# But you have the mutable data tyoe then use the deep copy 