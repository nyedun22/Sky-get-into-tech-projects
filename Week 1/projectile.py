import math
g = 9.81 # m/s
v0 = 44
theta = 80 * (math.pi / 180) # radians
x = 0.5
y0 = 1

# running the equation
height_projectile = y0 + (x*math.tan(theta)) - ((g * (x**2)) / (2 * ((v0*math.cos(theta)) ** 2)))

print(height_projectile)