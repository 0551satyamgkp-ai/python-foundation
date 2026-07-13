#Student Enrollment

'''info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
unique_courses = set()

for tup in info:
    unique_courses.add(tup[1])

print(unique_courses)

for name,course in info:
    print(name,course)

for name,course in info:
    if(course == "English"):
        print(name)

dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)'''

#Q 01

# word = input("Enter a string: ")

# reverse = ""

# for ch in word:
#     reverse = ch + reverse
# if word ==  reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#Q 02 

marks = [10, 20, 25, 30]
avg = sum(marks) / len(marks)
print("Average Number: ")