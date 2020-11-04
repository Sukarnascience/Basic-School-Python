# Temperature Conversion based on choice 
# 1. Fahrenheit to Celsius
# or
# 2. Celsius to Fahrenheit

a = int(input('''What to convert:-
1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
which one [1]/[2]:- '''))

if(a==1):
    x = float(input("Enter Fahrenheit Value:-"))
    C = 1.8*(x-32)
    print("it's Celsius Value is:-",C)
else:
    y = float(input("Enter Celsius Value:-"))
    F = 1.8*y+32
    print("it's Fahrenheit Value is:-",F)
