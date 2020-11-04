# Write a program to provide a choice for arithmetic operations.
# To add => "+"
# To sub => "-"

a = input("What you want to do ADD or SUB")

if(a=='add'):
    x = float(input("Enter First Value:-"))
    y = float(input("Enter Second Value:-"))
    z = float(input("Enter Third Value:-"))
    r = x+y+z
    print(x,"+",y,"+",z,"=",r)
elif(a=='sub'):
    x = float(input("Enter First Value:-"))
    y = float(input("Enter Second Value:-"))
    z = float(input("Enter Third Value:-"))
    r = x-y-z
    print(x,"-",y,"-",z,"=",r)
else:
    print("Invalid Input")
