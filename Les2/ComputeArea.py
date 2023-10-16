# Assign a radius
radius = int(input("straal?")) # radius is now 20

PI = 3.14159

# Compute area
if radius > 0:
    area = radius * radius * PI
    print("The area for the circle of radius", radius, "is", area)
else:
    print("Negatieve input")

# Display results
