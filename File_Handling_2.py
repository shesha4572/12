f = open("diary.txt", "r")
lst_lines = f.readlines()
count = 0
for i in lst_lines:
    i = i.lower()
    if i[0] == "p":
        count += 1
f.close()
print("No. of lines starting with H are :", count)
