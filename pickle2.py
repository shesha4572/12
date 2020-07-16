import _pickle
f = open("student.dat" , "rb")
stud_rec = _pickle.load(f)
print("contents: ")
for R in stud_rec:
    print(R)