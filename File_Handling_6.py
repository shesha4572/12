def AEDISP():
    f = open("writer.txt" , "r")
    for line in f:
        if line[0] == "a" or line[0] == "e":
            print(line, end="")
    f.close()

AEDISP()
