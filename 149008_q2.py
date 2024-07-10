class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students in the classroom.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                avg = student.get_average_grade()
                print(f"Average grade for {student.name}: {avg:.2f}")
                return
        print(f"No student found with the name {student_name}.")

    def get_class_average_for_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades recorded for the subject {subject}.")
        else:
            avg = total / count
            print(f"Class average for {subject}: {avg:.2f}")


# Demonstration of functionalities
def main():
    classroom = Classroom()

    while True:
        print("\nSchool Class Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Get the average grade of a student")
        print("4. Get the class average for a subject")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student's name: ")
            student = Student(name)
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                student.add_grade(subject, grade)
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_all_students()
        elif choice == '3':
            name = input("Enter student's name: ")
            classroom.get_student_average(name)
        elif choice == '4':
            subject = input("Enter subject: ")
            classroom.get_class_average_for_subject(subject)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
