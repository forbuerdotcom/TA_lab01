#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']


def add_bear(zoo):
    #Посадите медведя (bear) между львом и кенгуру.
    zoo.insert(1, 'bear')
    return zoo


def add_birds(zoo, birds):
    #Добавьте птиц из списка birds в последние клетки зоопарка.
    for i in range(len(birds)):
        zoo.append(birds[i])
    return zoo


def remove_elephant(zoo):
    #Уберите слона (elephant) из зоопарка.
    zoo.remove('elephant')
    return zoo


def cell_number(zoo, animal):
    #Номер клетки (1-индексированный, первая клетка - номер 1).
    return zoo.index(animal) + 1


def build_final_zoo():
    #Полный зоопарк после всех операций (для тестов).
    z = ['lion', 'kangaroo', 'elephant', 'monkey']
    add_bear(z)
    add_birds(z, birds)
    remove_elephant(z)
    return z


def main():
    z = ['lion', 'kangaroo', 'elephant', 'monkey']

    add_bear(z)
    print(z)

    add_birds(z, birds)
    print(z)

    remove_elephant(z)
    print(z)

    print("Лев - ", cell_number(z, 'lion'))
    print("жаворонок -", cell_number(z, 'lark'))


if __name__ == '__main__':
    main()