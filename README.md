# 📂 project Title 
  Collection Manipulator


Welcome to the **Student Data Organizer**! 📚
This is a simple **Python console-based application** used to manage student information easily.

## ✨ Features

The Student Data Organizer provides the following options:

1. ➕ **Add Student** – Add a new student's information.
2. 👀 **Display All Students** – View all stored student records.
3. ✏️ **Update Student Information** – Update name, age, grade, or subjects.
4. 🗑️ **Delete Student** – Remove a student's record.
5. 📖 **Display Subjects Offered** – Display all unique subjects offered.
6. 🚪 **Exit** – Exit the application

## 🛠️ Technologies Used

* 🐍 **Python** – Used to develop the Student Data Organizer application.
* 💻 **Visual Studio Code (VS Code)** – Used for writing, editing, and running the Python code.
* 🌿 **Git** – Used for version control and tracking changes in the project.
* 🐙 **GitHub** – Used to store, manage, and share the project online.


## 📂 Project Structure

```text
Student-Data-Organizer/

├── 📄 main.py
├── 📄 output.png 
├── 📄 README.md
```
## output
![program output](output.png)

## 👨‍🎓 Student Information

The program stores the following information:

* 🆔 Student ID
* 👤 Student Name
* 🎂 Student Age
* 🏫 Student Grade
* 📅 Date of Birth
* 📚 Subjects

## ▶️ How to Run

### 1️⃣ Install Python

Make sure Python is installed on your computer.

Check Python installation:

```bash
python --version
```

### 2️⃣ Run the Program

Open the terminal in the project folder and run:

```bash
python student_data_organizer.py
```

## 🖥️ Main Menu

When the program starts, it displays:

```text
🎓 Welcome to the student Data Organizer!

Select an option:

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter Your Choice:
```

## ➕ Add Student

Select **Option 1** to add a student.

The program asks for:

```text
Enter Student Id:-
Enter Student Name:-
Enter Student Age:-
Enter Student Grade:-
Enter Student dob (YYYY-MM-DD):
Enter subjects (comma-separated):
```

Example:

```text
Enter Student Id:- 101
Enter Student Name:- Rahul
Enter Student Age:- 20
Enter Student Grade:- A
Enter Student dob (YYYY-MM-DD): 2006-05-15
Enter subjects (comma-separated): Python,Java,C++
```

✅ Student Added Successfully!

## 👀 Display Students

Select **Option 2** to display all students.

Example:

```text
Student ID is: 101
Student Name is: Rahul
Student Age is: 20
Student Grade is: A
Student Subjects are: {'Python', 'Java', 'C++'}
Student DOB is: 2006-05-15
```

## ✏️ Update Student

Select **Option 3** and enter the Student ID.

You can update:

```text
1. Update Name
2. Update Age
3. Update Subjects
4. Update Grade
5. STOP
```

This allows student information to be modified without deleting the complete record. 🔄

## 🗑️ Delete Student

Select **Option 4** and enter the Student ID.

The matching student record will be removed from the list.

```text
Student Removed Successfully.
```

## 📚 Display Subjects Offered

Select **Option 5** to display all unique subjects stored in student records.

Example:

```text
Python
Java
C++
Database
```

The program uses a **set** so duplicate subjects are automatically removed. ✨

## 🧠 Python Concepts Used

### 📋 List

The `students` list stores all student records.

```python
students = []
```

### 📦 Dictionary

Each student's information is stored using a dictionary.

```python
student = {
    "name": name,
    "age": age,
    "grade": grade,
    "subjects": sub,
    "info": id_dob
}
```

### 🔢 Tuple

Student ID and DOB are stored together in a tuple.

```python
id_dob = (id, dob)
```

### 🔤 Set

Subjects are stored as a set to avoid duplicate subjects.

```python
sub = set(subjects.split(","))
```

### 🔄 While Loop

The `while True` loop keeps the program running until the user selects **Exit**.

### 🔁 For Loop

For loops are used to search and display student records.

## 🎯 Project Objective

The main objective of this project is to create a simple Python-based system that can **store, display, update, and delete student information** efficiently.

## 🌟 Advantages

* ✅ Easy to use
* ⚡ Fast data management
* 📚 Simple student record handling
* 🔄 Easy to update information
* 🗑️ Easy to delete records
* 📖 Displays unique subjects
* 🐍 Helps understand Python data structures

## 🚀 Future Scope

The project can be improved in the future by adding:

* 💾 File/database storage
* 🔐 Admin login system
* 🔍 Student search functionality
* 📊 Student marks and result management
* 📈 Student performance reports
* 🖥️ Graphical User Interface (GUI)
* 🗄️ MySQL database connectivity

## Author
  parmar vishal
T---

### License

* This project is created for learning and educational purposes.
