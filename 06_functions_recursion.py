# ==========================================
# FUNCTIONS IN PYTHON
# ==========================================
def func_name(param1, param2):
    # some work
    return "val"

# func_name(arg1, arg2)   # function call

def sum(a, b):
    s = a + b
    return s

print(sum(2, 3))


# ==========================================
# BUILT-IN vs USER DEFINED FUNCTIONS
# ==========================================
# Built-in Functions -> print(), len(), type(), range()
# User defined Functions -> made using def


# ==========================================
# DEFAULT PARAMETERS
# ==========================================
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Harsh")


# ==========================================
# PRACTICE (functions)
# ==========================================

# print the length of a list (list is the parameter)
def print_length(lst):
    print(len(lst))

# print the elements of a list in a single line (list is the parameter)
def print_elements(lst):
    for el in lst:
        print(el, end=" ")
    print()

# find the factorial of n (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# convert USD to INR
def usd_to_inr(usd, rate=83.0):
    return usd * rate

print(usd_to_inr(10))


# ==========================================
# RECURSION
# ==========================================
# When a function calls itself repeatedly

# prints n to 1 backwards
def show(n):
    if n == 0:          # base case
        return
    print(n)
    show(n - 1)

show(5)

# returns n!
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))


# ==========================================
# PRACTICE (recursion)
# ==========================================

# recursive function to calculate sum of first n natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

# recursive function to print all elements in a list (use list & index as parameters)
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

print_list([10, 20, 30])