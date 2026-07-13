#FILE I/O

#FILE OPERATIONS => open, read & close

# f = open("sample.txt", "r") #file object
# f = open("sample.txt", "w")

# #Read
# # # data = f.read()
# # # print(data)
# # print(type(data))

# # data = f.readline()
# # print(data)

# # data = f.readline()
# # print(data)

# #Write
# f.write("Text to overwrite \n the complete data.")

# f.close()

#MODE OF FILE OPERATIONS

# # r => reading
# w => writing, truncates file first
# x => create new & open for writing
# a => wrtting,  appends at end
# b => binary mode 
# t => text mode 
# + => opens disk file for updates(r & w)

# f = open("sample.txt", "a") 
# f.write("\nNew text being appended\n  to the file")
# f.close()

# f = open("sample2.txt", "x")
# f.write("some random text")
# f.close()

# f = open("sample.txt", "r+")
# f.write("1234")
# print(f.read())
# f.close()

#with keyword

# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(len(data)) 

#Delete File

# import os
# os.remove("sample2.txt")

#Practice Problem (Word Serach)

# data = True
# line = 1
# word = "New"

# with open("sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if("New" in data):
#           print(f"{word} found at line {line}")
#           break

#         print(data)
#         line += 1

#EXCEPTION HANDLING => try, except, else, finally

# try:
#     x = int(input("enter x: "))
#     ans = 10/x

# except ZeroDivisionError:
#     print("Divided by 0 is not allowed")

# except ValueError:
#     print("Invalid input")

# else:
#     print(f"ans = {ans}")

# finally:
#     print("End of program")

#LIST COMPREHENSIVE => (for, in, if)

#01
# squares = []

# for i in range(6):
#     squares.append(i*i)

# print(squares)

# sq = [i*i for i in range(6) if i%2 != 0]
# print(sq)

#02
# nums = [-2, -3, 3, 4, -1, 7]

# nums = [0 if val < 0 else val for val in nums]
# print(nums)

# 03
# words = ["hello", "pyhton", "satyam"]

# words =  [val.upper() for val in words]
# print(words)

#JSON MODULE => (JavaScript Object Notation)

#01 (json.loads())
# import json

# json_str = '{"name": "Satyam", "isTeacher": true}'

# py_obj =  json.loads(json_str)

# print(type(json_str))
# print(type(py_obj), py_obj)

#02 (json.dumps())
# import json

# py_obj = {
#     "name": "Satyam",
#     "isTeacher": True
# }

# json_str = json.dumps(py_obj)

# print(type(json_str), json_str)

#03 (json.load())
# import json

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(py_obj)

#04 (json.dump())

# import json
# data = {
#     "name": "Satyam",
#     "age": 27,
#     "isTeacher": True
# }

# with open("data.json", "w") as f:
#     json.dump(data, f, indent = 4, sort_keys =  True)