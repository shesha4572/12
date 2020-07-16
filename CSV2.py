import csv
with open("student.csv" , "r") as csv_file:
    reader = csv.reader(csv_file)
    c = 0
    for rec in reader:
        c += 1
    print("No. of records" , c)