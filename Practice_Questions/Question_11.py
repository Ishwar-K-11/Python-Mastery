# Take a Person age and wather they have valid ID(True/False) as input.They can enter a venue only if they are 18 or older.
# AND have a valid ID. Print the appropriate message.

age = int(input("Enter your age: "))
valid_id = input("Do you have a valid ID? (True/False): ")

if age >= 18 and valid_id == "True":
    print("You can enter the venue.")
else:
    print("You cannot enter the venue.")
