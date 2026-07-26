def discount_price(Original_Price,Discount):
    Disc = Discount / 100
    Total_Discount = Original_Price * Disc
    Total_Price = Original_Price - Total_Discount
    print(f"The total Discount Is : {Total_Discount}")
    print(f"The Total Price After Applying Discount Is : {Total_Price} ")

op = int(input("Enter the Original price: "))
dis = int(input("Enter the Discount in percentage: "))

discount_price(op,dis)
