import math

print('Welcome to the velocity calculator. Please enter the following:\n')

mass = 5 #input('Mass(in kg): ')
gravity = 9.8 #input('Gravity (in m/s^2, 9.8 for Earth, 24 Jupiter): ')
time = input('Time (in seconds): ')
density = 1.3 #input('Density of the fluid (in kg/m3, 1.3 for air, 1000 for water): ')
x_section = .01 #input('Cross sectional area (in m^2): ')
drag = .5 #input('Drag constant (0.5 for sphere, 1.1 for cylinder): ')

c = (1 / 2) * float(density) * float(x_section) * float(drag)
mg = float(mass) * float(gravity)
velocity = math.sqrt(mg / c) * (1 - math.exp(-(math.sqrt(mg * c) / float(mass)) * float(time)))

print(f'\nThe inner value of c is: {c:.3f}')
print(f'The velocity after {float(time):.1f} seconds is: {velocity:.3f} m/s')