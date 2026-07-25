# Given a list remove the duplicates from the list and return the list
def dupli(lst1):
    result = []
    for num in lst1:
          if num not in result:
              result.append(num)

    return result
          
lst1 = [10,20,30,40,20,55,78,49,55]
new = dupli(lst1)
print(new)


# Removing the elements from the list without creating the new one

def duplicate(lst1):
    i = 0

    while i < len(lst1):
        j = i + 1

        while j < len(lst1):
            if lst1[i] == lst1[j]:
                lst1.pop(j)
            else:
                j += 1
        i += 1

    return lst1

print(duplicate(lst1))