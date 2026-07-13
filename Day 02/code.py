#Conditional Statement

'''age = 15

if age >= 18:
    print("You can Vote")
    print("You can Drive")
else:
    print("You can't Vote & Drive")'''

#Exmaple 01  Traffic Light

'''color = input("Enter color: ")

if color  == "Red":
    print("Stop")
elif color == "Green":
    print("Go")
elif color == "Yellow":
    print("Look")
else:
    print("Wrong color for traffic lights")'''

#Example 02 

'''age = int(input("Enter age: "))

if (age < 13):
    print("Child")
elif (age >= 13 and age < 18):
    print("Teenager")
else:
    print("Adult")'''

#Example 03 Login

'''username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" and password == "pass"):
    print("LOGIN Successful!")
elif (username != "admin"):
    print("Wrong username")
else:
    print("Wrong password")'''

#Example 04 Multiple

'''n = int(input("enter num:"))

if (n % 5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")'''

# Odd & Even

'''n = int(input("enter num: "))

if (n % 2 == 0):
    print("Even")
else:
    print("Odd")'''

# Nesting

'''username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("success")
else:
    if (username != "admin"):
        print("wrong username")
    else:
        print("wrong password")'''

# Match Case

'''color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Wrong color!")'''

# Loop (While)

#finite loop

'''i = 1 #iterator

while (i <= 5):
    print("Hello Satyam", i)
    i += 1

print ("after loop, count = ", i)'''

#Example 01 loop
#forword  loop

'''i = 1

while (i <= 5):
    print(i)
    i += 1'''

#reverse loop

'''i = 5

while (i >= 1):
    print(i)
    i -= 1'''

#Multiplication

'''n = int(input("enter num: "))

i = 0 #i = 1
while (i < 10): #while (i <= 10):
    print(n * (i + 1)) #print(n * i)
    i += 1'''

#Break & Continue

'''i = 1

while (i <= 10):
    if (i % 6 == 0):
        break
    print(i)
    i += 1

print("outside loop now....")'''

'''i = 1

while (i <= 10):
    if (i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1

print("outside loop now....")'''

#odd with continue
'''i = 0

while (i < 10):
    i += 1
    if (i % 2 == 0):
        continue
    print(i)'''

#Loop (for)

#in => membership opertaor
'''string = "Hello"

for var in string:
    print(var)'''

#sequence 

'''for i in range(10):
    print(i)'''

#count the number of letter 

'''word = "artificial intelligence"
count = 0

for ch in word:
    if(ch == 'i'):
        count += 1

print("count of i = ", count)'''

#vowel count 

'''word = "artificial"
count = 0

for ch in word:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1

print("ans = ", count)'''

#Range() Function

'''for i in range(1, 10, 2): #1 -> start 10 -> under 10 2 -> differnce 2
    print(i)'''

#Sum n number 

'''n = int(input("enter number: "))
sum = 0  

for i in range(1, n + 1):
    sum += i

print("sum =", sum)'''

#Functions

'''def hello(): #function definition
    print("Hello Satyam")

hello() #function call'''

'''def sum(a , b):
    s = a + b
    return s

ans = sum(3, 4)
print(ans)'''

#Example 01 function

'''def calc_avg(a, b, c):
    sum = a + b + c
    return sum/3

print(calc_avg(5, 10, 15))'''

'''def sum(a, b = 1):
    return a + b

print(sum(4, 5)) # print(sum(5))  => 6'''

#Types of Function
#Lambda Function

'''avg = lambda a, b: (a + b)/2
print(avg(4,5))'''

#Factorial of n

'''def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact
n = int(input("enter n: "))
print(calc_factorial(n))'''