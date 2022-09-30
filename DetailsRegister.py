# Defining the function to register the student details
def regis():
    import mysql.connector

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password21$',
        port='3306',
        database='student'

    )
    print('register the student')
    name = input('enter name: ')
    # Name()
    roll_no = input('enter roll no: ')
    # Roll_no()
    collage = input('enter college name: ')
    # College()
    email = input('enter email: ')
    # Email()
    course = input('enter your course: ')
    # Course()

    table = """insert into student_system values('%s','%s','%s','%s','%s')""" % (
        name, roll_no, collage, email, course)  # Adding the data  to database

    my_cursor = mydb.cursor()
    my_cursor.execute(table)  # Executing the table
    mydb.commit()  # Saving the details
    print(my_cursor.rowcount, 'record added successfully')

    details = """select*from student_system"""
    my_cursor.execute(details)  # Executing the details
    my_cursor.fetchall()  # Fetching the details
