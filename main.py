student_list=[]

print("Welcome to the Student Data Organizer! ")
print()

while True:
    print("Select an Option")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information ")
    print("4. delete student")
    print("5.Display subjects Offered")
    print("6.exit")
    choice=int(input(" Enter your Choicen From 1-6 :"))
    print()
    if choice==1:
        print("Enter  Student details:" )
        student_id=int(input("Student ID: "))
        name=input("Name: ")
        age=int(input("Age:"))
        grade=input("Grade :")
        dob=int(input("Enter yout Date Of Birth(yyyy-mm-dd)"))
        subject=input("enter to a subject:").split(",")

        subject_set=set()
        for sub in subject:
            subject_set.add(sub.strip())




        std_info=(student_id,dob)
        student= {
            "student_id":student_id,
            "name":name,
            "age":age,
            "grade":grade,
            "subject":subject_set
            }
        student_list.append(student)
        print()
        print("student added successfully")
        print()

    elif choice==2:
        print("-------- Display All Students -------")  
        for student in student_list:
            print(f"student_id:{student['student_id']}|name{student['name']}|age:{student['age']}|grade{student['grade']}| subject{",".join(student['subject'])}")

    # elif choice==3:
    #     print("-----update your information-----")
    #     for student in student_list:
    #         if student_id

        



        

        
    elif choice==4:
        print("---- Delete Student----")
        student_id=int(input("Enter Student Id to delete:"))
        if student["student_id"]== student_id:
            student_list.remove(student)
            print()
            print("Student Deleted Successfully!")
            print()
        else:
            print(" Student Id is not found")
        

        
    elif choice==5:
        print("Display Subjects offered")
        s=set()
        for std in student_list:
            for subject in std["subject"]:
                s.add(subject)
            for subject in s:
                print (s)


               

                
    elif choice==6:
        print("Exiting this  progream goodbye...!")
        break

