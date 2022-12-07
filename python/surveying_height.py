import math

distance_ft = 65 # distance to the object  (base of the triangle)
angle_deg = 74 # the angle to the top of the object (angle of the hypotenuse)

# Convert from degrees to radians
angle_rad = math.radians(angle_deg) # creating a theta

# Calculate the height of the object
height_ft = distance_ft * math.tan(angle_rad) # tan(theta)

# Round to one decimal place
height_ft = round(height_ft, 1) 
print(height_ft)