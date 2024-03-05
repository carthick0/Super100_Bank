class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}"

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.grades = {}  # Student ID: Grade

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, grade):
        self.grades[student.student_id] = grade

    def __str__(self):
        return f"Course: {self.course_name}, Code: {self.course_code}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def get_student_gpa(self, student_id):
        total_grade = 0
        enrolled_courses = 0
        for course in self.courses:
            if student_id in course.grades:
                total_grade += course.grades[student_id]
                enrolled_courses += 1
        return total_grade / enrolled_courses if enrolled_courses > 0 else 0

    def __str__(self):
        return f"School with {len(self.students)} students and {len(self.courses)} courses"

# Example Usage
# Creating some students and courses
student1 = Student("Alice", "S001")
course1 = Course("freefire", "C101")

# Creating the school
school = School()
school.add_student(student1)
school.add_course(course1)

# Enrolling students in courses
student1.enroll(course1)
student2.enroll(course2)
student1.enroll(course2)

# Assigning grades
course1.assign_grade(student1, 3.5)
course2.assign_grade(student1, 4.0)
course2.assign_grade(student2, 3.7)

# Calculating GPA
print(f"{student1.name}'s GPA: {school.get_student_gpa(student1.student_id)}")
