from time import sleep
import pymysql


class Manager:
    def __init__(self, database, user='root', host='localhost', port=3306, password='123456', charset='utf8'):
        self.table = []
        self.db = pymysql.connect(
            user=user,
            host=host,
            port=port,
            password=password,
            charset=charset,
            database=database)
        self.cur = self.db.cursor()
        self.database = database

    def program_start(self):
        print("Entered", self.database, '.')
        while True:
            table = input("Please enter the table you want to use:")
            if not table:
                msg = input("Do you want to leave the database? 1.yes 2.no")
                if msg == '1':
                    print("Leaving database...")
                    sleep(1)
                    return

            while True:
                print("Please enter your option:")
                print("1.Add new user.")
                print("2.Delete user.")
                print("3.Add image to users.")
                option = input()
                if option == '1':
                    self.add_new_user(table)
                elif option == '2':
                    self.delete_student(table)
                elif option == '3':
                    self.add_image(table)
                elif not option:
                    option2 = input("Do you want to switch to another table in this database? 1 yes 2 no")
                    if option2 == '1':
                        sleep(0.5)
                        break
                    elif option2 == '2':
                        sleep(0.5)
                        print("Thank you for using.")
                        print("Bye!")
                        return

    def add_new_user(self, table):
        while True:
            try:
                print("Please enter the student information you want to add:")
                name = input("Name:")
                age = input("Age:")
                score = input("Score:")
                sql = 'insert into %s' % (table)
                sql = sql + " (name,age,score) values (%s,%s,%s)"
                self.cur.execute(sql, [name, age, score])
                self.db.commit()
                option = input("Add successfully! Do you want to continue? 1. yes 2.no")
                if option == '2':
                    print('leaving adding option...')
                    sleep(0.5)
                    break
            except Exception as e:
                print(e)
                self.db.rollback()

    def delete_student(self, table):
        while True:
            try:
                print("Please enter the student information you want to delete:")
                name = input("Name:")
                sql = 'delete from %s' % (table)
                sql = sql + " where name = %s"
                self.cur.execute(sql, [name])
                self.db.commit()
                option = input("Delete student successfully! Do you want to continue? 1.yes 2.no")
                if option == '2':
                    print("Leaving delete option...")
                    sleep(0.5)
                    break
            except Exception as e:
                print(e)
                self.db.rollback()

    def add_image(self, table):
        while True:
            try:
                print("Please enter the student you want to add image to:")
                name = input("Name:")
                filename = input("Please upload the image:")
                with open(filename, 'rb') as f:
                    data = f.read()
                sql = 'update %s' % (table)
                sql = sql + " set image = %s where name = %s"
                self.cur.execute(sql, [data, name])
                self.db.commit()
                self.show_image(name, table)

                option = input("Add student image successfully! Do you want to continue? 1.yes 2.no")
                if option == '2':
                    print("Leaving delete option...")
                    sleep(0.5)
                    break
            except Exception as e:
                print(e)
                self.db.rollback()

    def show_image(self, name, table):
        filename = str(name) + '.jpeg'
        file = open(filename, 'wb')
        sql = "select image from %s" % table
        sql = sql + " where name = %s ; "

        self.cur.execute(sql, [name])
        result = self.cur.fetchone()
        file.write(result[0])
        file.close()


def main():
    database = input("Please select your database.")
    control = Manager(database=database)
    control.program_start()
    control.cur.close()
    control.db.close()


if __name__ == '__main__':
    main()
