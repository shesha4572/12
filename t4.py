def reverse(str):
    str1 = str[::-1]
    return str1

def isPalindrome(str):
    if str.lower == isPalindrome(str.lower):
        return True
    else:
        return False

def search(str , sub):
    if sub in str:
        return True
    else:
        return False

def statistic(str):
   words = len(str.split())
   upp_case = 0
   low_case = 0
   digit = 0
   alpha = 0
   for i in str:
       if i.isupper():
           upp_case += 1
           alpha += 1
       elif i.islower():
           low_case += 1
           alpha += 1
       elif i.isdigit():
           digit += 1
   return words, low_case, upp_case, digit, alpha

while True:
    print("1. Reverse a String ")
    print("2. Palindrome Checker")
    print("3. Check for substring")
    print("4. Statistics")
    print("5. Exit")
    o = int(input("Choose an option :"))
    if o == 1:
        str = input("Enter a string : ")
        str_rev = reverse(str)
        print("Reversed string is " , str_rev)
    elif o == 2:
        str = input("Enter a string : ")
        chk = isPalindrome(str)
        if chk:
            print("Entered string is a Palindrome")
        else:
            print("Entered string is not a Palindrome")
    elif o == 3:
        str = input("Enter a string : ")
        sub = input("Enter a substring : ")
        chk = search(str , sub)
        if chk:
            print("Substring entered found in string")
        else:
            print("Substring entered not found in string")
    elif o == 4:
        str = input("Enter a string : ")
        words , low , upp , dig , alp = statistic(str)
        print("No. of words:" , words)
        print("No. of Uppercase letters :" , upp)
        print("No. of Lowercase letters :" , low)
        print("No. of Digits :" , dig)
        print("No. of Alphabets :" , alp)
    elif o == 5:
        break
    else:
        print("Wrong Option")