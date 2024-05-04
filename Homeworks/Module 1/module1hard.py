

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = {} # словарь для учеников и сред. балла

# i - достаёт балл, student - имя студента
for i, student in enumerate(students):
    grades_sum = sum(grades[i])
    average_grades[student] = grades_sum / len(grades[i])

print(average_grфades)
