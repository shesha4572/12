def funct(a , b):
    diff = b-a
    diff_term = diff/3
    a1 = a + diff_term
    a2 = a1 + diff_term
    return (a , a1 , a2 , b)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
tup = funct(a , b)
print("Series : " , end = "")
for i in tup:
    if tup[-1] == i:
        print(i)
        break
    print(i , end = " , ")