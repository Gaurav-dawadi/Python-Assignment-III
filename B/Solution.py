import pandas as pd
import datetime


print("----------------------------------------------")
print("!!!!!Welcome to IT Academy!!!!!")
print("----------------------------------------------")

print(" 1. Course Overview" "\n"
      " 2. Course Enrollment" "\n"
      " 3. All Students Info" '\n'
      " 4. Update Student Info" '\n'
      " 5. Delete Student Info")

print("----------------------------------------------")

choice = int(input("Choose any (1, 2, 3, 4 or 5) : "))


def courseEnquiry():

    with open("courseContent.txt", "r") as f:
        while True:
            data = f.read()
            if not data:
                break
            print(data)


def showStudentsInfo():

    df = pd.read_csv("studentInfo.csv", index_col='Name')
    return df


def updateStudentInfo():

    df = showStudentsInfo()
    nameofStudent = input("Enter name of the student whose info you want to update: ")
    return df.loc[nameofStudent]


if choice == 1:

    courseEnquiry()

elif choice == 2:

    enroll = input("Do you want to enroll in this course? (Y/N) : ")

    if enroll == "Y":

        name = input("Enter your name: ").title()
        address = input("Enter your address: ").title()
        date_joined = datetime.datetime.now()
        pay = input("Do you want to pay full? (Y/N) : ")

        if pay == "Y":
            pay = 'Rs 20000'+'(Paid)'
        elif pay == 'N':
            pay = 'Rs 10000'+'(Remaining)'

        course_completed = False

        with open("studentInfo.csv", "a") as enrollStudent:
            enrollStudent.write(name+' , '+address+' , '+str(date_joined)+' , '+pay+' , '+str(course_completed)+'\n')
            enrollStudent.close()
            print("----------------------------------")
            print("Record has been successfully Added")
            print("----------------------------------")

    elif enroll == 'N':
        print("                                                        ")
        print("----------Hope to see you soon in our Academy-----------")

elif choice == 3:
    print(showStudentsInfo())

elif choice == 4:
    print(updateStudentInfo())



















