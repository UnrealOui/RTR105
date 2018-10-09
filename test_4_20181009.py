"""
def thing():
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()
"""

"""
big = max("Hello world")
print(big)
tiny = min("Hello world")
print(tiny)

txt = ("Hi")
big = max(txt)
print(big)
"""

"""
print(float(99)/100)
i = 42
print(i)
print type(i)
f = float(i)
print(f)
print type(f)
"""

"""
s = "123"
print(s)
print type(s)
#print(s + 1)
i = int(s)
print(i)
print type(i)
print(i + 1)

ns = "hello world"
ins = int(ns)
"""

"""
x = 5
print("Throught the glass")

def lyrics(): #definition
    print("I'm looking at you through the glass")
    print("Don't know how much time has passed")
lyrics()
print("Nice")
print(x)
"""

"""
def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)
"""

"""
def greet(lang):
    if lang == 'es':
        return'Hola'
    elif lang == 'fr':         
        return'Bonjour'
    else:
        return'Hello'
"""

"""
#Class 9
def computepay(h,r):
    if h <= 40:
        payed = h * r
        return payed
    else:
        payed  = 40 * r + (h - 40) * (r * 1.5)
        return payed

hrs = float(input("Enter Hours:"))
rat = float(input("Enter Rate:"))
h = hrs
r = rat
    
p = computepay(h,r)
print("Pay",p)
"""
