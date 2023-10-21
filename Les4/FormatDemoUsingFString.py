import math

# Display the header of the table 
print(f"{'Degrees':<10s} {'Radians':<10s}",
    f"{'Sine':<10s} {'Cosine':<10s}", 
    f"{'Tangent':<10s}")

# Display values for 30 degrees
degrees = 30
radians = math.radians(degrees)
print(f"{degrees:<10d} {radians:<10.4f}",
    f"{math.sin(radians):<10.4f}",  
    f"{math.cos(radians):<10.4f}",
    f"{math.tan(radians):<10.4f}")

# Display values for 60 degrees
degrees = 60
radians = math.radians(degrees)
print(f"{degrees:<10d} {radians:<10.4f}",
    f"{math.sin(radians):<10.4f}",  
    f"{math.cos(radians):<10.4f}",
    f"{math.tan(radians):<10.4f}")