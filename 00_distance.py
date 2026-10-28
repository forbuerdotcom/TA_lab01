#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def compute_distances(sites):
    distances = {}
    # внешний цикл - распоковка. Каждая пара это (Имя: (x1, y1))
    # x1 и y1 тоже распоковываются, это кортеж из двух чисел
    # !city1 = Moskow!, !x1 = 550!, !y1 = 370!
    for city1, (x1, y1) in sites.items():
        distances[city1] = {}   #для создания словаря, в которые мы будем пихать наши расстояния
        for city2, (x2, y2) in sites.items(): #то же самое как и в первом цикле
            if city1 != city2: #растояние для одного и того же города считать бессмыссленно
                distances[city1][city2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 #полученные данные мы перемножаем и
                                                                                   # находим искомое расстояние
    return distances


def main():
    distances = compute_distances(sites)
    for city, row in distances.items(): #находим пары
        print(city, row)    #достаем из картежа имя, а потом внутренний словарь


if __name__ == '__main__':
    main()