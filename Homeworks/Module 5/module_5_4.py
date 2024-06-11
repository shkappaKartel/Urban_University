class Building:
    total = 0

    def __init__(self):
        Building.total += 1


buildings = [Building() for quantity in range(40)]

print(f'Всего было создано обьектов класса Building: {Building.total}')
