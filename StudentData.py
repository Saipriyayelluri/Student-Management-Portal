# Importing all the modules to the main file
import mysql.connector
from DatapassingLL import LinkedList, Node
from DetailsUpdation import update
from DetailsRegister import regis
from PersonDetail import fetch_info

# Welcoming the user &asking the user
print("""
*********************************************************
!!!!!!!!! WELCOME TO STUDENT MANAGEMENT PORTAL!!!!!!!!!!!
*********************************************************
1.Do you want to register student 
2.Do you want to see the detail of student
 """)
# Taking the user choice
user = input('Enter your choice: ')
# If user opt to choose one the below data will run
if user == '1':
    llist = LinkedList()
    llist.head = Node(regis())
    print("Do you want to save this information - (y/n)")  # asking the user to save the info or not
    choice = input("Enter the option : ")
    if choice == 'y':  # user opt to choose yes the below code will run
        print(
            "The Details have been saved successfully !!\n Do you want to continue => PRESS1:"
            "\n Do you want to quit =>PRESS2:")
        choice1 = input("Enter your choice:")  # Asking the user option to choose
        if choice1 == '1':
            print("1.Do you want to register student \n 2.Do you want to see the detail of student")
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                llist = LinkedList()
                llist.head = Node(regis())
            elif user_choice == '2':
                fetch_info()
        else:
            quit()
    # If user choice is no the below code will run
    elif choice == 'n':
        print("Do you want to edit this information -1 \n Do you want to Quit - 2")  # Asking the user
        user = input('Enter your choice: ')  # If opt is 1 update will be done
        if user == '1':
            update()
            client = input("Enter your choice : ")
            if client == 'y':  # Asking to save the info or not
                print("The details have been saved successfully!!!")
            elif client == 'n':
                quit()  # Exiting the program
elif user == '2':
    fetch_info()  # Fetches the users info
