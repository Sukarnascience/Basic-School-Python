#1. No. of lines in a file starting with a or A.
#2. Simple interest function with default argument.
#3. Random numbers from 1 to 6
#4. String palindrome
#5. Fibonacci series
#6. Bubble sort
#7. no. of vowels present in the text file
#8. Count no. of 'do' and 'Do'
#9. Binary search
#10. CSV file - read & write
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

#6 

randomlist = [15,6,42,5,46,11,1,4,33,52,22,2]
print("our list of no. are: ",randomlist)
for i in range(len(randomlist)):
    for j in range(0,len(randomlist)-i-1):
        if(randomlist[j]>randomlist[j+1]):
            randomlist[j],randomlist[j+1]=randomlist[j+1],randomlist[j]
print("after bubble sorting :",randomlist)

# OUTPUT:-
# our list of no. are:  [15, 6, 42, 5, 46, 11, 1, 4, 33, 52, 22, 2]
# after bubble sorting : [1, 2, 4, 5, 6, 11, 15, 22, 33, 42, 46, 52]

#7

'''
Create a text file named as 'data.txt' in that write:-
A man is a man.
if you not then you should be.
a big personality was also a human.
'''

ourFile = open("data.txt", "r")
data = ourFile.read()
count = 0
for i in data:
    if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
        count+=1
        
print("No. of Vowels present in a text file are :", count)
ourFile.close()

# other way to write if condition is:-
#   if(i in ('aAeEiIoOuU')):
#             or
#   if(i in ['a','A','e','E','i','I','o','O','u','U']):
# ................etc.
# there are multiple way to represent the same thing

# OUTPUT:-
# No. of Vowels present in a text file are : 27

#8

'''
Create a text file named as 'data.txt' in that write:-
Do every thing that you want to do
remeber one thing dont fall in troubble
Do this do that every thing
'''

myfile = open("data.txt",'r')
see = myfile.readlines()

do=Do=0

for i in see:
    seeMore = i.split()
    if("do" in seeMore):
        do += 1
    if("Do" in seeMore):
        Do += 1

print("no. of do is {} and no. of Do is {}".format(do,Do))

# OUTPUT:-
# no. of do is 2 and no. of Do is 2

#10
'''
Creat a CSV file and enter few data 
in my case it was :-
['Spoorthi', '17', '12-B', 'PCMB']
['Srinidhi', '17', '12-A', 'PCMC']
['Kalpana', '17', '12-A', 'PCMC']
['Ankita', '17', '12-A', 'PCMC']
['Uday', '17', '12-A', 'PCMC']
'''

import csv

def readingCSV(fileName,mode='a',i=0):
    data = open(fileName,'r')
    read = csv.reader(data)
    if(mode=='a'):
        for row in read:
            print(row)
    elif(mode=='p'):
        data=list(read)
        print(data[i])

def writeCSV(fileName,getData):
    data = open(fileName,'a')
    write = csv.writer(data)
    write.writerow(getData)
    data.close()
    
readingCSV("myData.csv")
# OUTPUT A:-
'''
['Spoorthi', '17', '12-B', 'PCMB']
['Srinidhi', '17', '12-A', 'PCMC']
['Kalpana', '17', '12-A', 'PCMC']
['Ankita', '17', '12-A', 'PCMC']
['Uday', '17', '12-A', 'PCMC']
'''

readingCSV("myData.csv",'p',2)
# OUTPUT B:-
# ['Kalpana', '17', '12-A', 'PCMC']

writeCSV("myData.csv",["Bhageashree","17","12-A","PCMC"])
# OUTPUT C:- The changes has been Dond so to see it has done or not so we will use readingCSV() function
readingCSV("myData.csv")
'''
['Spoorthi', '17', '12-B', 'PCMB']
['Srinidhi', '17', '12-A', 'PCMC']
['Kalpana', '17', '12-A', 'PCMC']
['Ankita', '17', '12-A', 'PCMC']
['Uday', '17', '12-A', 'PCMC']
['Bhageashree', '17', '12-A', 'PCMC']
You can see it has added
'''
