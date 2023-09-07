from students.education import Student
from students.disciplines import Discipline

if __name__ == '__main__':
    student_1 = Student('Иванов', 'Иван', 'Иванович')
    student_2 = Student('Смирнов', 'Мирон', 'Григорьевич')
    student_3 = Student('Иванова', 'Елена', 'Ивановна')
    student_4 = Student('Смирнова', 'Милана', 'Григорьевна')

    print(student_1)
    print(student_2)
    print(student_3)
    print(student_4)

    # Добавить дисциплины
    student_1.append_to_progress(Discipline('Математика', 5, 100))
    student_1.append_to_progress(Discipline('Физика', 5, 50))
    student_1.append_to_progress(Discipline('Химия', 3, 30))

    print(student_1.short_name)
    print(student_1.show_progress())

    print(student_2.short_name)
    print(student_2.show_progress())

    student_1.save_progress()

    # Удалить Иванова
    del student_1

    # Создать Иванова заново - Дисциплины должны подгрузиться из файла
    student_1_1 = Student('Иванов', 'Иван', 'Иванович')
    print(student_1_1.short_name)
    print(student_1_1.show_progress())