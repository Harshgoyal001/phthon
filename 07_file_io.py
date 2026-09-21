# ==========================================
# FILE I/O IN PYTHON
# ==========================================
# Types of files:
# 1. Text Files : .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.


# ==========================================
# OPEN, READ & CLOSE FILE
# ==========================================
f = open("file_name", "mode")
data = f.read()
f.close()

# Modes:
# 'r' -> read (default)
# 'w' -> write, truncates file first
# 'x' -> create new file for writing
# 'a' -> write, appends to end
# 'b' -> binary mode
# 't' -> text mode (default)
# '+' -> read and write


# ==========================================
# READING A FILE
# ==========================================
f = open("sample.txt", "r")
data = f.read()          # reads entire file
f.close()

f = open("sample.txt", "r")
line = f.readline()       # reads one line at a time
f.close()


# ==========================================
# WRITING TO A FILE
# ==========================================
f = open("demo.txt", "w")
f.write("this is a new line")   # overwrites entire file
f.close()

f = open("demo.txt", "a")
f.write("this is a new line")    # adds to file
f.close()


# ==========================================
# with SYNTAX
# ==========================================
with open("demo.txt", "a") as f:
    data = f.read()


# ==========================================
# DELETING A FILE (using os module)
# ==========================================
import os
# os.remove(filename)


# ==========================================
# PRACTICE
# ==========================================

# Create a new file "practice.txt" & add the given data
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.\n")

# WAF that replace all occurrences of "java" with "python" in above file
with open("practice.txt", "r") as f:
    content = f.read()
content = content.replace("Java", "Python").replace("java", "python")
with open("practice.txt", "w") as f:
    f.write(content)

# Search if the word "learning" exists in the file or not
with open("practice.txt", "r") as f:
    content = f.read()
if "learning" in content:
    print("Found")
else:
    print("Not found")

# find in which line of the file the word "learning" occurs first (print -1 if not found)
def find_line(filename, word):
    with open(filename, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        if word in line:
            return i
    return -1

print(find_line("practice.txt", "learning"))

# from a file with numbers separated by comma, print the count of even numbers
# (assume numbers.txt contains: 1,2,3,4,5,6)
with open("numbers.txt", "r") as f:
    data = f.read()
numbers = data.split(",")
count = 0
for num in numbers:
    if int(num) % 2 == 0:
        count += 1
print("Even count:", count)