# code to re raise the exception

def age_check():
    try:
        age = int(input("Enter The age of the person: "))
        if age < 0:
            print("The age cannot be negative")
        elif age >=150:
            print("The age is not real")

    except ValueError as e:
        print(f"Inside function error: {e}")
        raise

    except Exception as e:     # This statement defines that if the any other exception occurs rather then the ValueError catch it
        print(e)

try:
    age_check()

except Exception as e:
    print(f"The out Side Error: {e}")

else:
    print("The code get execuate")


"""
understanding the code and cencept:
We have use exception handling inside the function and outside the function both are independent until and unlesss you
write the raise keyword inside the except which is inside the function
By writing raise keyword under the block of except the outside exception and inside excpetion handling mechanism gets connect to each other
"""
