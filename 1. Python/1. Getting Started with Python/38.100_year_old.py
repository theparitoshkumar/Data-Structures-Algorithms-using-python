"""
Write a program that asks the user to enter their name and age. 
Print a message addressed to the user that tells the user the year in which they will turn 100 years old.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
present_year = int(input("Enter the present year(e.g., 2022): "))

rem_age = 100 - age
result_year = rem_age + present_year

print("Hello,",name,".You will get 100 years old in year",result_year)