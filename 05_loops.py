# ==========================================
# LOOPS IN PYTHON - while Loops
# ==========================================
# while condition:
#     #some work

# print hello 5 times
i = 0
while i < 5:
    print("hello")
    i += 1

# print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# ==========================================
# PRACTICE (using while)
# ==========================================

# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Print the multiplication table of a number n
n = int(input("Enter n: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

# Print the elements of the following list using a loop
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# Search for a number x in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number to search: "))
i = 0
found = False
while i < len(tup):
    if tup[i] == x:
        found = True
        break
    i += 1
print(found)


# ==========================================
# BREAK & CONTINUE
# ==========================================
# Break -> used to terminate the loop when encountered
# Continue -> terminates execution in current iteration & continues with next

# search example, stop when found
lst = [4, 8, 15, 16, 23, 42]
target = 16
for el in lst:
    if el == target:
        print("Found!")
        break

# print all numbers but not multiples of 3
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)


# ==========================================
# LOOPS IN PYTHON - for Loops
# ==========================================
lst = [1, 2, 3]
for el in lst:
    print(el)

# for Loop with else
for el in lst:
    print(el)
else:
    print("END")


# ==========================================
# range()
# ==========================================
# range(start?, stop, step?)

for el in range(5):
    print(el)

for el in range(1, 5):
    print(el)

for el in range(1, 5, 2):
    print(el)


# ==========================================
# pass STATEMENT
# ==========================================
# pass is a null statement, used as placeholder for future code
for el in range(10):
    pass


# ==========================================
# PRACTICE (using for & range())
# ==========================================

# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a number n
n = int(input("Enter n: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# ==========================================
# PRACTICE (using for)
# ==========================================

# Print elements of the following list using a loop
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in lst:
    print(el)

# Search for a number x in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number to search: "))
found = False
for el in tup:
    if el == x:
        found = True
        break
print(found)


# ==========================================
# PRACTICE (while / for combined)
# ==========================================

# find the sum of first n numbers (using while)
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)

# find the factorial of first n numbers (using for)
n = int(input("Enter n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)