import _pickle
record = []
while True:
    roll_no = int(input("Enter the roll no : "))
    name = input("Enter name : ")
    marks = int(input("Enter marks : "))
    data = [roll_no , name , marks]
    record.append(data)
    choice = input("Do you want to insert more records (Y/N) : ")
    if choice.upper() == "N":
        break
f = open("student.dat" , "wb")
_pickle.dump(record , f)
print("Record added")
f.close()