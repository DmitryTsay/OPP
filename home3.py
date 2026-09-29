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


some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [10, 9, 10, 10, 10]}
print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 'Ж')
some_student.courses_in_progress += ['Python', 'Git']
some_student.add_courses('Введение в программирование')
some_student.grades = {'Python': [10, 10, 9, 10], 'Git': [10, 10, 10, 9]}
print(some_student)

second_lecturer = Lecturer('Second', 'Buddy')
second_lecturer.grades = {'Python': [8, 9]}
print(some_lecturer > second_lecturer)
print(some_lecturer < second_lecturer)

second_student = Student('Second', 'Eman', 'Ж')
second_student.grades = {'Python': [10, 10]}
print(some_student < second_student)
print(some_student == second_student)