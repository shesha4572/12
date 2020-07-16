import csv
with open("student.csv" , "r") as csv_file:
    reader = csv.reader(csv_file)
    for rec in reader:
        print(",".join(rec))