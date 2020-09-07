def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
def recur_exp(a , b):
    if b == 0:
       return 1
    elif b == 1:
        return a
    else:
        return a * recur_exp(a, b-1)

print("1. Factorial")
print("2. a raised to b")
o = int(input("Enter an option : "))
if o == 1:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
elif o == 2:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a , "raised to" , b , "is" , recur_exp(a , b))