# Importing all the necessary modules

import mysql.connector
from DataRestriction import Name, College, Rollno, Email, Course


# Defining a function enrollment student details update


def update():
    global edit, FULL_EDITING
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password21$',
        port='3306',
        database='student'

    )
    name = input('enter your Name: ')

    print(''' 1.roll no editing
              2.college name editing
              3.email id editing
              4.course editing
              5. edit full details''')
    choice = input('enter your option: ')
    if choice == '1':
        roll_no = input('enter new roll no: ')
        edit = """UPDATE student_system SET rollno='%s' where std_name='%s' """ % (roll_no, name)
    elif choice == '2':
        college = input('enter new collage: ')
        edit = """UPDATE student_system SET college_name='%s' where std_name='%s' """ % (college, name)
    elif choice == '3':
        email = input('enter new email: ')
        edit = """UPDATE student_system SET email_id='%s' where std_name='%s' """ % (email, name)
    elif choice == '4':
        course = input('enter new course: ')
        edit = """UPDATE student_system SET course_name='%s' where std_name='%s' """ % (course, name)
    elif choice == '5':
        roll_no = input('enter new roll no: ')
        Rollno()
        college = input('enter new collage: ')
        College()
        email = input('enter new email: ')
        Email()
        course = input('enter new course: ')
        Course()
        FULL_EDITING = f"UPDATE std_details set email_id ='{email}',std_name ='{name}',std_roll ='{roll_no}',clg_name ='{college}',course ='{course}' where std_name = '{name}' "
        Name(), Rollno(), College(), Email(), Course(),
    my_cursor = mydb.cursor()
    my_cursor.execute(edit)  # Executing the database
    my_cursor.execute(FULL_EDITING)  # Updating the database

    mydb.commit()  # Saving the info in database
    print(my_cursor.fetchall(), 'edited successfully')  # Fetching all the info
