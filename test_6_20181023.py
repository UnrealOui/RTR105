#script
"""
#cant work
name = input("Enter name:")
print(name)
x = name - 10
print(x)
"""
"""
fruit = "apple"
letter = fruit[2]
print(letter)
x = 1
letter2 = fruit[x-1]
print(letter2)
print(len(fruit))
"""
"""
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
"""
"""
fruit = "apple"
for letter in fruit:
    print(letter)
"""
"""
word = "Killshot"
count = 0
for letter in word:
    if letter == "l":
        count = count + 1
print(count)
"""
"""
stringus = "My Python Lessons"
print(stringus[0:2])
print(stringus[3:9])
print(stringus[10:999])
print(stringus[:2])
print(stringus[3:])
print(stringus[:])
"""
"""
fruit = "grappes"
"r" in fruit
"p" in fruit
"app" in fruit
if "g" in fruit:
    print("Gotcha!")
"""
"""
word = "banana"
if word == "banana":
    print("All right, bananas.")

if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("All right, bananas.")
"""
"""
hello = "Hello, Chad"
lowhello = hello.lower()
print(lowhello)
print(hello)
print("Hi, Marta".lower())
"""
"""
name = "Andrew"
pos = name.find("rew")
print(pos)
"""
