# ==========================================
# WHAT IS PYTHON / OUR FIRST PROGRAM
# ==========================================
print("Hello World")


# ==========================================
# VARIABLES
# ==========================================
name = "harshgoyal"#string
age = 23#int
price = 25.9#float


# ==========================================
# DATA TYPES
# ==========================================
age = 23
pi = 3.14
complex_num = 2 + 3j
A = True
name = "Shradha"

print(type(age))
print(type(pi))
print(type(complex_num))
print(type(A))
print(type(name))


# ==========================================
# KEYWORDS
# ==========================================
# and  as  assert  break  class  continue  def  del  elif  else
# except  False  finally  for  from  global  if  import  in  is
# lambda  nonlocal  None  not  or  pass  raise  return  True
# try  while  with  yield


# ==========================================
# COMMENTS
# ==========================================
# Single Line Comment

"""
Multi Line
Comment
"""


# ==========================================
# TYPES OF OPERATORS
# ==========================================
# Arithmetic       + - * / % **
# Relational        == != > < >= <=
# Assignment          = += -= *= /= %= **=
# Logical               not and or

# print sum example
a = 5
b = 3
print("Sum is:", a + b)


# ==========================================
# TYPE CONVERSION
# ==========================================
a, b = 1, 2.0
sum = a + b
print(sum)

# a, b = 1, "2"
# sum = a + b     # this gives error


# ==========================================
# TYPE CASTING
# ==========================================
a, b = 1, "2"
c = int(b)
sum = a + c
print(sum)


# ==========================================
# INPUT IN PYTHON
# ==========================================
# input()          -> always str
# int(input())      -> int
# float(input())     -> float


# ==========================================
# PRACTICE
# ==========================================

# input 2 numbers & print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# input side of a square & print its area
side = float(input("Enter side of square: "))
print("Area:", side * side)

# input 2 floating point numbers & print their average
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Average:", (x + y) / 2)

# input 2 int numbers a and b, print True if a >= b else False
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a >= b)