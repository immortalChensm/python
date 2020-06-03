import pymysql

db = pymysql.connect("localhost","root","","python")

cursor = db.cursor()

#sql = "select version()"
#sql = "show tables"
sql = "desc p1"

cursor.execute(sql)

data = cursor.fetchall()
print(data)
cursor.close()
db.close()

