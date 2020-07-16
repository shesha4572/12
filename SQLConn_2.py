import mysql.connector
db = mysql.connector.connect(hostname = 'localhost' , username = 'root' , passwd = '****' , database = 'EMPLOYEE')
cursor = db.cursor()
cursor.execute("UPDATE EMPLOYEE SET Salary = Salary + 3000 WHERE Name LIKE 'Manoj'")
