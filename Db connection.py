import pymysql
db = pymysql.connect(host='localhost', user='root', password='database@py',database='November')
con = db.cursor()
sqlquery = "insert into t1 values(%s,%s,%s)"
val = (1, 'Manju', 21)
con.execute(sqlquery, val)
db.commit()
print("inserted")