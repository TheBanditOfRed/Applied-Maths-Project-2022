# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Vector Components
u = 101
A = 2
g = -9.8

Ux = u * m.cos(A)
Uy = u * m.sin(A)

print('Ux:              ', Ux)
print('Uy:              ', Uy)


# Time of Flight
t = Uy / (g / 2)

print('Time of Flight:  ', t, 's')


# Range
r = Ux * t

print('Range:           ', r, 'm')


# Creating X and Y Vectors
x = np.linspace(0, t)

y = (Uy * x) - ((g / 2) * (x ** 2))


# Creating the Plot
plt.plot(x, y)


# Showing the Plot
plt.show()
