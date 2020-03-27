def PrimeCheck(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    else:
        for i in range(2 , num):
            if num % i == 0:
                return False
        else:
            return True


num_user = int(input("Enter a number to be checked : "))
print("Entered number is :" , num_user)
check = PrimeCheck(num_user)
if check:
    print("Entered number is a prime number")
else:
    print("Entered number is not a prime number")
