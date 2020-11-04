# Write a program to calculate the area of a circle, the perimeter of a circle based on choice

a = input('''What you want to do:-
1. Parimeter of Circle(in short PC)
2. Area of Circle(in short AC)
So, Which one [PC/AC]:-''')

if(a=="PC"):
    b = float(input("Radius:-"))
    c = 2*3.14*b
    print("Perimeter of the circle is ",c,"cm")
else:
    b = float(input("Radius:-"))
    d = 3.14*b**2
    print("Area of the circle is ",d,"cm")
