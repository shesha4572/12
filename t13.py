with open("test.txt" , "r") as f:
    search = input("Enter string to be searched in file : ")
    str = f.read()
    count = str.count(search)
    print(count)

