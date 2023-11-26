import mysql.connector
from mysql.connector import Error

# Connect to MySQL
def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='school_management',
            user='root',
            password='1234'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error: ", e)
        return None

# Register a new student with additional fields
def register_student(name, roll_number, age, address, student_class, dob):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO students (name, roll_number, age, address, class, dob) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, roll_number, age, address, student_class, dob))
            connection.commit()
            print("Student registered successfully")
            return cursor.lastrowid  # Return the student ID
        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Add a new course
def add_course(course_code, course_name):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO courses (course_code, course_name) VALUES (%s, %s)"
            cursor.execute(query, (course_code, course_name))
            connection.commit()
            print("Course added successfully")
            return cursor.lastrowid  # Return the course ID
        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# New function to link a student to a course
def link_student_to_course(student_id, course_id):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s)"
            cursor.execute(query, (student_id, course_id))
            connection.commit()
            print("Student linked to course successfully")
        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Add a new teacher
def add_teacher(name, teacher_code):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO teachers (name, teacher_code) VALUES (%s, %s)"
            cursor.execute(query, (name, teacher_code))
            connection.commit()
            print("Teacher added successfully")
            return cursor.lastrowid  # Return the teacher ID
        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Show the list of students
def show_students():
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM students"
            cursor.execute(query)
            students = cursor.fetchall()

            if not students:
                print("No students registered.")
            else:
                print("List of students:")
                for student in students:
                    print(f"Name: {student[1]}, Roll Number: {student[2]}, Age: {student[3]}, Address: {student[4]}, Class: {student[5]}, DOB: {student[6]}")

        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Show the list of courses
def show_courses():
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM courses"
            cursor.execute(query)
            courses = cursor.fetchall()

            if not courses:
                print("No courses added.")
            else:
                print("List of courses:")
                for course in courses:
                    print(f"Code: {course[1]}, Name: {course[2]}")

        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Show details of a specific student
def show_student_details():
    roll_number = input("Enter roll number of the student: ")
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM students WHERE roll_number = %s"
            cursor.execute(query, (roll_number,))
            student = cursor.fetchone()

            if not student:
                print(f"No student found with roll number {roll_number}.")
            else:
                print(f"Details of student with roll number {roll_number}:")
                print(f"Name: {student[1]}, Roll Number: {student[2]}, Age: {student[3]}, Address: {student[4]}, Class: {student[5]}, DOB: {student[6]}")

        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Add this function to link a teacher to a course
def assign_teacher_to_course():
    teacher_id = input("Enter teacher ID: ")
    course_id = input("Enter course ID: ")
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO course_teachers (teacher_id, course_id) VALUES (%s, %s)"
            cursor.execute(query, (teacher_id, course_id))
            connection.commit()
            print("Teacher assigned to course successfully")
        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Add this function to show courses by teacher
def show_courses_by_teacher():
    teacher_id = input("Enter teacher ID: ")
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT courses.course_code, courses.course_name FROM courses INNER JOIN course_teachers ON courses.id = course_teachers.course_id WHERE course_teachers.teacher_id = %s"
            cursor.execute(query, (teacher_id,))
            courses = cursor.fetchall()

            if not courses:
                print("No courses assigned to this teacher.")
            else:
                print("Courses assigned to this teacher:")
                for course in courses:
                    print(f"Code: {course[0]}, Name: {course[1]}")

        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Show the list of teachers
def show_teachers():
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM teachers"
            cursor.execute(query)
            teachers = cursor.fetchall()

            if not teachers:
                print("No teachers added.")
            else:
                print("List of teachers:")
                for teacher in teachers:
                    print(f"Name: {teacher[1]}, Teacher Code: {teacher[2]}")

        except Error as e:
            print("Error: ", e)
        finally:
            cursor.close()
            connection.close()

# Menu function
def menu():
    print("\n************* School Management System *************")
    print(          "1. Register a student   2. Show students")
    print(          "3. Show courses         4. Show details of a specific student")
    print(          "5. Show students by course   6. Add a new teacher")
    print(          "7. Show teachers        8. Assign teacher to course")
    print(          "9. Show courses by teacher   10. Quit")
    print("***************************************************")

# Example usage
while True:
    menu()
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        age = input("Enter student age: ")
        address = input("Enter student address: ")
        student_class = input("Enter student class: ")
        dob = input("Enter student date of birth (dob): ")
        student_id = register_student(name, roll_number, age, address, student_class, dob)

        # Link the student to a course
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        course_id = add_course(course_code, course_name)
        link_student_to_course(student_id, course_id)

    elif choice == '2':
        show_students()

    elif choice == '3':
        show_courses()

    elif choice == '4':
        show_student_details()

    elif choice == '5':
        show_students_by_course()

    elif choice == '6':
        name = input("Enter teacher name: ")
        teacher_code = input("Enter teacher code: ")
        add_teacher(name, teacher_code)

    elif choice == '7':
        show_teachers()

    elif choice == '8':
        assign_teacher_to_course()

    elif choice == '9':
        show_courses_by_teacher()

    elif choice == '10':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
