#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib

MODULES = [
    '00_distance',
    '01_circle',
    '02_operations',
    '03_favorite_movies',
    '04_my_family',
    '05_zoo',
    '06_songs_list',
    '07_secret',
    '08_garden',
    '09_shopping',
    '10_store',
]

while True:
    print()
    for i, name in enumerate(MODULES, 1):
        print(f'{i}. {name}')
    print('0. Выход')

    choice = int(input('\nНомер задания: '))

    if choice == 0:
        break

    module = importlib.import_module(MODULES[choice - 1])
    print()
    module.main()
    input('\nEnter — обратно в меню...')