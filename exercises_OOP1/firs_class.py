class Student:
    def __init__(self,name,student_id,courses):
        self.name=name
        self.student_id=student_id
        self.courses=courses

    def enroll(self,course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

student1= Student("eduardo","1",["applied mathematics"])
student1.enroll("programming")
student1.enroll("algebra")

print(student1.name)
print(student1.get_courses())


