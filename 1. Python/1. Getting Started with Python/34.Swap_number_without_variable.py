"""Write a program to swap two numbers without using a third variable."""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1 +=num2
num2 = num1 - num2
num1 = num1 - num2

print("First number:",num1)
print("Second number:",num2)