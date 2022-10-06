"""
@author: vinay
"""

user_input = input("Give any number: ")

try:
    number = int(user_input)
except ValueError:
    number = float(user_input)

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("the number is zero")