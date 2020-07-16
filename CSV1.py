import csv
with open("student.csv" , "r") as csv_file:
    reader = csv.reader(csv_file)
    row = []
    for rec in reader:
        row.append(rec)
    print(row)