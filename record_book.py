# Writer :- Sukarna Jana

#1. No. of lines in a file starting with a or A.
#2. Simple interest function with default argument.
#3. Random numbers from 1 to 6
#4. String palindrome
#5. Fibonacci series
#6. Bubble sort
#7. no. of vowels present in the text file
#8. Count no. of 'do' and 'Do'
#9. Binary search    - still not written
#10. CSV file - read & write
#11. Queue operation - still not written
#12. Stack operation - still not written
#Any 5 MySQL Query (it is not a part of a Python its MySQL)
#13.
#    A. -see below 
#    B. -see below 
#    C. -see below 
#    D. -see below 
#    E. -see below 
#14. Python and MySQL interface 

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

#14
# I have done in my way you can change according to you
# You can use function or not depends upon you

import mysql.connector as sql

login = sql.connect(host="localhost",user="root",passwd="janajana",database="school")

def create_table(tableName):
    typer = login.cursor()
    typer.execute("create table {} (name varchar(20) NOT NULL,RNo int,stream char(4));".format(tableName))
    login.commit()

def enter_in_table(tableName,data1,data2,data3):
    typer = login.cursor()
    typer.execute("INSERT INTO {} VALUES('{}',{},'{}');".format(tableName,data1,data2,data3))
    login.commit()

def search_by_name(tableName,name):
    typer = login.cursor()
    typer.execute("select * from {} where name = '{}';".format(tableName,name))
    print(typer.fetchall())
    
def see(tableName):
    typer = login.cursor()
    typer.execute("select * from {};".format(tableName))
    print(typer.fetchall())

# See according to your output
create_table('schoolBook')
enter_in_table('schoolBook','Sukarna Jana',29,'PCMC')
enter_in_table('schoolBook','friend',0,'-NA-')
see('schoolBook')
search_by_name('schoolBook','Sukarna Jana')

# OUTPUT:-
'''
1. Done but we cant see
2. Done but we cant see
3. Done but we cant see
4. [('Sukarna Jana', 29, 'PCMC'), ('friend', 0, '-NA-')]
5. [('Sukarna Jana', 29, 'PCMC')]
'''

# 13 MYSQL Query with output
'''
> start your mysql <

mysql> create database schoolwork;
Query OK, 1 row affected (0.41 sec)

mysql> use schoolwork
Database changed
mysql> create table report_book
    -> (id varchar(4),
    -> name varchar(20),
    -> class int NOT NULL,
    -> section char(1) NOT NULL,
    -> phoneNo int NULL,
    -> stream char(4) NOT NULL);
Query OK, 0 rows affected (4.18 sec)

mysql> desc report_book;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| id      | varchar(4)  | YES |      | NULL    |       |
| name    | varchar(20) | YES |      | NULL    |       |
| class   | int         | NO  |      | NULL    |       |
| section | char(1)     | NO  |      | NULL    |       |
| phoneNo | int         | YES |      | NULL    |       |
| stream  | char(4)     | NO  |      | NULL    |       |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.29 sec)

mysql> insert into report_book
    -> values("0AB4","sukarna jana",12,'A',0123456789,"PCMC");
Query OK, 1 row affected (0.44 sec)

mysql> select * from report_book;
+------+--------------+-------+---------+-----------+--------+
| id   | name         | class | section | phoneNo   | stream |
+------+--------------+-------+---------+-----------+--------+
| 0AB4 | sukarna jana |    12 | A       | 123456789 | PCMC   |
+------+--------------+-------+---------+-----------+--------+
1 row in set (0.00 sec)

mysql> insert into report_book
    -> values("1R2W","spoorthi s",12,'B',987654321,"PCMB"),
    -> ("8BA9","srinidhi",12,'A',753869421,"PCMC"),
    -> ("789A","ravi kumar",12,'C',376824109,"AEIB"),
    -> ("75BB","radika",12,'A',718293645,"PCMP");
Query OK, 4 rows affected (0.31 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from report_book;
+------+--------------+-------+---------+-----------+--------+
| id   | name         | class | section | phoneNo   | stream |
+------+--------------+-------+---------+-----------+--------+
| 0AB4 | sukarna jana |    12 | A       | 123456789 | PCMC   |
| 1R2W | spoorthi s   |    12 | B       | 987654321 | PCMB   |
| 8BA9 | srinidhi     |    12 | A       | 753869421 | PCMC   |
| 789A | ravi kumar   |    12 | C       | 376824109 | AEIB   |
| 75BB | radika       |    12 | A       | 718293645 | PCMP   |
+------+--------------+-------+---------+-----------+--------+
5 rows in set (0.00 sec)

mysql> select * from report_book where stream="PCMC";
+------+--------------+-------+---------+-----------+--------+
| id   | name         | class | section | phoneNo   | stream |
+------+--------------+-------+---------+-----------+--------+
| 0AB4 | sukarna jana |    12 | A       | 123456789 | PCMC   |
| 8BA9 | srinidhi     |    12 | A       | 753869421 | PCMC   |
+------+--------------+-------+---------+-----------+--------+
2 rows in set (0.00 sec)

mysql> update report_book set phoneNo=111188889 where name="srinidhi";
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from report_book;
+------+--------------+-------+---------+-----------+--------+
| id   | name         | class | section | phoneNo   | stream |
+------+--------------+-------+---------+-----------+--------+
| 0AB4 | sukarna jana |    12 | A       | 123456789 | PCMC   |
| 1R2W | spoorthi s   |    12 | B       | 987654321 | PCMB   |
| 8BA9 | srinidhi     |    12 | A       | 111188889 | PCMC   |
| 789A | ravi kumar   |    12 | C       | 376824109 | AEIB   |
| 75BB | radika       |    12 | A       | 718293645 | PCMP   |
+------+--------------+-------+---------+-----------+--------+
5 rows in set (0.00 sec)

mysql> select * from report_book where name like "s%";
+------+--------------+-------+---------+-----------+--------+
| id   | name         | class | section | phoneNo   | stream |
+------+--------------+-------+---------+-----------+--------+
| 0AB4 | sukarna jana |    12 | A       | 123456789 | PCMC   |
| 1R2W | spoorthi s   |    12 | B       | 987654321 | PCMB   |
| 8BA9 | srinidhi     |    12 | A       | 111188889 | PCMC   |
+------+--------------+-------+---------+-----------+--------+
3 rows in set (0.01 sec)

mysql> select count(*) from report_book where name like "s%";
+----------+
| count(*) |
+----------+
|        3 |
+----------+
1 row in set (0.02 sec)

mysql>
'''
