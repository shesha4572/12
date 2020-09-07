import csv
f = open("student.csv" , "r")
csv_reader = csv.reader(f)
for i in csv_reader:
    print(i)
f.close()
