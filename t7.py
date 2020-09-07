def recur_lst(lst , sum = 0):
   if len(lst) == 0:
       return sum
   else:
       return recur_lst(lst[1::] , sum = lst[0] + sum)
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print("1. Sum of a list")
print("2. Fibonacci Series")
o = int(input("Enter an option : "))
if o == 1:
    lst = eval(input("Enter a list: "))
    print("Sum of all elements of list is" , recur_lst(lst))
elif o == 2:
    nterms = int(input("Enter number of terms in series : "))
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))