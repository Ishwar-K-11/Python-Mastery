"""
1.split()
Definition:
Splits a string into a list using the specified separator.
If no separator is given, it splits at whitespace.

Syntax:
string.split(separator)

"""
text = "Python is Best Programming Language"
lsit = text.split()   # By default it split the text into list where space is there
print(lsit)

print(list(text))   # spliting each and every character of the text

lsit2 = text.split("o")
print(lsit2)


"""
Definition:
Joins the elements of a list (or any iterable) into a single string
using the specified separator.

Syntax:
separator.join(iterable)
"""

my_list = ["a", "p", "p","l","e"]
print(" ".join(my_list))
print("".join(my_list))


my_list2 = ["a", "p", "p","l","e",5]
#print("".join(my_list2))    # throws error because the int is present in the list

ans ="".join(str(ch) for ch in my_list2)
print(ans)



# Reverse the following Sentence 
#Ishwar is a good coder in python language

text = "Ishwar is a good coder in python language"

word_list = text.split()
word_list = word_list[::-1]
print(word_list)
print(" ".join(word_list))
