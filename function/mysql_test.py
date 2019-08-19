#/usr/bin/python
import mysql.connector as mysql
#import mysql

mydb = mysql.connect(
	host = "localhost",
	user = "root",
	database = "bookdatabase"	
)

mycursor = mydb.cursor()


#mycursor.execute("SHOW DATABASES")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("SELECT * FROM book")

"""
sql = "INSERT INTO book (id, name, price) VALUES (%s, %s, %s)"
val = ('5', 'g', '1.7')
mycursor.execute(sql, val)
#commit is do the change
mydb.commit()
print (mycursor.rowcount, "inserted")
"""

sql = "DELETE FROM book WHERE id = '5'"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM book")
myresult = mycursor.fetchall()
for x in myresult:	print(x)

mycursor.execute("SHOW TABLES")
myresult = mycursor.fetchall()
for x in myresult:	print(x)

mycursor.execute("SELECT * FROM book")
myresult = mycursor.fetchone()
for x in myresult:	print(x)
