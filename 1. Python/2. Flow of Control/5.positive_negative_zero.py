"""
The syntax for a selection structure using elif is as shown below.
if condition:
  statement(s)
elif condition:
  statement(s)
elif condition:
  statement(s)
else:
  statement(s)
"""

#Check whether a number is positive, negative, or zero.

num = int(input("Enter the number: "))

if num > 0:
    print("Number is positive.")
elif num < 0:
    print("Number is negative.")
else:
    print("Number is zero.")