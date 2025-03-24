class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        m,l=0,0
        for gh in self.grades.values():
            m += sum(gh)
            l += len(gh)
        delim, delim_f = ', '.join(self.courses_in_progress),', '.join(self.finished_courses)
        m = f'Имя: {(self.name)}\nФамилия: {(self.surname)}\nСредняя оценка за домашние задания: {m/l}\nКурсы в процессе изучения: {delim}\nЗавершенные курсы: {delim_f}'
        return m

    def ocenka_r(self, lecturer, course, grade):
        if isinstance(lecturer,Mentor) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        # self.name = name
        # self.surname = surname
        # self.courses_attached = []
    
    def __str__(self):
        m,l=0,0
        for gh in self.grades.values():
            m += sum(gh)
            l += len(gh)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {m/l}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)