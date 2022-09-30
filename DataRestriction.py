import re



def Name():
    while True:  # taking name
        Name = input("Enter Your Name: ")
        if not re.match(r'^[a-zA-Z "     "]+$', Name) or len(Name) < 3:
            print("Name only consists letters please enter correct name and name should be more than 3 characters")
            continue
        break


def College():
     while True:  # taking college name
        College = input("Enter Your College Name: ")
        if not re.match(r'^[a-zA-Z "     "]+$', College) or len(College) < 3:
            print("Name only consists letters please enter correct name and name should be more than 3 characters")
            continue
        break


def Rollno ():
    while True:  # taking the roll number
        Rollno = input("Enter Your Roll Number: ")
        if not re.match(r'^[A-Za-z\d.-]+$', Rollno) or Rollno.isalnum():
            print("Enter the correct roll number inculcated year-course-roll number ")
            continue
        break

def Email():
    while True:  # taking email id
        Email = input("Enter your email id: ")
        if not re.match(r'\b[A-Za-z\d._%+-]+@[A-Za-z\d.-]+.[A-Z|a-z]{2,}\b', Email):
            print("Enter the correct email address")
            continue
        break

def Course():
    while True:  # taking course name
        Course = input("Enter your course name: ")
        if not re.match(r'^[a-zA-Z "     "]+$', Course) or len(Course) < 3:
            print("Enter the correct course")
            continue
        break

    # def Mobileno(self):
    #     while True:  # taking mobile number
    #         self.mobile = input("Enter the mobile number: \n(with country code): ")
    #         if not re.match(r'^\d{2}?[-\s]?[6-9]\d{9}$', self.mobile):
    #             print("Enter the valid mobile number")