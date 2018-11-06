from math import sin
from math import sqrt

def mans_sinuss(x):
    k = 1
    a = (-1)**2*2*x/2
    S = a
    print("Izdruka no liet.f. a1 = %6.2f S1 = %6.2f"%(a,S))

    while k <= 500:
        k = k + 1
        R = (-1)*x*2**2/((2*k-1)*(2*k))
        a = a * R
        S = S + a
        if k == 500:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    return S
            
x = float(input("Ievadi argumentu (x): "))

y = sin(sqrt(x)) * sin(sqrt(x))
print("A.I. sin:", y)

yy = mans_sinuss(x)
print("Bag of bones sin:", yy)
