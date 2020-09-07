def AEDISP():
    f = open("writer.txt" , "r")
    for line in f:
        if line[0] == "a" or line[0] == "e":
            print(line, end="")
    f.close()

"""AEDISP()"""


def Change(P, Q=30):
    P = P + Q
    Q = P - Q
    print(P,    "#" , Q)
    return (P)


R = 150
S = 100
R = Change(R, S)
print(R,  "#",S)
S = Change(S)