"""
The Range() Function
The range() is a built-in function in Python. 
Syntax of range() function is:
    range([start], stop[, step])
    
The start and step parameters are optional. If start value is not specified, by default the list starts from 0. 
If step is also not specified, by default the value increases by 1 in each iteration. All parameters of range() function must be integers. 
The step parameter can be a positive or a negative integer excluding zero.
"""

#start and step not specified
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#default step value is 1
print(list(range(2,10))) #[2, 3, 4, 5, 6, 7, 8, 9]

#step value is 5
print(list(range(0,30,5))) #[0, 5, 10, 15, 20, 25]


#step value is -1. Hence, decreasing sequence is generated
print(range(0,-9,-1)) #range(0, -9, -1)
print(list(range(0,-9,-1))) #[0, -1, -2, -3, -4, -5, -6, -7, -8]