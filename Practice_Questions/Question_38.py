# Function with the returen statent
# Check weather the number is prime or Not and print True or False

def prim_e(num):
    count = 0
    for i in range(1,num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
print(prim_e(16))
