import mysql.connector
db = mysql.connector.connect(hostname = 'localhost' , username = 'root' , passwd = '****' , database = 'EMPLOYEE')
cursor = db.cursor()
name = input("Enter name of employee to be deleted: ")
sql = "DELETE FROM EMPLOYEE WHERE NAME LIKE" , name , ";"
cursor.execute(sql)