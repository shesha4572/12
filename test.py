import mysql.connector
db = mysql.connector.connect(host = "localhost" , user = "root" ,passwd = "iiaass123" )
cursor = db.cursor()
cursor.execute("USE 12A;")
cursor.execute("SHOW TABLES;")
for i in cursor:
    print(i)
