import csv
with open("student.csv" , "r") as csv_file:
    reader = csv.reader(csv_file)
    rowlist = []
    c = 0
    for rec in reader:
        if reader.line_num == 1:
            continue
        else:
            rowlist.append(rec)
    c = len(rowlist)
    print("No. of records" , c)