
# #Write a Python program that prints "Hello, World!"
# print("Hello, World!!")

# #Set up Python on your local machine and write a program to display your name.
# print("My name is margi")

# #Write a Python program to demonstrate the creation of variables and different data types.
# age = 23
# print("My age is:",age)
# surname = "patel"
# print("my surname is:",surname)

# # How to take user input using the input() function. 
# name = input("Enter Your Name:")
# age = input("enter your Age:")

# print("Hello!!",name)
# print("You are",age, "year old")

# # How to check the type of a variable dynamically using type(). 
# name = "margi"
# age = 23
# print("your name is:",type(name))
# print("your age id:",type(age))

# # Write a Python program to find greater and less than a number using if_else. 
# num1 = int(input("Enter a first number"))
# num2 = int(input("Enter a second number"))

# if num1 > num2:
#     print(f"{num1} is grater than {num2}")
# else:
#      print(f"{num1} is less than {num2}")

# # Write a Python program to check if a number is prime using if_else. 
# num = int(input("Enter a number: "))
# prime = True

# for i in range(2,num):
#     if(num%i == 0):
#         prime = False
#         break

# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not prime")


# #Write a Python program to calculate grades based on percentage using if-else ladder.
# percentage = int(input("Enter a percentage: "))

# if percentage >= 90:
#      print("Grade A")
# elif percentage >= 80:
#      print("Grade B")
# elif percentage >=70:
#      print("Grade C")
# elif percentage >= 60:
#      print("Grade D")
# else:
#      print("Fail....")


# #Write a Python program to check if a person is eligible to donate blood using a nested if.
# age = int(input("Enter your age: "))
# weghit = int(input("Enter your weghit: "))

# if age >= 18:
#     if weghit > 50:
#         print("You eligible for blood donate")
#     else:
#         print("you are not eligible for blood donate beacause low weghit")
# else:
#     print("You are not eligible for blood donate beacause of you are under 18")


# # Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango'] 
# list1 = ['apple','banana','mango']
# for i in list1:
#     print(i)


# # Write a Python program to find the length of each string in List1. 
# list1 = ["apple","banana","kiwi","mango"]
# for item in list1:
#     print(item,len(item))



# # Write a Python program to find a specific string in the list using a simple for loop and if condition.
# list = ['apple','banana','mango']
# search_item = input("Enter a fruit to search: ")

# flag = True

# for fruits in list:
#     if fruits == search_item:
#         print(f"{search_item},found in the list")
#         flag = True
#         break
# else:
#     print("Fruit is not found in the list")


# """
# Print this pattern using nested for loop: 
# markdown 
# Copy code 
# * 
# ** 
# *** 
# **** 
# *****
# """

# for i in range(0,5):
#     print("*" * (i+1))


# # Write a Python program to print "Hello" using a string. 
# print("Helloo...")

# # Write a Python program to allocate a string to a variable and print it. 
# name = "Hello, i am margi..."
# print(name)

# # Write a Python program to print a string using triple quotes. 
# name = """
#         Hello my name is margi
#         my subject is python
# """
# print(name)

# # Write a Python program to access the first character of a string using index value.
# name = "python"
# print(name[0])
# print(name.index("p"))

#  # Write a Python program to access the string from the second position onwards using slicing.
# name = "python"
# print(name[1:])

# # Write a Python program to access a string up to the fifth character
# name = "python programing"
# print(name[:5])

# # Write a Python program to print the substring between index values 1 and 4.
# name = "python programing"
# print(name[1:4])

#  # Write a Python program to print a string from the last character. 
# name = "python"
# print(name[::-1])

# # Write a Python program to print every alternate character from the string starting from index 1. 
# name = "python"
# print(name[1::2])

# #Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']
# List1 = ['apple', 'banana', 'mango']
# for fruit in List1:
#     if fruit == "banana":
#         continue
#     print(fruit)


# # Write a Python program to stop the loop once 'banana' is found using the break statement.
# List1 = ['apple', 'banana', 'mango']
# for fruit in List1:
#     if fruit == "banana":
#         break
#     print(fruit)


# #Write a Python program to demonstrate string slicing. 
# name = "margi patel"
# print(name[:2])
# print(name[2:5])


# #Write a Python program that manipulates and prints strings using various string methods. 
# name = input("Enter a name: ")
# print(len(name)) #length of name
# print(name.lower()) #name into lower case
# print(name.upper()) #name into upper case
# print(name.capitalize()) #name of first latter is capital only first string
# print(name.title()) #first latter capital boths words
# print(name.strip()) #stratings extra space remove
# print(name.replace("ma","na")) #replace with old to new 
# print(name.find("a")) #find name and answer index
# print(name.startswith("mar")) #find start a specific string than true
# print(name.endswith("patel")) #find end with spesific string
# print(name.split()) #space remove and convert into 2 differt words
# print(name.join("ja")) #join in some words
# print(name.isalpha()) #check if is character
# print(name.isdigit()) #check if is number
# print(name.isalnum()) #check if is number and charavter both in one
# print(name.zfill(7)) #before string 00 


