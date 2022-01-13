"""
The syntax for if..else statement is as follows.
if condition:
  statement(s)
else:
  statement(s)
"""

#The user is eligible for Vote or not
age = int(input("Enter your age: "))

if age > 18:
    print("Eligible for Vote.")
else:
    print("Not Eligible for Vote")