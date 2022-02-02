# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Base Vector Figures
u = 50

y = 0
A = 0                                               # Angle
G = 6.67430 * (10 ** -11)                           # universal gravitation constant
M = 5.972 * (10 ** 24)                              # mass of the Earth
R = 6.371 * (10 ** 6)                               # radius of the Earth
g = (G * M) / ((R + y) ** 2)                        # Gravity as altitude increses
Or = 0                                              # Old Range
Nr = 0                                              # New Range
Mr = 0                                              # Max Range

            
while A != 90:
    global Nr
    global Or
    global Mr
    A = A + 1

    print('------------  Angle of ', A,'  ------------')

    
    # Vector Components
    Ux = u * m.cos(m.radians(A))
    Uy = u * m.sin(m.radians(A))

    print('Ux:              ', Ux)
    print('Uy:              ', Uy)
    print('Gravity:         ', g,'m/s^2')

    # Time of Flight
    t = Uy / (g / 2)

    print('Time of Flight:  ', t, 's')


    # Range
    r = Ux * t

    print('Range:           ', r, 'm')

    
    # Total Max Range
    Nr = r

    if Or < Nr:
        Mr = Nr

    Nr = Or

    print('Total Max Range: ', Mr, 'm')
        
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


# Showing the Plot
plt.show()




#   ------------------------NOTES------------------------
#
#
#
#
#
#
#


