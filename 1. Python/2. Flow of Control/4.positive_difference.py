#Program to print the positive difference of two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    diff = num1 - num2
else:
    diff = num2 - num1
print("The difference between", num1,"and", num2, "is",diff)