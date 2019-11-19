"""
存储二进制文件
"""
import pymysql

db = pymysql.connect(user='root',
                     host='localhost',
                     port=3306,
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()
# 读二进制文件,并写入到数据库
with open('xi.jpeg', 'rb') as f:
    data = f.read()

try:
    sql = "update class_1 set image=%s where id = 1;"
    cur.execute(sql, [data])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 从数据库中读二进制文件,并且复制一份出来!
sql = 'select image from class_1 where id=1;'
cur.execute(sql)
data = cur.fetchone()
with open('1.jpeg', 'wb') as f:
    f.write(data[0].encode())

cur.close()
db.close()
