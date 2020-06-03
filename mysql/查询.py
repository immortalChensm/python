import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="python",charset="utf8")

cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
var = '中国人'
sql ="select * from p1"

try:
    ret = cursor.execute(sql)
    db.commit()
    print(cursor.fetchall())
except:
    db.rollback()

cursor.close()
db.close()