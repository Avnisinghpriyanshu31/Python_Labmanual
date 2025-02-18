class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)
        
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Enrolled in: {[course.course_name for course in self.courses]}"

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.courses = []

    def teach_course(self, course):
        self.courses.append(course)
        course.assign_teacher(self)
    
    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}, Teaching: {[course.course_name for course in self.courses]}"

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher
        
    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Teacher: {self.teacher.name if self.teacher else 'No Teacher Assigned'}, Students: {[student.name for student in self.students]}"

student1 = Student(1, "Avni", 20)
student2 = Student(2, "Rishe", 19)

teacher1 = Teacher(101, "Mr. Rupesh", "PYTHON")
teacher2 = Teacher(102, "Ms. Patel", "English")

course1 = Course(1001, "PYTHON")
course2 = Course(1002, "English Literature")


student1.enroll_in_course(course1)
student2.enroll_in_course(course1)
student2.enroll_in_course(course2)


teacher1.teach_course(course1)
teacher2.teach_course(course2)


print(student1)
print(student2)
print(teacher1)
print(teacher2)
print(course1)
print(course2)
