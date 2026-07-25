# Reverse a list without using any function 

def rev(lst):
    n = len(lst)
    new_lst = []
    for i in range(n-1,-1,-1):
        new_lst.append(lst[i])

    return new_lst

lst = list(map(int,input("Enter the list(space seperated): ").split()))
ans = rev(lst)
print(ans)