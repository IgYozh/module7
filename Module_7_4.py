name_team_1 = "Мастера Кода"
name_team_2 = "Волшебники Данных"

score_team_1 = 40
score_team_2 = 42

def num(team1_num=0, team2_num=0):
    print('В команде %s участников: %x !' % (name_team_1, team1_num))
    print('Итого сегодня в командах участников: %s и %x !' % (team1_num, team2_num))

def time(team1_time=0, team2_time=0):
    time_1 = team1_time
    time_2 = team2_time

    print('Команда {} решила задач: {}!'.format(name_team_2, score_team_2))
    print('{} решили задачи за {} cек. !'.format(name_team_2, time_2))


def challenge_result(tasks_total=0, time_avg=0):
    print(f'Команды решили {score_team_1} и {score_team_2} задач')
    if score_team_1 > score_team_2:
        print(f'Результат битвы: победа команды {name_team_1} !')
    else:
        print(f'Результат битвы: победа команды {name_team_2} !')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')

num(team1_num=5, team2_num=6)
time(team1_time=1552.512, team2_time=2153.31451)
challenge_result(tasks_total=82, time_avg=45.2)