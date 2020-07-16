import mysql.connector
db = mysql.connector.connect(hostname = 'localhost' , username = 'root' , passwd = '****')
cursor = db.cursor()
cursor.execute("CREATE DATABASE TESTDB;")
cursor.execute("USE TESTDB;")
cursor.execute("CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(20), LAST_NAME VARCHAR(20), AGE INT(3) , SEX VARCHAR(10), INCOME NUMERIC(10));")