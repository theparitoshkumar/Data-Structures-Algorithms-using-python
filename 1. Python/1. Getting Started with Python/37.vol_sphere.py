"""The volume of a sphere with radius r is 4/3πr3. 
Write a Python program to find the volume of spheres with radius 7cm, 12cm, 16cm, respectively."""

radius1 = 7
radius2 = 12
radius3 = 16 
pi = 22/7

vol1 = 4/3*pi*(radius1**3)
vol2 = 4/3*pi*(radius2**3)
vol3 = 4/3*pi*(radius3**3)

print("Volume of sphere with radius", radius1,"is",vol1)
print("Volume of sphere with radius", radius2,"is",vol2)
print("Volume of sphere with radius", radius3,"is",vol3)
