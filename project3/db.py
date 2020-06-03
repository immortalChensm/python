import pymysql
import config
import sys
class DB():
    def __init__(self):
        self.host=config.dbconfig['host']
        self.port=config.dbconfig['port']
        self.user=config.dbconfig['user']
        self.passwd=config.dbconfig['passwd']
        self.dbname=config.dbconfig['dbname']

    def connection(self):
        self.connnet = pymysql.connect(self.host,self.user,self.passwd,self.dbname,charset="utf8")
        self.cursor = self.connnet.cursor()

    def close(self):
        self.connnet.close()

    def find(self):
        if self.tableName:
            self.connection()
            self.field()

            sql = "SELECT "+str(self.fieldstr)+" FROM "+str(self.tableName)
            self.cursor.execute(sql)
            data = dict(zip(self.fields,self.cursor.fetchone()))
            return data
        else:
            sys.stderr.write("表未指定")

    def table(self,tableName):
        if tableName:
            self.tableName = tableName

            self.connection()
            self.cursor.execute("SHOW COLUMNS FROM %s"%(tableName))
            self.fields = list()
            for field in self.cursor.fetchall():
                self.fields.append(str(field[0]))

        else:
            sys.stderr.write("需要传递一个表名")

        return self
    def field(self,**fieldName):
        self.field = []
        self.fieldstr = ''
        if fieldName:
            for field in fieldName:
                self.field.append(filed)
            self.fieldstr = ','.join(self.field)
        else:
            self.fieldstr = "*"
    def where(self):
        pass
    def order(self):
        pass
    def group(self):
        pass
    def limit(self):
        pass
    def page(self):
        pass
    def select(self):
        pass
    def getField(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def get(self):
        pass
    def all(self):
        pass
    def save(self):
        pass
    def destory(self):
        pass
    def fetchSql(self):
        pass
    def column(self):
        pass
    def value(self):
        pass
    def name(self):
        pass
    def alias(self):
        pass
