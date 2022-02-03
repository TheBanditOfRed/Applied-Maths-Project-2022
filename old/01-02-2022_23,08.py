# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Base Vector Figures
u = 50
A = 0
g = 9.8
Or = 0          # Old Range
Nr = 0          # New Range
Mr = 0          # Max Range

while A != 90:
    A = A + 1

    print('------------  Angle of ', A,'  ------------')

    
    # Vector Components
    Ux = u * m.cos(m.radians(A))
    Uy = u * m.sin(m.radians(A))

    print('Ux:              ', Ux)
    print('Uy:              ', Uy)


    # Time of Flight
    t = Uy / (g / 2)

    print('Time of Flight:  ', t, 's')


    # Range
    r = Ux * t

    print('Range:           ', r, 'm')


    # Max Range-----------------------------------------------------------NEEDS TO BE FIXED
    Nr = r

    if Or < Nr:
        Mr = Nr
        
    Nr = Or
    print(Mr)


    # Max Height
    T = t / 2
    H = (Uy * T) - ((g / 2) * (T ** 2))

    print('Max Height:      ', H, 'm')


    # Creating X and Y Vectors
    x = np.linspace(0, t)

    y = (Uy * x) - ((g / 2) * (x ** 2))


    # Creating the Plot
    plt.plot(x, y)


# File Saving
plt.savefig('test.png')


# Showing the Max Range
print(Mr)


# Showing the Plot
plt.show()




#   ------------------------NOTES------------------------
#
#   Gravity as altitude increses, g = (G * M) / ((R + Z) ** 2)
#
#   G (universal gravitation constant) = 6.67430 * (10 ** -11)
#   M (mass of the Earth) = 5.972 * (10 ** 24)
#   R (radius of the Earth) = 6.371 * (10 ** 6)
#   Z (altitude) = y


