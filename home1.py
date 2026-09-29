class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender  
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 

class Reviewer(Mentor):  
    pass 

class Lecturer(Mentor):
    pass  

lectures = Lecturer('Иван', 'Иванов')  
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lectures, Mentor))  
print(isinstance(reviewer, Mentor))       
print(lectures.courses_attached)
print(reviewer.courses_attached)
