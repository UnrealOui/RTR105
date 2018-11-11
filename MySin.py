from math import sin
from math import sqrt

def mans_sinuss(x):
    n = 1
    a = 2*x/2
    S = a
    print("a1 = %6.2f S1 = %6.2f"%(a,S))

    while n <= 500:
        n = n + 1
        R = (-1)*x*2**2/((2*n-1)*(2*n))
        a = a * R
        S = S + a
        if n == 499:
            print("a%d = %6.8f S%d = %6.8f"%(n,a,n,S))
        if n == 500:
            print("a%d = %6.8f S%d = %6.8f"%(n,a,n,S))

    return S

print("------------------------")
print("SIN function calculation:")
print("------------------------")
x = float(input("Ievadi argumentu (x): "))
print("------------------------")
y = sin(sqrt(x)) * sin(sqrt(x))
print("A.I. SIN:", y)
print("")
yy = mans_sinuss(x)
print("")
print("Bag of bones SIN:", yy)
print("")

print("       500                                       ")
print("     ------                                     ")
print("     \\                n+1    n    2*n-1      ")
print("      \\          (-1)    * x  * 2             ")
print("sin   =>      ----------------------    ")
print("      /                   (2*n)!                 ")
print("     /                                             ")
print("     ------                                      ")
print("        n=1                                       ")

print("")

print("                      2  ")
print("       (-1) * x * 2    ")
print("R: ----------------")
print("     (2*n-1) * (2*n)")
