"""
Case Study-based Question Schools use “Student Management Information System” (SMIS) to manage student-related data. 
This system provides facilities for:
• recording and maintaining personal details of students.
• maintaining marks scored in assessments and computing results of students.
• keeping track of student attendance.
• managing many other student-related data. 
Let us automate this process step by step.
Identify the personal details of students from your school identity card and write a program to accept these
details for all students of your school and display them in the following format.

                NAME OF SCHOOL
    Student Name: XYZ       Roll No.: 123
    Class: XXX              Section: A 
    Address: Address1
             Address2
    City: ABC               PIN: 999999
    Parent's/Guardian's Contact No.:999999999

"""

school = input("Enter name of school: ")
name = input("Enter your name: ") 
roll = int(input("Enter Roll No.: ")) # roll may be increase or decrase if students get admit or transfer
Class = int(input("Enter your Class: ")) # class will increase every year
section = input('Enter your section: ')
address1 = input("Enter your address line 1: ")
address2 = input("Enter your address line 2: ")
city = input("Enter your city: ")
pin = input("Enter Your PIN:")
contact = input("Enter your contact number: ")


print("\t\t\t\t",school)
print("\tName:",name,end = "\t\t")
print("Roll No.:",roll)
print("\tClass:",Class,end = "\t\t\t\t\t")
print("Section:",section)
print("\tAddress:",address1)
print("\t\t\t",address2)
print("\tCity:",city,end="\t\t\t\t")
print("PIN:",pin)
print("\tParent's/Guardian's Contact No.:",contact)

