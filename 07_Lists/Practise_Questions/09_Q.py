"""
Given a list You Have to seperate the odd and even elements my creating two seperate list of odd and even

"""


def odd_even(lst1):
    lst_odd =[]
    lst_even = []
    for num in lst1:
        if num % 2 == 0:
            lst_even.append(num)
        else:
            lst_odd.append(num)
    print("Odd List: ",lst_odd)
    print("Even List: ",lst_even)


lst1 = list(map(int,input("Enter the elements: ").split()))
odd_even(lst1)
