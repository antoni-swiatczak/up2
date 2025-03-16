# 2025-03-02

# hello world
print ("Hello World")

# basics
print ("My first program")
price = 100
qty = 5
total = price*qty
print ("Total = ", total)

# if else
x = 5
if x > 10:
   print ("Answer")
   print ("True")
elif x < 10:
   print ("Answer")
   print ("False")
else:
   print ("Answer")
   print ("False")

amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

# Multi-Line Statements
a = 1
b = 2
total = a + \
        b
print (total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursdayś', 'Friday']
print (days)

# Quotations in Python
word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""
print (paragraph)

# Comments in Python
name = "Madisetti" # This is again comment
'''
This is a multiline
comment.
'''

# Podtrzymanie skryptu
#raw_input("\n\nPress the enter key to exit.")

# Multiple Statements on a Single Line
import sys; x = 'foo'; sys.stdout.write(x + '\n')

# Multiple Statement Groups as Suites
'''
if expression :
   suite
elif expression :
   suite
else :
   suite
'''

# Python Variables
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable

print (counter)
print (miles)
print (name)

# Deleting Python Variables
#del var1[,var2[,var3[....,varN]]]]
#del var
#del var_a, var_b
'''
counter = 100
print (counter)

del counter
print (counter)
'''
x = "Zara"
y =  10
z =  10.10

# Printing Variables Type
print(type(x))
print(type(y))
print(type(z))

# Casting Python Variables
x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )

# Case-Sensitivity of Python Variables
age = 20
Age = 30

print( "age =", age )
print( "Age =", Age )

# Multiple Assignment
a,b,c = 10,20,30
a=b=c=10
a,b,c = 1,2,"Zara Ali"
print (a,b,c)

# Function
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

# Numeric Data Types
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type
print (var4)

# String Data Types
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# List Data Type
print(type([2023, "Python", 3.11, 5+6j, 1.23E-4]))

# Python for Loop
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiouy':
      print (char, end='')

numbers = [34,54,67,21,78,97,45,44,80,19]
print(numbers[0])
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)

#range(start, stop, step)

for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])

#break

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")

var = '0'
while var.isnumeric() == True:
   var = "test"
   if var.isnumeric() == True:
      print ("Your input", var)
print ("End of while loop")
'''
var = 1
while var == 1 : # This constructs an infinite loop
   num = int(input("Enter a number :"))
   print ("You entered: ", num)
print ("Good bye!")
'''

# Functions

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Pass by Reference
def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg = arg + 1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

sum = lambda arg1, arg2: arg1 + arg2;

# Strings
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

print ("My name is %s and weight is %d kg!" % ('Anton', 110))

var = 'Welcome to "Python Tutorial" from TutorialsPoint'
print ("var:", var)

var = "Welcome to 'Python Tutorial' from TutorialsPoint"
print ("var:", var)

var = '''Welcome to TutorialsPoint'''
print ("var:", var)

var = """Welcome to TutorialsPoint"""
print ("var:", var)

var = '''
Welcome To
Python Tutorial
from TutorialsPoint
'''
print ("var:", var)
'''
1	len(list)
Returns the length of the string.

2	max(list)
Returns the max alphabetical character from the string str.

3	min(list)
Returns the min alphabetical character from the string str.
'''

# Lists
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)

