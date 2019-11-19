"""
使用数据库完成登录注册功能,数据表自己拟定

注册方法:收集用户信息,将用户信息存储到数据库,用户名不能重复
登录方法:获取用户名密码,与数据库信息比对,判断是否登录
"""
import pymysql


def connect_database():
    global db
    db = pymysql.connect(
        user='root',
        password='123456',
        host='localhost',
        port=3306,
        database='login',
        charset='utf8'
    )

    global cur
    cur = db.cursor()


def close_database():
    global cur
    cur.close()
    global db
    db.close()


def check_name_duplicate(name):
    sql = "select name from user_information where name =%s;"
    global cur
    cur.execute(sql, [name])
    result = cur.fetchone()
    if result:
        return True
    return False


def add_new_user():
    name = input("Please input your name")
    if check_name_duplicate(name):
        print("The username has exists. Please try another one.")
    else:
        password = input("Please input your password")
        try:
            sql = "insert into user_information (name,password) values (%s,%s);"
            global cur
            cur.execute(sql, [name, password])
            global db
            db.commit()
            print('Thank you for your registration.')
            sql = "select id from user_information where name='%s'" % (name)
            cur.execute(sql)
            id = cur.fetchone()
            print('Your id is', id[0])
        except Exception as e:
            print(e)
            db.rollback()
            print('Add new user failed.')


def check_login():
    name = input("Username:")
    password = input("Password:")
    global cur
    sql = 'select password from user_information where name= %s'
    cur.execute(sql, [name])
    if password == cur.fetchone()[0]:
        print('Welcome!')
    else:
        print("Password incorrect.")


def main():
    connect_database()
    while True:
        option = input("Please choose the function you want: 1.add new user 2.login")
        if not option:
            break
        else:
            if option == '1':
                add_new_user()
            elif option == '2':
                check_login()
    close_database()


if __name__ == '__main__':
    main()
