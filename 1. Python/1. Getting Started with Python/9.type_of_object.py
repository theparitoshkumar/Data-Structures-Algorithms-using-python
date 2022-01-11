"""
Determine the data type of the variable using built-in function type()
"""

num1 = 10
print(type(num1))
# <class 'int'>
num2 = -1210
print(type(num2))
# <class 'int'>
var1 = True
print(type(var1))
# <class 'bool'>
float1 = -1921.9
print(type(float1))
# <class 'float'>
float2 = -9.8*10**2
print(float2, type(float2))
# -980.0000000000001 <class 'float'>
var2 = -3+7.2j
print(var2, type(var2))
# (-3+7.2j) <class 'complex'>