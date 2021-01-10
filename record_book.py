#1. No. of lines in a file starting with a or A.
#2. Simple interest function with default argument.
#3. Random numbers from 1 to 6
#4. String palindrome
#5. Fibonacci series
#6. Bubble sort
#7. no. of vowels present in the text file
#8. Count no. of 'do' and 'Do'
#9. Binary search
#10. CSV file -pop, read & write
#11. Queue operation
#12. Stack operation.

#1 ans
'''
Create a text file named as 'data.txt' in that write:-
A man is a man.
if you not then you should be.
a big personality was also a human.
'''

count = 0

myFile = open("data.txt",'r')
readFile = myFile.readlines()

for i in readFile:
    if(i[0] == 'a' or i[0] == 'A'):
        count += 1
        
print("the no of lines we have that starts with a or A are :",count)

# OUTPUT :-
# the no of lines we have that starts with a or A are : 2

#3

import random as r

def makeRandomNo():
    value = r.randint(1,6)
    return value

print("your random value 1 ~ 6 is :{}".format(makeRandomNo()))

# OUTPUT:-
# your random value 1 ~ 6 is :2

#2

def simpleInterest(P,T,R=20):
    SI = (P*R*T)/100
    return SI

print("simple interest of : P=100,R=_,T=5 is:",simpleInterest(100,5))
print("simple interest of : P=100,R=50,T=5 is:",simpleInterest(100,5,50))

# OUTPUT:-
# simple interest of : P=100,R=_,T=5 is: 100.0
# simple interest of : P=100,R=50,T=5 is: 250.0

#4

string = input("Enter your string :")

string2 = string[-1::-1]
if(string==string2):
    print("the string is palindrome")
else:
    print("the string is not a palindrome")

#or

string2=""

for i in range(-1,-len(string)-1,-1):
    string2=string2+string[i]

if(string==string2):
    print("the string is palindrome")
else:
    print("the string is not a palindrome")
    
# OUTPUT:-
# Enter your string :dfdf
# the string is not a palindrome
# the string is not a palindrome

#5

upto = int(input("upto where you want [n]:"))

a,b=0,1

print(a,b,end=" ")
for i in range(0,upto):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

# if you want to use while loop then this :-
print("\n")

i = 1
a,b=0,1
print(a,b,end=" ")
while i<=upto:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    i+=1
    
# OUTPUT:-
# upto where you want [n]:10
# 0 1 1 2 3 5 8 13 21 34 55 89 
# 0 1 1 2 3 5 8 13 21 34 55 89 
