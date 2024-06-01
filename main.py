class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rating):
        if course not in lecturer.courses_attached:
            print(f'Лектор {lecturer.name} {lecturer.surname} не закреплён за курсом {course}')
            return
        if course not in self.courses_in_progress:
            print(f'Студент {self.name} {self.surname} не записан на курс {course}')
            return
        lecturer.ratings[course].append(rating)
        print(f'Студент {self.name} {self.surname} поставил оценку {rating} лектору {lecturer.name} {lecturer.surname} '
              f'за курс {course}')

    def get_average_grade(self):
        total_grades = sum(self.grades.values())
        total_assignments = len(self.grades)
        return total_grades / total_assignments if total_assignments else 0.0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.ratings = {course: [] for course in courses_attached}

    def get_average_rating(self):
        total_ratings = sum(sum(ratings) for ratings in self.ratings.values())
        total_lectures = sum(len(ratings) for ratings in self.ratings.values())
        return total_ratings / total_lectures if total_lectures else 0.0

    def __str__(self):
        average_rating = self.get_average_rating()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}"

    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()

    def __le__(self, other):
        return self.get_average_rating() <= other.get_average_rating()

    def __gt__(self, other):
        return self.get_average_rating() > other.get_average_rating()

    def __ge__(self, other):
        return self.get_average_rating() >= other.get_average_rating()

    def __eq__(self, other):
        return self.get_average_rating() == other.get_average_rating()

    def __ne__(self, other):
        return self.get_average_rating() != other.get_average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

    def check_homework(self, student, course, grade):
        if course not in self.courses_attached:
            print(f"Эксперт {self.name} {self.surname} не закреплен за курсом {course}")
            return
        if course not in student.courses_in_progress:
            print(f"Студент {student.name} {student.surname} не записан на курс {course}")
            return
        student.grades[course].append(grade)
        print(f'Эксперт {self.name} {self.surname} проверил домашнюю работу у студента {student.name} {student.surname} '
              f'по курсу {course} с оценкой {grade}')

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.extend(['Python'])

cool_reviewer = Reviewer('Some', 'Buddy', ['Python'])

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)