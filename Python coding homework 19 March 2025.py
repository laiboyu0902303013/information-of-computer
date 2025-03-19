#Python coding homework 19 March, 2025

import math

# given data
F1 = 500
F2 = 800
theta = 56

#Resolve F2 into components:
F2x = F2 * math.cos(math.radians(theta))
F2y = F2 * math.sin(math.radians(theta))

#Sum of components:
Rx = F1 + F2x
Ry = F2y

#Resultant magnitude:
R = math.sqrt(Rx**2+Ry**2)

#Resultant direction:
direction = math.degrees(math.atan(Ry/Rx))

#Output result:
print(f"Resultant Force Magnitude (R): {R:.2f} lbs")
print(f"Direction (theta): {direction:.2f} degrees")