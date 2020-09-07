def fact(num):
    fac = 1
    for i in range(0 , num+1):
        fac *= i
    return fac

def fibonnaci(num):
    a = 0
    b = 1
    sum = 0
    count = 1
    print("Fibonacci Series: ", end=" ")
    while (count <= num):
        print(sum, end=" ")
        count += 1
        a = b
        b = sum
        sum = a + b

print("1. Factorial of a number")
print("2. Fibonacci Series")
n = int(input("Choose an option : "))
if n == 1:
    num = int(input("Enter a number : "))
    print("Factorial of" , num , "is" , fact(num))
elif n == 2:
    num = int(input("Enter a number : "))
    fibonnaci(num)
else:
    print("Wrong Option")