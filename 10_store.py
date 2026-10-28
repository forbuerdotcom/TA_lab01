#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Пример:
#   Лампа - 27 шт, стоимость 1134 руб


def calc_product(batches):
    total_quantity = 0
    total_cost = 0

    for batch in batches:
        total_quantity += batch['quantity']
        total_cost += batch['quantity'] * batch['price']

    return total_quantity, total_cost


def calc_all(goods, store):
    result = {}
    for name, code in goods.items():
        result[name] = calc_product(store[code])
    return result


def format_line(name, quantity, cost):
    return f"{name} - {quantity} шт, стоимость {cost} руб"


def main():
    for name, code in goods.items():
        total_quantity, total_cost = calc_product(store[code])
        print(format_line(name, total_quantity, total_cost))


if __name__ == '__main__':
    main()