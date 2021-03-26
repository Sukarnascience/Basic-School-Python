'''
Some of the Common asked Question:-
1. Count no. of lines start with 'A' ~ 
2. Binary file using the pickle module 
3. stack code using the list ~
4. factorial ~
5. python and MySQL interface code ~
6. bubble short ~
7. random dice ~
'''

# 1st Q.
myfileName = "myData.txt"
myFile = open(myfileName)
allLines = myFile.readlines()
count = 0
for i in allLines:
    if(i[0]=='A'):
        count += 1
print("No. of times we found 'A' in {} file are : {}".format(myfileName,count))

# 2nd Q.
import pickle

data1 = {"first name":"Sukarna","last name":"Jana","dob":"19/09/2003"}
data2 = {"first name":"Spoorthi","last name":"S","dob":"05/08/2003"}
final_data = {}
final_data["data1"]=data1
final_data["data2"]=data2
binaryFile = open("myDataFile",'ab')
pickle.dump(final_data,binaryFile)
binaryFile.close()
binaryFile = open("myDataFile","rb")
outdata = pickle.load(binaryFile)
print(outdata["data1"])
print(outdata["data2"]["dob"])

# 3rd Q.
top = None

def isEmpty(stack):
    if(stack==[]):
        return True
    else:
        return False

def Push(stack,item):
    stack.append(item)
    top = len(stack)-1

def Pop(stack):
    if(isEmpty(stack)):
        return("UnderFlow")
    else:
        item = stack.pop()
        if(len(stack)==0):
            top = None
        else:
            top = len(stack)-1
        return item

def Peek(stack):
    if(isEmpty(stack)):
        return "UnderFlow"
    else:
        top = len(stack)-1
        return stack[top]

def Display(stack):
    if(isEmpty(stack)):
        print("Stack is Empty")
    else:
        top = len(stack)-1
        print("{} <- Top".format(stack[top]))
        for i in range(-2,-len(stack)-1,-1):
            print(stack[i])

stack = [23,5,6,4,56,3,2,344,55,6,5,345,456,7,56,56,78,67]

while True:
    print("Stack Operation :-")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. exit")
    c = int(input(" Your choice"))
    if(c == 1):
        item = int(input("Your Input :"))
        print(Push(stack,item))
    elif(c == 2):
        print(Pop(stack))
    elif(c == 3):
        print(Peek(stack))
    elif(c == 4):
        Display(stack)
    elif(c == 5):
        print("Bye...")
        break

# 4th Q.
def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

user = int(input("Factorial of :"))
print(factorial(user))

# 5th Q.
import mysql.connector as myDB

dataBase = myDB.connect(host="localhost",user="root",passwd="jana1234",database="school")
if(dataBase.is_connected()):
    print("Connected Successfully")
else:
    print("Ooops.. fail to connect")

cs = dataBase.cursor()
# fetching the data in different type
cs.execute("select * from ledger;")
# use of fecthmany() function
datamany = cs.fetchmany(3)
for i in datamany:
    print(i)
# use of fetchone() function 
onedata = cs.fetchone()
print(onedata)
onedata = cs.fetchone()
print(onedata)
row = cs.fetchone()
while row is not None:
    print(row)
    row = cs.fetchone()
# use of fetchall() function
data = cs.fetchall()
for i in data:
    print(i)
# use of rowcount
rowcountdata = cs.rowcount
print(rowcountdata)
# insert a data now
data1,data2="MainPage","test1234"
cs.execute("insert into account values('{}','{}')".format(data1,data2))
dataBase.commit()
dataBase.close()

# 6th Q.
randomList = [23,5,6,4,56,3,2,344,55,6,5,345,456,7,56,56,78,67]
print("the random list is :{}".format(randomList))
for i in range(len(randomList)):
    for j in range(0,len(randomList)-i-1):
        if(randomList[j]>randomList[j+1]):
            randomList[j],randomList[j+1]=randomList[j+1],randomList[j]
print("Sorted the list is:{}".format(randomList))

# 7th Q.
import random

print("Random Dice Game")
print("If user gess the correct no. between 1~6 then user gets a point\n 5 chance")
userScore = 0
comScore = 0
chance = 1
while chance<=5:
    com = random.randint(1,6)
    user = int(input("Enter your random no. from 1~6 :"))
    if(com==user):
        print("great...")
        userScore += 1
    else:
        print("Oops!...")
        comScore += 1 
    chance += 1
if(comScore>userScore):
    print("computer wins the match...")
elif(comScore<userScore):
    print("user wins the match...")
else:
    print("match tie")
