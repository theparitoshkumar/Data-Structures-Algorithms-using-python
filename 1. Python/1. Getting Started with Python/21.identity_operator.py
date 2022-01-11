#**********************Identity Operators***********************

#***********************is**************************
#Evaluates True if the variables on either side of the operator point towards the same memory location and False otherwise. 
#var1 is var2 results to True if id(var1) is equal to id(var2)

num1 = 5
print("type(num1) is int:",type(num1) is int)
num2 = num1
print("Address of num1:",id(num1))
print("Address of num2:",id(num2))
print("num1 is num2:",num1 is num2)



#****************************is not*******************
#Evaluates to False if the variables on either side of the operator point to the same memory location and True otherwise. 
#var1 is not var2 results to True if id(var1) is not equal to id(var2)

print("num is not num2:",num1 is not num2)