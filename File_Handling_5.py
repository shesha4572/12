def IsToUpCount(f):
    count_is , count_to , count_up = 0 , 0 , 0
    words = f.read()
    list_words = words.split()
    for i in list_words:
        i = i.lower()
        if i == "is":
            count_is += 1
        elif i == "to":
            count_to += 1
        elif i == "up":
            count_up += 1
    return count_is , count_to , count_up


f = open("writer.txt" , "r")
c_is , c_to , c_up = IsToUpCount(f)
f.close()
print("Count of is, to and up respectively is" , str(c_is)+ "," , str(c_to) + ","  , str(c_to))