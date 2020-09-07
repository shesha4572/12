import random
def funct(num):
    rand = random.randrange(10**(num-1) , 10**num)
    return rand

num = int(input("Enter a number : "))
print("Random number : " , funct(num))