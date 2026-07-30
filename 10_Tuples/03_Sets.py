# Common sets Operation

sets_01 = {10, 20, 30, 40}


sets_01.add(100)  # Adds a single element
print(sets_01)


nums = {1000,2000}
sets_01.update(nums)  # Adds multiple elements
print(sets_01)

sets_01.remove(100)  # removes a single element
print(sets_01)

sets_01.discard(2000)  # removes a single element without an error
print(sets_01)

sets_01.pop()  # removes and return an element if the valuse is not given it will remove the last element bu default
print(sets_01)

sets_01.copy()  # creates a copy of the set
print(sets_01)

sets_01.clear()  # removes all element from the set
print(sets_01)


