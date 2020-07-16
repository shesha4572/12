import mysql.connector
db = mysql.connector.connect(hostname = 'localhost' , username = 'root' , passwd = '****' , database = 'EMPLOYEE')
cursor = db.cursor()
cursor.execute("SELECT * FROM EMPLOYEE ORDER BY Salary")
for i in cursor:
    print(i)
