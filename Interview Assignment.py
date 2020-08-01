# Q1. what is the difference between list and tuple in Python?
# A1. The main difference between lists and tuples is the fact that lists are mutable whereas tuples are immutable

#Example:
#list:
a = ["biology", "maths", "physics"]
print(a)
a[0] = "chemistry"
print(a)
#tuple:
a = ("biology", "maths", "physics")
print(a)
# a[0] = "chemistry"
# print(a)  ...here you will get TypeError: 'tuple' object does not support item assignment

#------------------------------------------------------------------------

#Q2. what are the key features of python?
#A2. 1. Easy to code:
#    2. Free and Open Source:
#    3. Object-Oriented Language:
#    4. Large Standard Library:
#    5. Dynamically Typed Language:

#-----------------------------------------------------------------------

#Q3. what type of language is Python?
#A3. Python (programming language) Python is an interpreted, high-level,
#    general-purpose programming language.

#----------------------------------------------------------------------------------

#Q4. How is Python an interpreted language?
#A4. Python is called an interpreted language because it goes through an interpreter,
#    that turns the code we write into a language that is  understood by the processor.

#------------------------------------------------------------------------------------

#Q5. what is the difference between list vs set with example program?
#A5. Lists and tuples are standard Python data types that store values in a sequence.
#    Sets are another standard Python data type that also store values
#    The major difference is that sets, unlike lists or tuples, cannot have multiple
#    occurrences of the same element and store unordered values.
# Example:
emptySet = set()
Bipc = set(["Biology", "Physics", "Chemistry", "English", "French"])
Mpc = set(["Maths", "Physics", "Chemistry", "English", "Sanskrit"])
print(Bipc)
print(Mpc)
# The output will display the above sets in an unordered manner.

#---------------------------------------------------------------------------------------------

#Q6. How to copy the data from list to empty list with example program?
#A6. There are many ways to copy a list in python:
#    1. copying by slicing:
a = [1, 2, 3, 4, 5]
b = a[:]
print(a)
print(b)
print(id(a))
print(id(b))
# since id of a and b are different they are treated as 2 lists

#    2. copying using list() built-in function:
c = [5, 6, 7, 8, 9]
d = list(c)
print(c)
print(d)
print(id(c))
print(id(d))
# since id of c and d are different they are treated as 2 lists

#   3. copying using the copy method:
a = [1, 2, 3, 4, 5]
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))

#---------------------------------------------------------------------------------------

#Q7. what is name space in python?
#A7. Namespaces in Python are implemented as Python dictionaries, this means it is a mapping of names (keys) to objects (values).

#------------------------------------------------------------------------------------------

#Q8. What is Python path?
#A8. PYTHONPATH is an environment variable which you can set to add additional directories

#--------------------------------------------------------------------------------------

#Q9. what are Python modules?
#A9. Modules refer to a file containing Python statements and definitions.
#    Python code is called a module. example: shiva.py  and its module name would be shiva
#     We use modules to break down large programs into small file for easy access.

#----------------------------------------------------------------------------------------------

#Q10. what are local and global variables in Python with example program?
#A10. There are two types of variables: global variables and local variables.

# The scope of global variables is the entire program whereas,
# the scope of local variable is limited to the function where it is defined.

# local variable example:
def sum(x,y):
    sum = x + y # here x, y are local variables
    return sum
print(sum(5, 10))

# global variables example:
z = 25
def func():
    global z
    print(z)
z=20
func()
print(z)
# here z is called both within the function and outside of the function

#------------------------------------------------------------------------------------------------------

#Q11. which one of these is a floor division?
#   a./
#   b.//
#   c.%
#   d.None of the mentioned

#A.11 ...b is the solution

#-------------------------------------------------------------------------
#Q12. list1 is [2, -6, 656, 12, 26] what is list1[-1]?
#A.12
list1 = [2, -6, 656, 12, 26]
print(list1)
print(list1[-1])

# solution will be 26 ..indexing and -1 is the index of 1st value from the end.

#----------------------------------------------------------------------------------------
#Q13. what is the maximum possible length of an identifier?
#  a. 31 characters
#  b. 63 characters
#  c. 79 characters
#  d. None of the above

#A.13 . 79 is the solution..Identifiers are unlimited in length.
# But to avoid PEP-8 voilation we Limit all lines to a maximum of 79 characters

#--------------------------------------------------------------------------------------------

#Q14. what is the difference between break and continue with an example program by using both in a single program?
#A14. The break statement is used to terminate the loop prematurely when a certain condition is met.
#     The continue statement is used to move ahead to the next iteration without executing
#     the remaining statement in the body of the loop.
#  Example:

while True:
    value = input("\nEnter a number: ")
    if value == 'q':
        print("break statement executed")
        break

    if not value.isdigit():
        print("continue statement executed")
        continue
    
    value = int(value)
    print("Square of", value, "is", value**2)

#------------------------------------------------------------------------------------

#Q15. which of the following is an invalid statement?
# a. abc = 1,000,000
# b. a b c = 1000 2000 3000
# c. a,b,c = 1000, 2000, 3000
# d. a_b_c = 1,000,000

#A.15. b c d are invalid

#---------------------------------------------------------------
#Q16. write  a program for even and odd numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = 0, 0

for num in list1:
    if num % 2 == 0: 
        even_count += 1
  
    else: 
        odd_count += 1
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 

#-----------------------------------------------------------------
#Q17. explain 1.Type Error 2.Name Error 3. Value Error
#A17. 1.Type Error: A TypeError occurs in Python when you attempt to call a
#       function or use an operator on something of the incorrect type.

a = 2 + "two" # 2 is int and "two" is str
print(a)

# 2. Name Error: A NameError means that Python tried to use a variable or function name
#    that has not been defined till tht point.

print (hello)

# 3. Value Error: Raised when a built-in operation or function receives an
#    argument that has the right type but an inappropriate value

k = int("fish")
print(k)
