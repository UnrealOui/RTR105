import sys
sys.path.append("/usr/local/anaconda3/lib/python3.6/site-packages")
import numpy

from numpy import *     # Importē skaitlisko metožu bibliotēkas funkcijas
x = linspace(0, 7, 70)  # Trešais arguments ir ģenerējamo elementu skaits
y = cos(x)
y2 = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y, color = "#112299")
plt.plot(x, y2, color = "#992211")
plt.show()
