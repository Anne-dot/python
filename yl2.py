# Kirjuta programm, mis küsib kasutajalt raadiuse 
# ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
from math import pi
circle_radius = float(input('Sisesta ringi raadius: '))
circle_perimeter = round(2*pi*circle_radius,2)
circle_area = round(pi*circle_radius**2, 2)
print('Ringi ümbermõõt on', circle_perimeter, 'ja pindala on:', circle_area)
