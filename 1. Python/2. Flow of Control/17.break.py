"""
The break statement alters the normal flow of execution as it terminates the current loop 
and resumes execution of the statement following that loop.
"""

#Program to demonstrate the use of break statement in loop

for num in range(10):
    num += 1
    if num == 8:
        break
    print("Num has value", num)
print("Encounterd break! out of the loop.")
