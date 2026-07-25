Amount = int(input("Enter the Purchase Amount: "))

if Amount > 5000:
    discount = Amount * 0.20
    total_amount = Amount - discount
    print(f"Discount: {discount}")
    print(f"Total Amount To Be Paid: {total_amount}")
elif Amount > 2000:
    discount = Amount * 0.10
    total_amount = Amount - discount
    print(f"Discount: {discount}")
    print(f"Total Amount To Be Paid: {total_amount}")
elif Amount > 1000:
    discount = Amount * 0.05
    total_amount = Amount - discount
    print(f"Discount: {discount}")
    print(f"Total Amount To Be Paid: {total_amount}")
else:
    print("No Discount Applicable")
    print(f"Total Amount To Be Paid: {Amount}")