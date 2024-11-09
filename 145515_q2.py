class Student:
    def __init__(self, student_id, assignments):
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' added for {self.name} with grade {grade}.")

    def display_grades(self):
        if self.assignments:
            print(f'Grades for {self.name}:')
            for assignment, grade in self.assignments.items():
                print(f'- {assignment}: {grade}')
            else:
                print(f'No grades available for {self.name}.')

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.list_of_students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f'Student with ID {student_id} not found.')

    def display_students_and_grades(self):
        if self.students:
            print(f"Students and grades for the course '{self.course_name}':")
            for student in self.students:
                print(f'\n{student.name} (ID: {student.student_id})')
                student.display_grades()
            else:
                print('No students enrolled in this course.')

if __name__ == "__main__":
    instructor = Instructor("Prof Owen", "Computer Science 202")

    while True:
        print("\nCourse Management System:")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and their grades")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter student's ID: ")
            assignment_name = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")

        elif choice == "3":
            instructor.display_students_and_grades()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
        