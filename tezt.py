import statistics
"""
ДАНО:
Датасет с фамилиями и показателями.
Список футболистов.
"""

dataset = {'admin$': 2, 'Borat': 23, 'daemon_': 6, 'Kovalev': 16, 'Anderson': 21, 'Corvin': 3, 'aBrams': 14, '13': 20,
           'Gerhaгd': 19, 'Zidane': 12, 'Messi': 10, 'Rupert': 10}

footballers = ['Messi', 'Zidane']

"""
ЗАДАЧА:
ШАГ 1
Очистить датасет по совокупности условий:
1) Нам нужны только люди (фамилия состоит из букв)
2) Нам не нужны футболисты
3) Показатель может быть только чётным, остальное – искажения. Искажения исправить: привести к ближайшему меньшему чётному.
Вернуть очищенный словарь в переменной cleared_dataset.
ШАГ 2
Теперь небольшая аналитика на очищенном словаре. 
Надо вернуть список фамилий тех, у кого значение показателя выше медианного, в порядке убывания показателя.
Список поместить в переменной result.
"""
cleared_dataset = dict()
for key,value in dataset.items():
    if key.isalpha() and key not in footballers:
        if value % 2 == 0:
            cleared_dataset[key] = value
        else:
            cleared_dataset[key] = value-1
med = statistics.median(cleared_dataset.values())
final_list = []
cleared_dataset = dict(sorted(cleared_dataset .items(), key=lambda item: item[1], reverse=True))
for key, value in cleared_dataset.items():
    if value > med:
        final_list.append(key)
print(final_list)







