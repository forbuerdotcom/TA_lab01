#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


# Создайте множество цветов, произрастающих в саду и на лугу
def garden_set():
    return set(garden)


def meadow_set():
    return set(meadow)


# Выведите на консоль все виды цветов
def all_flowers():
    return garden_set() | meadow_set() #ИЛИ (+)


# Выведите на консоль те, которые растут и там и там
def common_flowers():
    return garden_set() & meadow_set() # И (*)


# Выведите на консоль те, которые растут в саду, но не растут на лугу
def only_in_garden():
    return garden_set() - meadow_set() #НЕ (-)


# Выведите на консоль те, которые растут на лугу, но не растут в саду
def only_in_meadow():
    return meadow_set() - garden_set() # НЕ (-)


def main():
    print(all_flowers())
    print(common_flowers())
    print(only_in_garden())
    print(only_in_meadow())


if __name__ == '__main__':
    main()