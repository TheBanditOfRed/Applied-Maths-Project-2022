Modelling Brief:
Throwing the javelin as sport evolved from the everyday use of the spear in hunting and warfare. It was widely practised in Ancient Greece and incorporated in the Olympic Games in 708BC as part of the pentathlon. It has been part of the modern Olympic Games programme since 1908 for men and 1932 for women.

Individual techniques vary but the goal of every javelin athlete is the same, to achieve the largest possible range from their point of projection. By using relevant historical data and through appropriate calculations examine how athletes can optimise their javelin throws.


Formulating the Problem
After reading the brief it is clear that the objective of this project is to discover which variables cumulate in the furthest possible distance that a javelin could be theoretically thrown by a human being.

Before diving into the calculations there are a number of tasks we can complete that can make our lives easier in the future:

Research:
	By conducting research either in person or online we can find data that would be extremely 	difficult to find otherwise. Some topics we should research:

    • What is the mass of the javelin?
    • What are the best javelin throwing techniques?
    • How fast can a human throw an object?
    • What is the maximum velocity of a human?
    • How much drag does the javelin generate?

Variables:
	By listing any possible variables now, we can decide which ones we should exclude in future 	calculations:
	
    • Velocity of the javelin when:
        ◦ Being held by the athlete
        ◦ Thrown by the athlete
        ◦ It impacts the ground
	
    • Velocity of the athlete when:
        ◦ They begin their run
        ◦ When they release the javelin

    • The air resistance of:
        ◦ The athlete
        ◦ The javelin

    • The acceleration due to gravity as the altitude of the javelin varies.

    • The angle that the javelin is launched at.
      
    • The launch force of the javelin.

    • The length of the javelin.

    • The centre of gravity of the javelin.


	To simplify the calculations the following assumptions will be made:

    • The javelin will be treated as a particle with a streamlined body for drag calculations.
      
    • Wind resistance is a consistent force and only moves horizontally towards the front of the javelin.
      
    • During the athlete’s run up, they will travel at a constant acceleration.
      
    • The existence of lift will be ignored for all calculations.

	Due to these assumptions if this experiment is ever conducted in the real-world, the results 	from said experiment will most likely vary from the results calculated here.
	

Translating the Problem to Mathematics
If we take take Usain Bolt’s 2009 world record 100m sprint as the basis for the peak of human athletic performance we can calculate that with an acceleration of 9.5 m/s2 (science.org), an athlete could run the javelin running distance of 19m in 2s, with a final velocity of 19m/s.

The athlete will also increase the acceleration of the javelin by over-arm throwing the javelin, this converts rotational momentum into angular acceleration, resulting in an increase in overall velocity.
To keep calculations simple we will ignore this for the first and second set of calculations, and attempt to include in the third set of calculations (I don’t think this will be possible as I believe I currently lack the mathematical ability to do so, but this does not mean I won’t try my best to include it).

To find the most accurate values for the best speed and launch angle, I will be using a custom made script written in the coding language python (python 3.10). All relevant files can be found at https://github.com/TheBanditOfRed/Applied-Maths-Project-2022/, although I will also include the code used to produce the results for each set of calculations in this booklet.
It is important to note that the code uses one external code library created by J.D.Hunter, “Matplotlib: A 2D Graphics Environment”, Computing in Science and Engineering, vol.9, no.3, pp.90-95, 2007. More information about this library can be found at https://matplotlib.org/.


Computing the Solution – First Calculation
The script used to calculate the first set of calculations was version 7 of the code and was completed on the 04/02/2022 at 01:53am. 
In the first set of calculations my main objective was to get a the basic projectile projection complete and working, therefore I ignored the height of the athlete, and I have also used the formula for gravity based on an objects altitude instead of using 9.8m/s2 for the acceleration due to gravity.

This is the code for the first set of calculations:


# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math as m


# Base Vector Figures
u = 19

y = 0
A = 0                                    # Angle
G = 6.67430 * (10 ** -11)                # Universal gravitation constant
M = 5.972 * (10 ** 24)                   # Mass of the Earth
R = 6.371 * (10 ** 6)                    # Radius of the Earth
g = (G * M) / ((R + y) ** 2)             # Gravity as altitude increases

            
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


So what is happening here? Everything with a # before it is a comment (ie. Has no effect on the code. Comments are usually used to keep code organised and easier to read). Lets break the code down by comment category:

	# Import Libraries

		This section imports any internal and external libraries into the coding environment 		so that they may be used as needed. In this case we import:
    • Matplotlib.pyplot	=>	Used to graph the graphs
    • Numpy		=>	An advanced math library
    • Math			=>	A simple math library		
	

	# Base Vector Figures

		All constant variables and start figures are stored here, such as ‘u’ which is the initial 		velocity of the javelin which we calculated in the previous section to be 19m/s.


	while A != 90:
	
		While this is not a comment it is important to explain that this represents the 			beginning of a loop, and that everything which is indented after this line will loop as 		long as ‘A’ is not equal to 90.


	# Vector Components
		
		Calculates ‘Ux’ and ‘Uy’, and prints the values for ‘Ux’, ‘Uy’, and ‘g’ in the console
	

	# Time of Flight
		
		Calculates ‘t’ and prints the value for ‘t’ in the console


	# Range

		Calculates ‘r’ and prints the value for ‘r’ in the console


	# Max Height

		Calculates ‘T’ and ‘H’, and prints the values for ‘T’ and ‘H’ in the console


	# Creating the X and Y Variables

		The line of code ‘x = np.linspace’ exists purely to ensure when ‘y’ is graphed, that it 		is fully visible to the viewer. ‘y’ is also calculated.
		
    
	# Creating the Plot
	
		The graph is plotted based on ‘x’ and ‘y’


	# Showing the Plot

		The plot and all related information is shown in the console


The Data
Having Ran the script we now have 90 data points to check and see which has the largest range.

After looking through all data points, the javelin thrown at 45° with a velocity of 19m/s gave us out best results:

	-----------------  Angle of 44   -----------------				
	Ux:               13.667456206434373					
	Uy:               13.198509038720948					
	Gravity:          9.819973426224687 m/s^2
	Time of Flight:   2.688094654813164 s
	Range:            36.739415973409244 m
	Max Height:       8.869710399622253 m

	-----------------  Angle of 45   -----------------
	Ux:               13.435028842544403
	Uy:               13.435028842544403
	Gravity:          9.819973426224687 m/s^2
	Time of Flight:   2.736265824643791 s
	Range:            36.76181027495788 m
	Max Height:       9.19045256873947 m

	-----------------  Angle of 46   -----------------
	Ux:               13.198509038720948
	Uy:               13.667456206434373
	Gravity:          9.819973426224687 m/s^2
	Time of Flight:   2.783603501397429 s
	Range:            36.739415973409244 m
	Max Height:       9.511194737856684 m


When considering that the world record javelin throw is 98.48m, the over-arm throw, which was left out from this set of calculations, must create a lot of additional acceleration seeing that our best throw is still 61.8005840266m away from the world record.

NOTE: I have just come to the realization that I have coded the gravity based on an objects altitude incorrectly and it in fact only calculates the gravity when y = 0. This will be fixed for the second and third set of calculations.
