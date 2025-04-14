import math
degrees = float(input("Enter an angle in degrees: "))

radians = math.radians(degrees)

sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print("sin(", degrees, ") =", sine)
print("cos(", degrees, ") =", cosine)
print("tan(", degrees, ") =", tangent)
