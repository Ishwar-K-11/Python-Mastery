"""
World Capitals
    Create a dictionary contais five country and their capitals as a key and value
    iterate through this dictionary using the items() methods and print each in format country --> Capital

"""

count = {
    "India" : "New Delhi",
    "France" : "Paris",
    "Japan" : "Tokyo",
    "Brazil" : "Brasilla",
    "Australia" : "Canberra"
}

for lists in count.items():
    print(f"{lists[0]} --> {lists[1]}")