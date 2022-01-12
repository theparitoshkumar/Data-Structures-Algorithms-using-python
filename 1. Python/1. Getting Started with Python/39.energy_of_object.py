"""
The formula E = mc^2 states that the equivalent energy (E) can be calculated as 
the mass (m) multiplied by the speed of light (c = about 3×10^8 m/s) squared. 
Write a program that accepts the mass of an object and determines its energy.
NOTE: ^ is denoting power.
"""

mass = int(input("Enter the mass of the object: "))
speed_of_light = 3 * (10 ** 8)
energy = mass * (speed_of_light ** 2)

print("Energy:", energy)