#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'печенье': [
#         {'shop': 'пятерочка', 'price': 9.99},
#         {'shop': 'ашан', 'price': 10.99},
#     ],
#     ...
# }
# Указать надо только по 2 магазина с минимальными ценами


def collect_all_offers(shops):
    #Собирает все предложения по каждому товару:
    #{название товара: [{'shop': ..., 'price': ...}, ...]}
    #
    offers = {}
    for shop_name, products in shops.items():
        for product in products:
            name = product['name']
            if name not in offers:
                offers[name] = []
            offers[name].append({'shop': shop_name, 'price': product['price']})
    return offers


def pick_cheapest_two(offers):
    #Из каждого списка оставляет 2 магазина с минимальной ценой.
    result = {}
    for name, items in offers.items():
        items.sort(key=lambda item: item['price'])
        result[name] = items[:2]
    return result


sweets = pick_cheapest_two(collect_all_offers(shops))


def main():
    print(sweets)


if __name__ == '__main__':
    main()