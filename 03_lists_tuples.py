# ==========================================
# LISTS IN PYTHON.they are mutable (can be changed) and ordered (indexing is possible)
# ==========================================
marks = [87, 64, 33, 95, 76]        # marks[0], marks[1]..

student = ["Karan", 85, "Delhi"]     # student[0], student[1]..
student[0] = "Arjun"                  # allowed in python

print(len(student))


# ==========================================
# LIST SLICING
# ==========================================
marks = [87, 64, 33, 95, 76]
print(marks[1:4])      # [64, 33, 95]
print(marks[:4])        # same as marks[0:4]
print(marks[1:])         # same as marks[1:len(marks)]
print(marks[-3:-1])       # [33, 95]


# ==========================================
# LIST METHODS
# ==========================================
lst = [2, 1, 3]
lst.append(4)               # [2, 1, 3, 4]
lst.sort()                    # [1, 2, 3, 4]
lst.sort(reverse=True)         # descending order
lst.reverse()                    # reverses list
lst.insert(1, 10)                 # insert element at index

lst2 = [2, 1, 3, 1]
lst2.remove(1)             # removes first occurrence -> [2, 3, 1]
lst2.pop(0)                  # removes element at idx


# ==========================================
# PRACTICE (lists)
# ==========================================

# ask the user to enter names of their 3 favorite movies & store in a list
movies = []
for movie in range(3):
    movie = input("Enter movie name: ")
    movies.append(movie)
print(movies)

# check if a list contains a palindrome of elements (use copy() method)
lst = [1, 2, 3, 2, 1]
temp = lst.copy()
temp.reverse()
if lst == temp:
    print("Palindrome")
else:
    print("Not a palindrome")


# ==========================================
# TUPLES IN PYTHON they are immutable (cannot be changed) and ordered (indexing is possible)
# ==========================================
tup = (87, 64, 33, 95, 76)   # tup[0], tup[1]..
# tup[0] = 43                  # NOT allowed

tup1 = ()          # empty tuple
tup2 = (1,)         # single element tuple
tup3 = (1, 2, 3)


# ==========================================
# TUPLE METHODS
# ==========================================
tup = (2, 1, 3, 1)
print(tup.index(1))    # returns index of 1st occurrence -> 1
print(tup.count(1))     # counts total occurrences -> 2


# ==========================================
# PRACTICE (tuples)
# ==========================================

# count number of students with "A" grade in this tuple
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

# store the above values in a list & sort them from "A" to "D"
grades_list = list(grades)
grades_list.sort()
print(grades_list)