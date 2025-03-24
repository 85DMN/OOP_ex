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
 
students, lectorers = [],[]

best_student = Student('Ryou','Eman','man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python_ML']
students.append(best_student) 

best_student1 = Student('Natan','Ivanov','man')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Python_ML'] 
students.append(best_student1)

best_student2 = Student('Emma','Petrova','woman')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Python_ML'] 
students.append(best_student2)

reviwer = Reviewer("Some",'Buddy')
reviwer.courses_attached += ['Python']
reviwer.courses_attached += ['Python_ML']

reviwer1 = Reviewer("Ann",'Hunt')
reviwer1.courses_attached += ['Python']
reviwer1.courses_attached += ['Python_ML']

reviwer2 = Reviewer("Nik",'Spot')
reviwer2.courses_attached += ['Python']
reviwer2.courses_attached += ['Python_ML']

lector = Lecturer("Any",'Where')
lector.courses_attached += ['Python']
lector.courses_attached += ['Python_ML']
lectorers.append(lector)

lector1 = Lecturer("Mikhael",'Hunt')
lector1.courses_attached += ['Python']
lector1.courses_attached += ['Python_ML']
lectorers.append(lector1)

lector2 = Lecturer("Sam",'Spot')
lector2.courses_attached += ['Python']
lector2.courses_attached += ['Python_ML']
lectorers.append(lector2)

reviwer.rate_hw(best_student,'Python',10)
reviwer.rate_hw(best_student1,'Python',10)
reviwer.rate_hw(best_student2,'Python',10)
reviwer1.rate_hw(best_student,'Python',10)
reviwer1.rate_hw(best_student1,'Python',10)
reviwer1.rate_hw(best_student2,'Python',10)
reviwer2.rate_hw(best_student,'Python',9)
reviwer2.rate_hw(best_student1,'Python',9)
reviwer2.rate_hw(best_student2,'Python',9)

reviwer.rate_hw(best_student,'Python_ML',9)
reviwer.rate_hw(best_student1,'Python_ML',9)
reviwer.rate_hw(best_student2,'Python_ML',9)
reviwer1.rate_hw(best_student,'Python_ML',9)
reviwer1.rate_hw(best_student1,'Python_ML',9)
reviwer1.rate_hw(best_student2,'Python_ML',9)
reviwer2.rate_hw(best_student,'Python_ML',10)
reviwer2.rate_hw(best_student1,'Python_ML',10)
reviwer2.rate_hw(best_student2,'Python_ML',10)
 
best_student.ocenka_r(lector,'Python',10)
best_student.ocenka_r(lector1,'Python',10)
best_student.ocenka_r(lector2,'Python',10)
best_student1.ocenka_r(lector,'Python',10)
best_student1.ocenka_r(lector1,'Python',10)
best_student1.ocenka_r(lector2,'Python',10)
best_student2.ocenka_r(lector,'Python',9)
best_student2.ocenka_r(lector1,'Python',9)
best_student2.ocenka_r(lector2,'Python',9)

best_student.ocenka_r(lector,'Python_ML',10)
best_student.ocenka_r(lector1,'Python_ML',10)
best_student.ocenka_r(lector2,'Python_ML',10)
best_student1.ocenka_r(lector,'Python_ML',10)
best_student1.ocenka_r(lector1,'Python_ML',10)
best_student1.ocenka_r(lector2,'Python_ML',10)
best_student2.ocenka_r(lector,'Python_ML',9)
best_student2.ocenka_r(lector1,'Python_ML',9)
best_student2.ocenka_r(lector2,'Python_ML',9)

def srednee_po_vsem(parametr):
    statistika = {}
    for j in parametr:
        ty = list(j.grades.keys())
        for g in ty:
            if statistika.get(g) == None:
                statistika[g]=(sum(j.grades[g])/len(j.grades[g]))
            else:
                statistika[g]=(sum(j.grades[g])/len(j.grades[g])+statistika[g])/2                
    return statistika

print(srednee_po_vsem(students))
 
# print(best_student.grades)