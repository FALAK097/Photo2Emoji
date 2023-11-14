# name = input("What is your name ")
# print("My name is " + name)
# hero = input("What's your favorite super hero name ?")
# print(name + "'s favorite super hero name is " + hero)


# Type conversion in python

# old_age = input("Enter your old age ")
# new_age = int(old_age) + 2
# print(new_age)
# first = input("Enter first number")
# second = input("Enter second number")
# sum = int(first) + int(second)
# print("Sum of two numbers is " + str(sum))


# Strings

# name = "Tony Stark"
# print(name.upper())
# print(name.lower())
# print(name.find('S'))  # -1 is printed if not found
# print(name.replace("T", "M"))


# Arithmetic Operators

# print(5 / 3)
# print(5 // 3)
# print(5 % 2)
# print(5 ** 2)
# i = 5
# print(i)
# i += 2
# print(i)

# if else statements

# age = input("Enter your age ")
# if int(age) >= 18:
#     print("You are an adult")
#     print("You can vote")
# elif int(age) < 18 and int(age) > 3:
#     print("You are in school")
# else:
#     print("You are not human")


# Calculator program

# first = input("Enter your first number ")
# operator = input("Enter the operator (+ - * / %) ")
# second = input("Enter your second number ")
# first = int(first)
# second = int(second)
# if operator == "+":
#     print(first + second)
# elif operator == "-":
#     print(first - second)
# elif operator == "*":
#     print(first * second)
# elif operator == "/":
#     print(first / second)
# elif operator == "%":
#     print(first % second)
# else:
#     print("Invalid Operation")

# Print 1 - 10 using while loop
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# Print star pattern
# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i + 1

# i = 5
# while i >= 1:
#     print(i * "*")
#     i = i - 1


# FOR LOOPS
# for i in range(5):
#     print(i)

# marks = [95, 98, 97]
# for score in marks:
#     print(score)

# marks.append(98)
# marks.insert(0, 99)
# print(len(marks))
# print(99 in marks)
# marks.clear()
# print(marks)


# Break & Continue Statements

# students = ["A", "B", "C", "D", "E"]
# for student in students:
#     if student == "D":
#         break
#     if student == "D":
#         continue
#     print(student)


# [] - Lists
# () - Tuples , Not compulsary to use parenthesis
# {} - Sets - Unordered

# Dictionary

# marks = {"Chemistry": 95, "Physics": 90}
# print(marks["Chemistry"])

# marks["Maths"] = 99
# print(marks)

# marks["Chemistry"] = 96
# print(marks)


# In-Built functions , Module functions , User - defined functions

# module functions

# import math
# from math import *
# print(sqrt(4))


# user defined functions

# def print_sum(first, second):
#     print(first + second)
# print_sum(12, 15)


# f string  --- Introduced in python 3.16 and it replaces the format string method

# country = "India"
# name = "Falak"

# print(f"Hello my name is {name} and I am from {country}")


# Doc String

# def square(n):
#     ''' Takes in a number n, returns the square of n '''
#     print(n**2)


# square(5)
# print(square.__doc__)


# Lambda Functions    # double = lambda x:x*2  lambda arguments: expression

# def double(x):
#     return x*2
# print(double(5))


# Map

# l = [1, 2, 3, 4, 5]
# newl = list(map(lambda x: x*2, l))
# print(newl)


# Filter

# def filter_function(a):
#     return a > 2

# newnewl = list(filter(filter_function, l))
# print(newnewl)


# Reduce

# from functools import reduce
# newnewnewl = reduce(lambda x, y: x+y, l)
# print(newnewnewl)


# is vs ==

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)  # True - Value equality
# print(a is b)  # False - Exact location of object in memory

# a = 10
# b = 10
# print(a == b)  # True
# print(a is b)  # True
