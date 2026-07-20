# Анализ курсов студентов
#
# Реализовать программу, которая должна:
#
# Прочитать файл student_courses.json, содержащий:
#
# имя,
#
# дату рождения (birth_date) в формате дд.мм.гггг,
#
# дату поступления (enrollment_date) в том же формате,
#
# список курсов.
#
# Вычислить:
#
# Общее количество студентов.
#
# Средний возраст на момент поступления.
#
# Количество студентов на каждом курсе.
#
# Сохранить отчёт в JSON-файл student_courses_report.json.
#
# Данные:
#
# [
#
#   {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]}, 
#
#   {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]}, 
#
#   {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]}, 
#
#   {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]}, 
#
#   {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]}, 
#
#   {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]}, 
#
#   {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]}, 
#
#   {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]}, 
#
#   {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]}, 
#
#   ...
#
# ]
#
# Пример вывода (student_courses_report.json):
#
# {
#
#     "total_students": 100,
#
#     "average_enrollment_age": 27.9,
#
#     "students_per_course": {
#
#         "Art": 21,
#
#         "Biology": 18,
#
#         "Business": 28,
#
#         "Chemistry": 16,
#
#         "Economics": 23,
#
#         "History": 9,
#
#         "Linguistics": 23,
#
#         "Math": 23,
#
#         "Philosophy": 19,
#
#         "Physics": 19
#
#     }
#
# }


import json
import datetime

def get_age(date, birth_date):
    return (datetime.datetime.strptime(date, '%d.%m.%Y') - datetime.datetime.strptime(birth_date, '%d.%m.%Y')).days // 365.25

with open('students.json') as f:
    data = json.load(f)

    total_students = len(data)

    average_enrollment_age = int(sum(
        get_age(data[i]['enrollment_date'], data[i]['birth_date']) 
        for i in range(total_students)
    ) / total_students)
    
    students_per_course = {}
    
    for i in range(total_students):
        for course in data[i]['courses']:
            if course in students_per_course:
                students_per_course[course] += 1
            else:
                students_per_course[course] = 1
    
    with open('student_courses_report.json', 'w') as f:
        json.dump({'total_students': total_students, 'average_enrollment_age': average_enrollment_age, 'students_per_course': students_per_course}, f)

























