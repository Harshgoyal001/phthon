# ==========================================
# STRINGS - basic operations
# ==========================================
# concatenation
print("hello" + "world")

# length of str
str1 = "hello"
print(len(str1))


# ==========================================
# INDEXING
# ==========================================
str1 = "greater_noida_institute_of_technology"
print(str1[0])   # 'g'
print(str1[1])   # 'r'
# str1[0] = 'B'    # not allowed.because it is immutable 


# ==========================================
# SLICING
# ==========================================
str1 = "greater_noida_institute_of_technology"
print(str1[1:4])    # "re"
print(str1[:4])      # same as str1[0:4]
print(str1[1:])       # same as str1[1:len(str1)]

# Negative Index
str2 = "Apple"
print(str2[-3:-1])   # "pl"


# ==========================================
# STRING FUNCTIONS
# ==========================================
str1 = "I am a coder."

print(str1.endswith("er."))# True
print(str1.capitalize())# "I am a coder."
print(str1.upper())# "I AM A CODER."
print(str1.replace("am", "was"))# "I was a coder."
print(str1.find("coder"))# 7
print(str1.count("am"))# 1


# ==========================================
# PRACTICE (strings)
# ==========================================

# input user's first name & print its length
name = input("Enter your first name: ")
print(len(name))

# find the occurrence of '$' in a String
str1 = "price is $5, $10 and $20"
print(str1.count("$"))


# ==========================================
# CONDITIONAL STATEMENTS - if-elif-else
# ==========================================
# if(condition):
#     Statement1
# elif(condition):
#     Statement2
# else:
#     StatementN

# grade students based on marks
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)


# ==========================================
# PRACTICE (conditional statements)
# ==========================================

# check if a number entered by the user is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# find the greatest of 3 numbers entered by the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

# check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")