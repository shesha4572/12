import csv
with open("student.csv" , "r") as csv_file:
    reader = csv.reader(csv_file)
    name = input("Enter the name to be searched : ")
    for rec in reader:
        if rec[0] == name:
            print(rec)