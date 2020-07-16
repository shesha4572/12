import csv
fields = ["Name" , "Roll_no"]
records = [
    ("A" , 4) ,
    ("B" , 5)
        ]
with open("student.csv" , "w" , newline = "") as csv_file:
    writer = csv.writer(csv_file , delimiter = ",")
    writer.writerow(fields)
    writer.writerows(records)
    print("File created")
    