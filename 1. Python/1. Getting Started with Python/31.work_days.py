"""Write a program to calculate in how many days a work will be completed by three persons A, B and C together. 
A, B, C take x days, y days and z days respectively to do the job alone. The formula to calculate the number of days if they work together
is xyz/(xy + yz + xz) days where x, y, and z are given as input to the program."""

days_A = int(input("Enter the number of days required by A to complete a work alone: "))
days_B = int(input("Enter the number of days required by B to complete a work alone: "))
days_C = int(input("Enter the number of days required by C to complete a work alone: "))

result = (days_A*days_B*days_C)/(days_A*days_B + days_B*days_C + days_A*days_C)

print("Three persons A,B and C will complete the work in",result,"days.")