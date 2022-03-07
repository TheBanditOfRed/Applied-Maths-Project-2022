# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Base Vector Figures
u = 19

A = 0                                               # Angle
G = 6.67430 * (10 ** -11)                           # universal gravitation constant
M = 5.972 * (10 ** 24)                              # mass of the Earth
R = 6.371 * (10 ** 6)                               # radius of the Earth
g = 9.819973426224687                               # Gravity

            
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

        
    # Max Height
    T = t / 2
    H = ((Uy * T) - (G * M * 2 * (T ** 2))) / (R ** 2)
    Y = H
    
    print('Max Height:      ', H, 'm')


    # Creating X and Y Vectors
    x = np.linspace(0, t)

    y = ((Uy * x) - (G * M * 2 * (x ** 2))) / (R ** 2)


    # Creating the Plot
    plt.plot(x, y)


# File Saving
plt.savefig('test.png')


# Showing the Plot
plt.show()




#   ------------------------NOTES------------------------
#
#   y = (((Uy * x) / (R ** 4)) ** (1 / 3)) - (((2 * G * M * x) / (R ** 2)) ** (2 / 3))
#
#
#
#



