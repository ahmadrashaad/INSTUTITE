
class Student:
    """
    A class representing a student in a training institute.
    Stores student details and calculates academic averages.
    """

    def __init__(self, full_name, admission_number, course_name, marks):
        self.full_name = full_name
        self.admission_number = admission_number
        self.course_name = course_name
        self.marks = marks

    def display_profile(self):
        """Display the student's academic profile."""
        print("\n----- STUDENT PROFILE -----")
        print("Full Name:", self.full_name)
        print("Admission Number:", self.admission_number)
        print("Course Name:", self.course_name)
        print("Marks:", self.marks)
        print("Average:", round(self.calculate_average(), 2))

    def calculate_average(self):
        """Calculate and return the student's average marks."""
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)


student1 = Student(
    "John Kamau",
    "ADM001",
    "Computer Science",
    [75, 80, 85, 90]
)

student2 = Student(
    "Mary Wanjiku",
    "ADM002",
    "Information Technology",
    [65, 70, 75, 80]
)

student3 = Student(
    "Peter Mwangi",
    "ADM003",
    "Software Engineering",
    [88, 92, 85, 95]
)


students = [student1, student2, student3]


print("INITIAL STUDENT PROFILES")

for student in students:
    student.display_profile()


print("\nUPDATING JOHN KAMAU'S MARKS")

student1.marks = [90, 85, 95, 100]


print("\nUPDATED STUDENT AVERAGES")

for student in students:
    print(
        student.full_name,
        "- Average:",
        round(student.calculate_average(), 2)
    )
