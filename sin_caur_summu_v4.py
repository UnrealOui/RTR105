# -*- coding: utf-8 -*-
from math import sin
x = float(input("Ievadi argumentu (x): "))
#print type(x)
#a0, a1, a2, a3 -> a
y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))

k = 0
a = (-1)**0*x**1/(1)
S = a
print("a0 = %.2f S0 = %.2f"%(a,S))

k = 1
#a1 = (-1)**1*x**3/(1*2*3)
#a1 = a0 * (-1)*x*x/(2*3)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print("a%d = %.2f S%d = %.2f"%(k,a,k,S))

k = 2
#a2 = (-1)**2*x**5/(1*2*3*4*5)
#a2 = a1 * (-1)*x*x/(4*5)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a 
print("a%d = %.2f S%d = %.2f"%(k,a,k,S))

k = 3
#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
#a3 = a2 * (-1)*x*x/(6*7)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print("a%d = %.2f S%d = %.2f"%(k,a,k,S))
