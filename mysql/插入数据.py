import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="python",charset="utf8")

cursor = db.cursor()
var = '中国人'
sql ="insert into p1(id,name,age) values(null,'老表',18)"

try:
    ret = cursor.execute(sql)
    db.commit()
    print(cursor.lastrowid)
except:
    db.rollback()

cursor.close()
db.close()