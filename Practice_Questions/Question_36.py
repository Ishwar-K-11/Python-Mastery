def high(a,b,c):
    if a >= b and a >= c:
        print(f"{a} is Grater Number then {b} and {c}")
    elif b>=a and b>=c:
        print(f"{b} is grater then {a} and {c}")
    else: 
        print(f"{c} is grater then {a} and {b}")

num1,num2,num3 = map(int,input("Enter The Three Numbers: ").split())

high(num1,num2,num3)

