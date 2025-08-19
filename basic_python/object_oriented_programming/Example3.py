class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def enroll(self, course):
        print(f"{self.name} is enrolled in {course}")

s1 = Student("Rahma Lindungi Laowo", "Information Technology")
s1.enroll("Python Programming")