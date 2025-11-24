# Student Report System - OOP Version (Improved & Structured)

class Student:
    def __init__(self, name):
        """Initialize a Student with a name and an empty list of grades."""
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the student's grades list."""
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"❌ Invalid grade {grade}. Must be between 0 and 100.")

    def calculate_average(self):
        """Calculate the average of the student's grades."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def display_info(self):
        """Display the student's name, grades, and average."""
        print(f"\n📘 Student: {self.name}")
        print(f"Grades: {self.grades if self.grades else 'No grades entered'}")
        print(f"Average: {self.calculate_average():.2f}")
        print("-" * 30)


def input_students():
    """Interactively collect student and grade data."""
    students = []

    print("Welcome to the Student Report System!")
    print("Enter student names. Type 'done' when finished.\n")

    while True:
        name = input("Enter student name (or 'done'): ").strip()

        if name.lower() == "done":
            break
        if name == "":
            print("❌ Name cannot be empty.")
            continue

        student = Student(name)

        print(f"➡ Enter grades for {name} (0–100). Type 'done' to finish.")

        while True:
            grade_input = input("Enter grade: ").strip()

            if grade_input.lower() == "done":
                break

            try:
                student.add_grade(float(grade_input))
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")

        students.append(student)
        print(f"✔ Added {name} with {len(student.grades)} grades.\n")

    return students


def display_summary(students):
    """Display all students and their grade summaries."""
    print("\n========== Student Summary ==========")

    for student in students:
        student.display_info()


def calculate_class_average(students):
    """Calculate the overall class average."""
    all_grades = [grade for student in students for grade in student.grades]
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


def main():
    students = input_students()

    if not students:
        print("No students added. Exiting.")
        return

    display_summary(students)

    class_avg = calculate_class_average(students)
    print(f"\n🏫 Class Average: {class_avg:.2f}\n")


if __name__ == "__main__":
    main()
