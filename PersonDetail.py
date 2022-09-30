# importing modules
import mysql.connector


def fetch_info():             # defining function for retrieving
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password21$',
        port='3306',
        database='student'

    )
    print('For fetching the details of the student please enter the name of student ')
    name = input('enter student name: ')

    retriev = """ select*from student_system where std_name='%s'""" % name
    my_cursor = mydb.cursor()
    my_cursor.execute(retriev)
    row= my_cursor.fetchall()
    for row in row:
        print("NAME : ", row[0])
        print("ROLL_NO   : ", row[1])
        print("COLLEGE_NAME :", row[2])
        print("EMAIL :", row[3])
        print("COURSE :", row[4])
        mydb.close()
