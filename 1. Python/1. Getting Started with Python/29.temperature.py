"""
Write a Python program to convert temperature in degree Celsius to degree Fahrenheit. If water boils at 100 degree C and freezes as 0 degree C, use the program to find out what is the boiling point and freezing point of water on the Fahrenheit scale.
(Hint: T(°F) = T(°C) × 9/5 + 32)
"""

temp_C = int(input("Enter the te in degree Celsius: "))
temp_F = temp_C * 9/5 +32
print(temp_C,"degree Celsius is",temp_F,"in degree Fahrenheit.")

boiling_point_C = 100
boiling_point_F = boiling_point_C * 9/5 +32
print("Boiling point of water in Fahrenheit is",boiling_point_F)

freezing_point_C = 0 
freezing_point_F = freezing_point_C * 9/5 +32
print("Freezing point of water in Fahrenheit is",freezing_point_F)