#  Write a Python program to print “Hello, World!” on the screen
name = "Hello world"
print(f"{name}")

# Write a Python program to read a string, an integer, and a float from the keyboard and display them
name = input("Enter your name: .... ")
age = int(input("Enter your age:  .... " ))
height = float(input("Enter your height: .... "))
print("My name is : ",name)
print("My age is : ",age)
print("My height is : ",height)

# Write a Python program to open a file in write mode, write some text, and then close it. 
f = open("myfileexample.txt",'w')
f.write("\n Hello ")
f.write("\n Programmer ")
f.close()

# Write a Python program to create a file and print the string into the file
with open("file1.txt","w") as f:
    f.write("HELLOOO PROGRAMER")

# Write a Python program to read a file and print the data on the console
with open("myfileexample.txt","r") as f:
    print(f.read())

# Write a Python program to check the current position of the file cursor using tell()
with open("myfileexample.txt","r") as f:
    print(f.read(5))
    print(f.tell())

#  Write a Python program to handle exceptions in a calculator
try:
    num1 = int(input("Enter a num1 : "))
    num2 = int(input("Enter a num2 : "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print(f"No of sum is : {add}")
    print(f"No of sub is : {sub}")
    print(f"No of mul is : {mul}")
    print(f"No of div is : {div}")
except ValueError:
    print("Invalid value ")
except ZeroDivisionError:
    print("Can't devide by 0 ")

# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero)
# FileNotFound Exception
try:
    with open("demo.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("FILE NOT FOUND")

# Write a Python program to handle file exceptions and use the finally block for closing the file
try:
    with open("file1.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found . ")
finally:
    print("File is closed....")

# Write a Python program to print custom exceptions
class NegativeValueError(Exception):
    def __init__(self, message="value can't be negative"):
        self.message = message
        super().__init__(self.message)
    
def checkvalue ():
    num = int(input("Enter a number : "))
    if num < 0:
        raise NegativeValueError("Value negative")
    else:
        print(num)

try:
    checkvalue()
except NegativeValueError as e:
    print(f"Error : {e}")

#  Write a Python program to create a class and access the properties of the class using an object
class student:
    name = "margi"
    subject = "python"

obj = student()
print(obj.name)
print(obj.subject)

# Write a Python program to demonstrate the use of local and global variables in a class
global_var = "python"

class student:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    def display(self):
        local_variable = "Java"
        print(local_variable)

        global global_var
        print(global_var)

        print(f"{self.name}")
        print(f"{self.subject}")

obj = student("margi","PHP")
obj.display()

# Write a Python program to show single inheritance
class A:
    def displayA(self):
        print("CLASS A IS HERE")

class B(A):
    def displayB(self):
        print("CLASS B IS HERE")
    
obj = B()
obj.displayA()
obj.displayB()

# Write a Python program to show multilevel inheritance
class A:
    def displayA(self):
        print("CLASS A IS HERE")

class B:
    def displayB(self):
        print("CLASS B IS HERE")
    
class C(A,B):
    def displayC(self):
        print("CLASS C IS HERE")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

# Write a Python program to show multiple inheritance
class A:
    def displayA(self):
        print("CLASS A IS HERE")

class B(A):
    def displayB(self):
        print("CLASS B IS HERE")
    
class C(B):
    def displayC(self):
        print("CLASS C IS HERE")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

# Write a Python program to show hierarchical inheritance
class A:
    def displayA(self):
        print("CLASS A IS HERE")

class B(A):
    def displayB(self):
        print("CLASS B IS HERE")
    
class C(A):
    def displayC(self):
        print("CLASS C IS HERE")

b = B()
b.displayA()
b.displayB()

C = C()
C.displayA()
C.displayC()

# Write a Python program to show hybrid inheritance
class A:
    def displayA(self):
        print("CLASS A IS HERE")

class B(A):
    def displayB(self):
        print("CLASS B IS HERE")
    
class C(A):
    def displayC(self):
        print("CLASS C IS HERE")

class D(B):
    def displayD(self):
        print("CLASS D IS HERE")

d = D()
d.displayA()
d.displayB()
d.displayD()

c = C()
c.displayA()
c.displayC()

# Write a Python program to demonstrate the use of super() in inheritance
class A:
    def __init__(self):
        print("THIS IS A CONSTRUCTUR OF CLASS A")
    
    def displayA(self):
        print("THIS IS CLASS A")

class B(A):
    def __init__(self):
        super().__init__()
        print("THIS IS A CONSTRUCTUR OF CLASS B")
    
    def displayB(self):
        super().displayA()
        print("THIS IS CLASS B")
    
obj = B()
# obj.displayA()
obj.displayB()

# Write a Python program to show method overriding
class parent:
    def show1(self):
        print("This is a parent class method. ")

class child(parent):
    def show(self):
        print("This is child class method ")

p = parent()
c = child()
p.show1()
c.show()

#  Write a Python program to create a database and a table using SQLite3
#  Write a Python program to insert data into an SQLite3 database and fetch it
import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="",port=3306)

mycursor = mydb.cursor()

mycursor.execute("create database if not exists topsdb2 ")

mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="topsdb2")

mycursor = mydb.cursor()

mycursor.execute("""
                 create table if not exists student (
                 id int primary key auto_increment ,
                 name varchar(60) ,
                 email varchar(100))
                """)
mydb.commit()

def add_stud():
    name = input("Enter name : ")
    email = input("Enter email id :")

    values = (name,email)

    query = "insert into student (name,email) values (%s,%s)"

    mycursor.execute(query,values)
    mydb.commit()
    print("Data Inserted...!! ")

def view_stud():
    query = "select * from student"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        print(i)

while True:
    print("""
            Press 1 for ADD Student
            Press 2 f0r VIEW Students
""")
    try:
        choice = int(input("Enter your choice : "))

        if choice == 1:
            add_stud()
        elif choice == 2:
            view_stud()
        else:
            print("Invalid choice....")
            break
    except ValueError:
        print("Please Enter Number ...")
        

# Write a Python program to search for a word in a string using re.search().
import re

text = input("Enter a Sentence : ")
word = input("Enter word which word do you want to find? : ")

match = re.search(word,text)
if match:
    print(f"{word} found at position {match.start()}")
else:
    print("word not match")


# Write a Python program to match a word in a string using re.match()
import re
text = input("Enter a Sentence : ")
word = input("Enter word which word do you want to find? : ")

match = re.match(word,text)
if match:
    print(f"{word} matched at the beginning of the string")
else:
    print("Not matched at the beginning of the string")