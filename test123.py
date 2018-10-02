import random

rock = 1
scissors = 2
paper = 3

x = random.randint(rock, paper)
y = input("Please choise rock/paper/scissors: ")
y = int(y)
#RPS
print("Rock, Paper, Scissors!")
#A.I choise
if x == 1:
    print("A.I. choise: Rock!")
elif x == 2:
    print("A.I. choise: Scissors!")
elif x == 3:
    print("A.I. choise: Paper!")
#Ur choice
if y == 1:
    print("Your choise: Rock!")
elif y == 2:
    print("Your choise: Scissors!")
elif y == 3:
    print("Your choise: Paper!")
#rock vs y
if x == 1 and y == 1:
    print("Draw!")
elif x == 1 and y == 2:
    print("U lost!")
elif x == 1 and y == 3:
    print("U won!")
#scissors vs y
elif x == 2 and y == 1:
    print("U won!")
elif x == 2 and y == 2:
    print("Draw!")
elif x == 2 and y == 3:
    print("U lost!")
#paper
elif x == 3 and y == 1:
    print("U lost!")
elif x == 3 and y == 2:
    print("U won!")
elif x == 3 and y == 3:
    print("Draw!")
#wrong input vs y
else:
    print("U got cancer? Print correct!")
