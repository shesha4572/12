import random
def Dice():
    return random.randint(1 , 6)

o = int(input("Press 1 to roll dice: "))
if o == 1:
    print("Dice reads : " , Dice())