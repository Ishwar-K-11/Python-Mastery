# Check if the list is sorted

list1 = list(map(int,input("Enter the list numbers(Space Seperated): ").split()))

sorted_list = True

for i in range(len(list1)-1):
    if list1[i] > list1[i+1]:
        sorted_list = False
        break

if sorted_list:
    print("The list is sorted")
else:
    print("The list is not sorted")