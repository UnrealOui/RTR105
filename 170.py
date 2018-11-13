from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

a = 0.8
b = 3.2

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print("Dotajā intervālā [%s, %s] sakņu nav")%(a,b)
    sleep(1); exit()
else:
    print("Dotajā intervālā sakne(s) ir!")

deltax = 0.01

while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x

print("Sakne ir:", x)
