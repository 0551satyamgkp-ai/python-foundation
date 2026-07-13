#Q 01 (if, elif, else)

'''salary = int(input("enter your salary: "))

if (salary < 30000):
    print("Tax rate = 5%")
elif (salary >= 30000 and salary < 70000):
    print("Tax rate = 15%")
else:
    print("Tax rate = 25%")'''

#Q 02 (def, for, if)

'''def print_even_number(a , b):
    for i in range(a , b + 1):
        if (i % 2 == 0):
            print(i)

print_even_number(10 , 20)'''

#Q 03(def, while)

'''def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

print_digits(312)'''

#Q 04 (def, while)

'''def print_count_digits(n):
    while n > 0:
        n = n // 10
        print(n)

print_count_digits(98765)'''

#Q 05 (def, while)

'''def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

print(sum_of_digits(1234))'''

#Q 06 (while, if)

'''i = 1

while (i < 100):
    i += 1
    if (i % 3 == 0 and i % 5 == 0):
        print(i)'''

#Q 07 (while, if, elif, else)

'''while True:
    value = input("enter a num (or quit): ")

    if value.lower() == "quit":
        break
    num = int(value)

    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")'''

#Q 08 (def, if, elif, else)

'''def calculator(a, b, operation):

    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Inavalid operation"
    
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))'''

#Q 09 (def, if, for)

'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(41))
print(is_prime(35))'''

#Q 10 (guessing number but secret number is hide)

'''from getpass import getpass
secret_number = int(getpass("enter secret number: "))    
while True:
        guess =  int(input("enter your guess: "))

        if guess > secret_number:
            print("Too High")
        elif guess < secret_number:
            print("Too Low")
        else:
            print("Correct!")
            break'''