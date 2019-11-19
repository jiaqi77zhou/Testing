"""写入信息到已有表格stu中"""
import pymysql

db = pymysql.connect(
    user='root',
    host='localhost',
    port=3306,
    password='123456',
    charset='utf8',
    database='stu')

cur = db.cursor()

try:
    exc=[]
    for i in range(3):
        name = input("Name:")
        age = input("Age:")
        score = input("Score:")
        exc.append((name,age,score))
    # 法一
    sql_1 = "insert into class_1 (name,age,score) values(%s,%s,%s)"
    cur.executemany(sql_1,exc)
    db.commit()


except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
