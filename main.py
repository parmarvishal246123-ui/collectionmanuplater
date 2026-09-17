print("Welcome to the student Data Organizer!")

students=[]

while True:
      print()
      print("Select an option:")
      print("1.Add Student")
      print("2.Display All Students")
      print("3.Update Student Information")
      print("4.Delete Student")
      print("5.Display Subjects Offered")
      print("6.Exit")
      print()

      choice=int(input("Enter Your Choice"))

      if choice == 1:
          print()
          id = int(input("Enter Student Id:- "))
          name = input("Enter Student Name:- ")
          age = int(input("Enter Student Age:- "))
          grade = input("Enter Student Grade:- ")
          dob = input("Enter Student dob (YYYY-MM-DD):  ")
          subjects = input("Enter subjects (comma-separeted): ")

          id_dob=(id,dob)
          sub=set(subjects.split(","))

          dict={"name":name,
                "age":age,
                "grade":grade,
                "subjects":sub,
                "info":id_dob
                }
          students.append(dict)
          print("Student Added Succesfully")


      elif choice == 2:
            print()
            if len(students) != 0:
              for std in students:
                  print(f"Student ID is: {std['info'][0]} | Student Name is: {std['name']} | Student Age is: {std['age']} | Student Grade is: {std['grade']} | Student Subjects are: {(std['subjects'])} | Student DOB is: {std['info'][1]}")


            else:
              print("Student Not Found!")

      elif choice == 3:
            print()
            id=int(input("Enter Student ID:"))
            for std in students:
                if std["info"][0] == id:
                    while True:
                        print("1.Update Name")
                        print("2.Update Age")
                        print("3.Update Subjects")
                        print("4.Update Grade")
                        print("5.STOP")

                        ch=int(input("Enter Your Option: "))

                        if ch == 1:
                            name= input("Enter New Name: ")
                            std["name"]=name

                        elif ch == 2:
                            age= int(input("Enter New Age: "))
                            std["age"]=age

                        elif ch == 3:
                            sub= input("Enter New Subjects: ")
                            std["subjects"]=set(sub.split(","))

                        elif ch == 4:
                            grade= input("Enter New Grade: ")
                            std["grade"]=grade

                        elif ch == 5:
                            print("STOP!")
                            break
                        else:
                            print("Enter Valid Choice")
                            

                else:
                    print("Student Data Not Found")

      elif choice ==4:
            print()
            if len(students) != 0:
                id = int(input("Enter Student ID: "))
                for std in students:
                    if std["info"][0] == id:
                        students.remove(std)
                        print("Student Removed Succesfully.")


      elif choice == 5:
        a=set()
        for std in students:
            for sub in std["subjects"]:
                a.add(sub)
        print()
        for sub in a:
            print(sub)

      elif choice == 6:
         print("Thank you for using Student data organizer..")
         break
        