import csv
records = []
while True:
    name = input("Enter name of employee : ")
    eno = input("Enter employee number : ")
    sal = int(input("Enter salary : "))
    records.append([eno , name , sal])
    check = input("Do you want to enter more data? Y/N : ")
    if check.lower() == "n":
        break
with open("employee.csv" , "w" , newline = "") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    for i in records:
        writer.writerow(i)
    print("Details entered")