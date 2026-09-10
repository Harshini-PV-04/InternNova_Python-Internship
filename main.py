# ============================================================
# STUDENT MANAGEMENT SYSTEM
# Week 6 - Final Python Project
# ============================================================

from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# ABSTRACT CLASS
# ============================================================

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_role(self):
        pass


# ============================================================
# STUDENT CLASS - INHERITANCE
# ============================================================

class Student(Person):

    def __init__(self, name, age, course, marks):
        super().__init__(name, age)

        # Encapsulation: private attribute
        self.__marks = marks

        self.course = course

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")

    # Method
    def display_role(self):
        print("Role: Student")

    # Calculate grade
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 50:
            return "D"
        else:
            return "F"

    # Display student information
    def display_info(self):
        print("\n-----------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.__marks)
        print("Grade:", self.calculate_grade())
        print("-----------------------------")


# ============================================================
# TEACHER CLASS - POLYMORPHISM
# ============================================================

class Teacher(Person):

    def display_role(self):
        print("Role: Teacher")


# ============================================================
# STUDENT MANAGEMENT CLASS
# ============================================================

class StudentManagementSystem:

    def __init__(self):
        # Dictionary used as data structure
        self.students = {}

        # Automatically generate student IDs
        self.next_id = 1

    # --------------------------------------------------------
    # ADD STUDENT
    # --------------------------------------------------------

    def add_student(self):

        print("\n===== ADD STUDENT =====")

        try:
            name = input("Enter student name: ")

            age = int(input("Enter age: "))

            course = input("Enter course: ")

            marks = float(input("Enter marks: "))

            if age <= 0:
                print("Age must be greater than 0.")
                return

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            student = Student(name, age, course, marks)

            # Assign student ID
            student.student_id = self.next_id

            # Store object inside dictionary
            self.students[self.next_id] = student

            self.next_id += 1

            print("\nStudent added successfully!")

        except ValueError:
            print("\nError: Please enter valid numeric values.")


    # --------------------------------------------------------
    # VIEW ALL STUDENTS
    # --------------------------------------------------------

    def view_students(self):

        print("\n===== ALL STUDENTS =====")

        if not self.students:
            print("No student records found.")
            return

        for student in self.students.values():
            student.display_info()


    # --------------------------------------------------------
    # SEARCH STUDENT
    # --------------------------------------------------------

    def search_student(self):

        print("\n===== SEARCH STUDENT =====")

        try:
            student_id = int(input("Enter Student ID: "))

            if student_id in self.students:
                self.students[student_id].display_info()
            else:
                print("Student not found.")

        except ValueError:
            print("Invalid Student ID.")


    # --------------------------------------------------------
    # UPDATE MARKS
    # --------------------------------------------------------

    def update_marks(self):

        print("\n===== UPDATE MARKS =====")

        try:
            student_id = int(input("Enter Student ID: "))

            if student_id in self.students:

                marks = float(input("Enter new marks: "))

                self.students[student_id].set_marks(marks)

                print("Marks updated successfully.")

            else:
                print("Student not found.")

        except ValueError:
            print("Please enter valid numeric values.")


    # --------------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------------

    def delete_student(self):

        print("\n===== DELETE STUDENT =====")

        try:
            student_id = int(input("Enter Student ID: "))

            if student_id in self.students:

                del self.students[student_id]

                print("Student deleted successfully.")

            else:
                print("Student not found.")

        except ValueError:
            print("Invalid Student ID.")


    # --------------------------------------------------------
    # SAVE DATA TO FILE
    # --------------------------------------------------------

    def save_to_file(self):

        try:

            with open("students.txt", "w") as file:

                for student in self.students.values():

                    file.write(
                        f"{student.student_id},"
                        f"{student.name},"
                        f"{student.age},"
                        f"{student.course},"
                        f"{student.get_marks()},"
                        f"{student.calculate_grade()}\n"
                    )

            print("Student data saved successfully.")

        except Exception as error:
            print("Error while saving data:", error)


    # --------------------------------------------------------
    # SHOW CURRENT DATE AND TIME
    # --------------------------------------------------------

    def show_date_time(self):

        current_time = datetime.now()

        print("\nCurrent Date and Time:")
        print(current_time.strftime("%d-%m-%Y %H:%M:%S"))


# ============================================================
# POLYMORPHISM DEMONSTRATION
# ============================================================

def demonstrate_polymorphism():

    print("\n===== POLYMORPHISM DEMONSTRATION =====")

    student = Student("Harshini", 21,
                       "Computer Science Engineering", 90)

    teacher = Teacher("Dr. Kumar", 40)

    # Same method name, different behavior
    student.display_role()
    teacher.display_role()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    system = StudentManagementSystem()

    while True:

        print("\n")
        print("======================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Save Data to File")
        print("7. Show Date and Time")
        print("8. Demonstrate Polymorphism")
        print("9. Exit")
        print("======================================")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                system.add_student()

            elif choice == 2:
                system.view_students()

            elif choice == 3:
                system.search_student()

            elif choice == 4:
                system.update_marks()

            elif choice == 5:
                system.delete_student()

            elif choice == 6:
                system.save_to_file()

            elif choice == 7:
                system.show_date_time()

            elif choice == 8:
                demonstrate_polymorphism()

            elif choice == 9:

                print("\nThank you for using Student Management System!")
                break

            else:
                print("Please choose a number between 1 and 9.")

        except ValueError:

            print("Invalid input! Please enter a number.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()