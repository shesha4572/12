def PalindromeCheck(x):
    if x == x[::-1]:
        return True
    else:
        return False


str_user = input("Enter a string to be checked : ")
check = PalindromeCheck(str_user.lower())
print("Entered string is: " + str_user)
if check:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")
