import logging

logging.basicConfig(filename="student_management.log",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

students = {1: {'fname': 'sohan', 'lname': 'borawar', 'contact': 7069476530, 'subjects': {'python': {'marks': 89, 'fees': 80000}, 'java': {'marks': 78, 'fees': 90000}}, 'faculty': 'jigar'}, 34: {'fname': 'pre', 'lname': 'patel', 'contact': 456789432, 'subjects': {'java': {'marks': 87, 'fees': 65000}, 'web': {'marks': 87, 'fees': 87000}, 'php': {'marks': 79, 'fees': 23000}}, 'faculty': 'falguni'}, 65: {'fname': 'vishal', 'lname': 'yadav', 'contact': 123456789, 'subjects': {'design': {'marks': 93, 'fees': 67000}, 'figma': {'marks': 85, 'fees': 87000}}, 'faculty': 'parth'}}



def student_add(serial_num,fname,lname,contact,faculty):
    if serial_num in students:
        print("The entered serial nmuber is already avaliable in the database")
        logging.warning("The entered serial nmuber is already avaliable in the database")
    else:
        students[serial_num] = {
            "fname": fname,
            "lname": lname,
            "contact": contact,
            "subjects": {},
            "faculty":faculty
        }
        print("Student data entered successfully.")
        logging.info("Student data entered successfully.")

def add_subject(serial_num,subject,marks,fees,subject2,marks2,fees2):
    if serial_num in students:
        students[serial_num]["subjects"][subject] = {"marks":marks,"fees":fees}
        students[serial_num]["subjects"][subject2] = {"marks":marks2,"fees":fees2}
        print("Student marks data entered successfully.")
        logging.info("Student marks data entered successfully.")
        print()
    else:    
        print("entered serial number doesnot exsist")
        logging.warning("entered serial number doesnot exsist")


def remove_student(serial_num):
    if serial_num in students:
        del students[serial_num]     
        print("student removed successfully")                                  #del is used remove the student from database
        logging.info("student removed successfully")
    else:
        print("entered serial number doesnot exsist")
        logging.warning("entered serial number doesnot exsist")

def view_allstudent():
    if students :
        for serial_num,student in students.items():
            print(f"Serial Number :{serial_num}")
            print(f"Student Name :{student['fname']} {student['lname']}")
            print(f"Contact Number :{student['contact']}")
            print(f"faculty Name :{student['faculty']}")
            if student['subjects']:
                for subject,values in student['subjects'].items():
                    print(f" {subject} : Marks - {values['marks']},Fees- {values['fees']}")
                    print()
            else:
                print("There are No Subjects")
                logging.warning("There are No Subjects")
    else:
        print("There is no data avaliable")    
        logging.warning("There is no data avaliable")

def view_specific_student(serial_num):
    if serial_num in students:
        student = students[serial_num]
        print(f"Serial Number : {serial_num}")
        print(f"Student Name : {student['fname']} {student['lname']}")
        print(f"Contact : {student['contact']}")
        print("subjects :")
        if student['subjects']:
            for subject,values in student['subjects'].items():
                print(f"{subject} : Marks - {values['marks']},Fees - {values['fees']}")
        logging.info(f"view_specific_student{(serial_num)}")        
    else:
        print("entered serial number doesnot exsist")
        logging.warning("entered serial number doesnot exsist")




# >>>>>>>>>>>>>>>>>>>>>>>>>>Display Side<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<






while True:
    print("press 1 for counseller")
    print("press 2 for faculty")
    print("press 3 for student")
    print("press 4 for Exit") 
    print()
    role_id = int(input("enter role id :"))
    print()
    while role_id == 1 :
        logging.info("Counseller Loged IN")
        
        print("1.Add student")
        print("2.Remove student")
        print("3.View all student")
        print("4.View specific student")
        print("5.Get back to main menu")
        print()

        counseller_choice = int(input("A choice by counseller :"))

        if counseller_choice ==1:
            logging.info("Add Student Selected")

            serial_num  = int(input("Enter Serial number :"))
            fname = input("Enter first name of student :")
            lname = input("Enter last name of student :")
            contact = int(input("Enter contact number :"))
            subject = input("Enter Subject :")
            marks = int(input("Enter marks :"))
            fees = int(input("Enter fees :"))
            subject2 = (input("Enter subject :"))
            marks2 = int(input("Enter marks :"))
            fees2 = int(input("Enter fees :"))
            faculty = input("Enter faculty :")

            student_add(serial_num,fname,lname,contact,faculty)
            add_subject(serial_num,subject,marks,fees,subject2,marks2,fees2)
            print()

        elif counseller_choice == 2:
            logging.info("Remove Student Selected")

            print("To remove student")
            print()
            serial_num = int(input("Enter serial number :"))
            remove_student(serial_num)
            print()

        elif counseller_choice == 3:
            logging.info("View All Student Selected")
            
            print()
            view_allstudent()
            print()
           
        elif counseller_choice == 4:
            logging.info("View Specific Student Selected")

            print(">>>>>>>view specific student<<<<<<<<<")
            serial_num = int(input("Enter serial number :"))
            print()
            view_specific_student(serial_num)
            print()
            
        elif counseller_choice == 5:
            logging.info("Getting back to main menu")

            print("Thank you >Getting back to main menu<")
            break

        else:
            logging.warning("Invalid input")
            print("invalid input")    

    while role_id == 2 :
        logging.info("Faculty Loged IN")

        print("1.Add marks of student")
        print("2.View all student")
        print("3.Get back to main menu")


        faculty_choice = int(input("Enter a choice by faculty :"))

        if faculty_choice == 1:
            logging.info("Add Marks Of Student Selected")

            serial_num = int(input("Enter serial number :"))
            if serial_num in students:
                subject = input("Enter the subject :")
                marks = int(input("Enter marks :"))
                fees = int(input("Enter fees :"))
                subject2 = input("Enter the other subject :")
                marks2 = int(input("enter marks :"))
                fees2 = int(input("Enter fees :"))
                add_subject(serial_num,subject,marks,fees,subject2,marks2,fees2)
                print()
                

            else:
                logging.warning("The entered serial does not exist")
                print("The entered serial does not exist")
                  

        elif faculty_choice == 2:
            logging.info("View All Student Selected")
            print("view all student")        
            view_allstudent()
            print()

        elif faculty_choice == 3:
            logging.info("Getting back to main menu")
            print("Thank you >Getting back to main menu<")
            break
        else :
            logging.warning("Invalid Input")
            print("invalid input")

    if role_id == 3 :
        logging.info("Sudent Loged In")

        print("Enter your Serial Number to view your details")
        serial_num = int(input("Enter your serial number :")) 
        view_specific_student(serial_num)
        print()
        print("For any other Quries Contact faculty")
        print()

    if role_id == 4:
        logging.info("Exit The Program")
        print(students)
        break