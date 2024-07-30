# использование %
team1_num = 5
team2_num = 6
print('Использование %')
print('В команде Мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print()

# использование format()
score_2 = 42
team1_time = 18015.2
print('Использование format()')
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print()

# использование f-строк
score_1 = 40
score_2 = 42
print('Использование f-строк')
print(f'Команды решили {score_1} и {score_2} задач')

challenge_result = 'Мастера кода'
print(f'Результат битвы: победа команды {challenge_result}!')
print()

tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')