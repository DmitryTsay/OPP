from home2 import student, reviewer


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        if len(all_grades) == 0:
            return 0
        return round(sum(all_grades) / len(all_grades), 2)


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        if len(all_grades) == 0:
            return 0
        return round(sum(all_grades) / len(all_grades), 2)


    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.average_grade()}'
        return res

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


def average_hw_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    if len(all_grades) == 0:
        return 0
    return round(sum(all_grades) / len(all_grades), 2)

def average_lecture_grade(lecturer, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    if len(all_grades) == 0:
        return 0
    return round(sum(all_grades) / len(all_grades), 2)

student1 = Student('Иван', 'Иванов', 'М')
student2 = Student('Анна', 'Петрова', 'Ж')
lecturer1 = Lecturer('Петр', 'Сидоров')
lecturer2 = Lecturer('Максим', 'Максимов')
reviewer1 = Reviewer('Симон', 'Антонов')
reviewer2 = Reviewer('Екатерина', 'Смирнова')

student1.courses_in_progress += ['Python', 'Git']
student1.add_courses('Введение в програмирование')
student2.courses_in_progress += ['Python']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python', 'Git']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Git', 7)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)

print(student1 > student2)
print(student1 == student2)
print(lecturer1 < lecturer2)
print(lecturer1 >= lecturer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]
print(average_hw_grade(students, 'Python'))
print(average_hw_grade(students, 'Git'))
print(average_hw_grade(students, 'Java'))
print(average_lecture_grade(lecturers, 'Python'))   
print(average_lecture_grade(lecturers, 'Git'))