
class Student:
    """
    Represents a student and stores academic information.
    Calculates and displays individual academic summaries.
    """

    def __init__(self, full_name, admission_number, course_name, marks):
        
        self.full_name = full_name
        self.admission_number = admission_number
        self.course_name = course_name
        self.marks = marks



    
    def display_profile(self):
        print("\n------ STUDENT PROFILE ------")
        print("Full Name:", self.full_name)
        print("Admission Number:", self.admission_number)
        print("Course:", self.course_name)
        print("Marks:", self.marks)
        print("Average Marks:", self.calculate_average())

    
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)




student1 = Student(
    "John Kamau",
    "ADM001",
    "Information Technology",
    [75, 80, 85, 90]
)

student2 = Student(
    "Mary Wanjiku",
    "ADM002",
    "Computer Science",
    [65, 70, 75, 80]
)

student3 = Student(
    "Peter Otieno",
    "ADM003",
    "Business Management",
    [80, 85, 90, 95]
)



print("INITIAL STUDENT ACADEMIC SUMMARIES")

students = [student1, student2, student3]

for student in students:
    student.display_profile()




print("\n------ UPDATING STUDENT MARKS ------")

student1.marks = [90, 85, 95, 100]

print("John Kamau's marks have been updated.")




print("\nUPDATED ACADEMIC SUMMARIES")

for student in students:
    print(
        student.full_name,
        "- Average:",
        student.calculate_average()
    )



print("\nVERIFYING OTHER STUDENTS' DATA")

student2.display_profile()
student3.display_profile()
