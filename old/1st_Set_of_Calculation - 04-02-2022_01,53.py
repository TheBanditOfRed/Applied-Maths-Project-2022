# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Base Vector Figures
u = 19

y = 0
A = 0                                               # Angle
G = 6.67430 * (10 ** -11)                           # universal gravitation constant
M = 5.972 * (10 ** 24)                              # mass of the Earth
R = 6.371 * (10 ** 6)                               # radius of the Earth
g = (G * M) / ((R + y) ** 2)                        # Gravity as altitude increses

            
while A != 90:
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
#   ------------  Angle of  45   ------------
#   Ux:               13.435028842544403
#   Uy:               13.435028842544403
#   Gravity:          9.819973426224687 m/s^2
#   Time of Flight:   2.736265824643791 s
#   Range:            36.76181027495788 m
#   Max Height:       9.19045256873947 m
#
#   ------------  Angle of  45   ------------
#   Ux:               13.435028842544403
#   Uy:               13.435028842544403
#   Gravity:          9.819973426224687 m/s^2
#   Time of Flight:   2.736265824643791 s
#   Range:            36.76181027495788 m
#   Max Height:       9.19045256873947 m



