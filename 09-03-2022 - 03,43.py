# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math


# Base Figures
u = 19
y = 0
DC = 0.1                                            # Drag Coefficient
RA = 0.70686                                        # Reference Area
p = 1.225                                           # Mass Density of Air
A = 0                                               # Angle
G = 6.67430 * (10 ** -11)                           # Universal Gravitation Constant
M = 5.972 * (10 ** 24)                              # Mass of the Earth
R = 6.371 * (10 ** 6)                               # Radius of the Earth
O = (math.pi) / 2                                   # Angular Distance (rad)
tl = 0.25                                           # Time
m = 800                                             # Mass of Javelin
rc = 1                                              # Radius / Length of Arm (m)
print('Initial Velocity:              ', u,'m/s')


# Gravity as Altitude Increses
g = (G * M) / ((R + y) ** 2)


# Angular Velocity
w = (O / tl) * 2                                    # Angular Velocity
print('Angular Velocity (rad):        ', w,'rad/s')

v = w * rc                                          # Tangential Velocity of a Point in Angular Velocity
print('Angular Velocity (m):          ', v,'m/s')

u = u + v
print('Initial + Angular Velocity:    ', u,'m/s')


# Drag
FD = (1/2) * p * (28.8036 ** 2) * DC * RA           # Drag
print('Drag Force:                    ', FD,'N')

a = (FD / m)                                        # Deceleration due to Drag
u = u - (a * tl)                                    # Velocity after Drag
print('Velocity:                      ', u,'m/s')

            
while A != 90:
    A = A + 1

    print('------------  Angle of ', A,'  ------------')

    
    # Vector Components
    Ux = u * math.cos(math.radians(A))
    Uy = u * math.sin(math.radians(A))
    

    print('Ux:              ', Ux)
    print('Uy:              ', Uy)
    

    # Time of Flight
    t = Uy / (g / 2)

    print('Time of Flight:  ', t, 's')


    # Range
    r = Ux * t

    print('Range:           ', r, 'm')

        
    # Max Height
    T = t / 2
    H = (Uy * T) - ((g / 2) * (T ** 2))
    
    print('Max Height:      ', H, 'm')


    # Creating X and Y Vectors
    x = np.linspace(0, t)

    
    y = (Uy * x) - (((G * M) / ((R + H) ** 2) / 2) * (x ** 2))


    # Creating the Plot
    plt.plot(x, y)


# File Saving
plt.savefig('test.png')


# Showing the Plot
plt.show()








