# Here we will learn to sort Via keys and values in lambda 

# You Get OutPut
#           [('english : 70),(hindi,80),('math',90),('Science:99)]
# Indexing        0       1     0    1      0    1       0     1


Marks = {"English" : 70, "Hindi" : 80, "Math" : 100, "Science":99 }

ans = sorted(Marks.items(), key= lambda x:x[1])
print(ans)

"""
ans = sorted(Marks.items(), key= lambda x:x[1])

so In the above line of code :
        -The sorted() - function try to sort the dictionary
        -The Marks.items takes out the key and its value 
        -key= lambda x:x[1] so here the indexing works in the lambda function and it treats x[1]
        -In the above x:x[0] it will sort the Dictionary according to the keys in the dict because keys got the index 0
"""


"""
answ = sorted(Marks.item(), key= lambda x:x[0])     It will sort according to the keys of the dictionary
print(answ)
"""

Mar = {
    "Akshay" : [70, 80, 30, 60, 75],
    "Kartik" : [55, 65, 87, 85, 77],
    "Jack" : [97, 77, 55, 87, 66],
    "Ishu" : [98, 76, 79, 87, 77]
}





