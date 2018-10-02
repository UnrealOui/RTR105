"""
hrs = input("Enter Hours:")
h = float(hrs)
sh = 40
rat = 10.50
rcf = 1.5
if h > 40:
    a = h - sh
    r = rat * rcf
    x = a * r + sh*rat
    print(x)
else:
    x = h * rat
    print(x)
"""    
astr = "Bob"
try:
    print("Hello")
    istr = str(astr)
    print("There")
except:
    istr = -1
    
print("Done", istr) 
