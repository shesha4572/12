import _pickle
f = open("student.dat" , "rb")
stud_rec = _pickle.load(f)
found = 0
rno = int(input("Enter the roll no to be searched : "))
for R in stud_rec:
    if R[0] == rno:
        print("Successful Search" , R[0] , "Found!")
        found = 1
        break
if found == 0:
    print("Sorry, record not found")
    f.close()