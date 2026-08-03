def Sum(x, y):
    return x + y


c = Sum(10, 15)  # What is the we passes the string instead of integers
print(c)


def sum_1(z:int,i:int) ->int :
    return z + i

d = sum_1(10,89)
print(d)



# If you are passing list and inside list the integers are there then the type annotations becomes in following way
def list_1(lst:list[int]) ->int:
    return max(lst)

h = list_1([10,20,30,50,9,6])
print(h)