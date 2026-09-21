# ==========================================
# DICTIONARY IN PYTHON
# ==========================================
dict1 = {
    "name": "shradha",
    "cgpa": 9.6,
    "marks": [98, 97, 95],
}

print(dict1["name"], dict1["cgpa"], dict1["marks"])
dict1["key"] = "value"     # to assign or add new


# ==========================================
# NESTED DICTIONARIES
# ==========================================
student = {
    "name": "shradha",
    "score": {
        "chem": 98,
        "phy": 97,
        "math": 95
    }
}
print(student["score"]["math"])   # 95


# ==========================================
# DICTIONARY METHODS
# ==========================================
myDict = {"a": 1, "b": 2}
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict.get("a"))
myDict.update({"c": 3})


# ==========================================
# SET IN PYTHON
# ==========================================
nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}      # resolves to {1, 2}
null_set = set()           # empty set syntax


# ==========================================
# SET METHODS
# ==========================================
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.clear()

s2 = {1, 2, 3}
s3 = {2, 3, 4}
print(s2.union(s3))            # {1, 2, 3, 4}
print(s2.intersection(s3))      # {2, 3}
s2.pop()


# ==========================================
# PRACTICE (dictionary & set)
# ==========================================

# store word meanings in a python dictionary
word_meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}
print(word_meanings)

# given a list of subjects, find how many classrooms needed (1 per unique subject)
subjects = ["python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"]
unique_subjects = set(subjects)
print(len(unique_subjects))

# enter marks of 3 subjects, store in a dictionary
marks_dict = {}
for i in range(3):
    sub = input("Enter subject name: ")
    m = int(input("Enter marks: "))
    marks_dict[sub] = m
print(marks_dict)

# store 9 & 9.0 as separate values in a set (using built-in data types)
s2 = {"9", "9.0"}
print(s2)