import numpy as np

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
          'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

data = np.array([
    [1000, 1200, 1500, 1350, 1400, 1300, 1250, 1450, 1300, 1550, 1600, 1700],
    [800, 900, 1000, 950, 1000, 1100, 1200, 1150, 1000, 1100, 1200, 1300],
    [1200, 1300, 1250, 1400, 1500, 1600, 1650, 1700, 1600, 1550, 1500, 1400],
    [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450],
])

annual_production_per_factory = np.sum(data, axis=1)

total_production = np.sum(data)

most_productive_factory_index = np.argmax(annual_production_per_factory)
most_productive_factory = most_productive_factory_index + 1

print(f"Общее количество произведенных грузовиков за год: {total_production}")
for i, production in enumerate(annual_production_per_factory, 1):
    print(f"Завод {i} - {production} грузовиков")
print(f"Завод {most_productive_factory} был самым продуктивным")
