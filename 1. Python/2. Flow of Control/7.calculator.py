"""
Let us write a program to create a simple calculator to perform basic arithmetic operations on two numbers.
The program should do the following:
• Accept two numbers from the user.
• Ask user to input any of the operator (+, -, *, /).
        An error message is displayed if the user enters anything else.
• Display only positive difference in case of the operator "-".
• Display a message “Please enter a value other than 0” 
        if the user enters the second number as 0 and operator ‘/’ is entered.
"""

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second number: "))

op = input("Enter the operator (+, -, *, /) : ")

if op == "+":
    result = num1 + num2
elif op == "-":
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == "0":
        print("Denominator zero not allowes. Program Terminated.")
    else:
        result = num1/num2
print("Result:",result)