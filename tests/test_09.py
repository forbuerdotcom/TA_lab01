import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
shop_mod = importlib.import_module('09_shopping')

def test_all_products_present():
    assert set(shop_mod.sweets.keys()) == {'печенье', 'конфеты', 'карамель', 'пирожное'}


def test_two_shops_per_product():
    for product, offers in shop_mod.sweets.items():
        assert len(offers) == 2, f"{product}: должно быть 2 магазина"


def test_pechenye_cheapest():
    # пятерочка 9.99 < ашан 10.99 < магнит 11.99
    assert shop_mod.sweets['печенье'] == [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ]


def test_konfety_cheapest():
    # магнит 30.99 < пятерочка 32.99 < ашан 34.99
    assert shop_mod.sweets['конфеты'] == [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ]


def test_karamel_cheapest():
    # магнит 41.99 < ашан 45.99 < пятерочка 46.99
    assert shop_mod.sweets['карамель'] == [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ]


def test_pirozhnoe_cheapest():
    # пятерочка 59.99 < магнит 62.99 < ашан 67.99
    assert shop_mod.sweets['пирожное'] == [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]

def test_offers_sorted_ascending():
    for product, offers in shop_mod.sweets.items():
        prices = [o['price'] for o in offers]
        assert prices == sorted(prices), f"{product}: не отсортировано"

def test_main_prints_sweets(capsys):
    shop_mod.main()
    out = capsys.readouterr().out
    for product in ['печенье', 'конфеты', 'карамель', 'пирожное']:
        assert product in out


if __name__ == "__main__":
    pytest.main([__file__])