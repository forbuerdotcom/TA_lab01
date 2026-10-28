import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
goods_mod = importlib.import_module('10_store')

def test_calc_single_batch():
    # Лампа: 1 партия 27 * 42
    batches = [{'quantity': 27, 'price': 42}]
    assert goods_mod.calc_product(batches) == (27, 1134)


def test_calc_two_batches():
    # Стол: 22*510 + 32*520 = 11220 + 16640 = 27860, кол-во 54
    batches = [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ]
    assert goods_mod.calc_product(batches) == (54, 27860)


def test_calc_empty_batches():
    assert goods_mod.calc_product([]) == (0, 0)

def test_calc_all_lampa():
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    assert result['Лампа'] == (27, 1134)


def test_calc_all_stol():
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    assert result['Стол'] == (54, 27860)


def test_calc_all_divan():
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    # 2*1200 + 1*1150 = 3550, кол-во 3
    assert result['Диван'] == (3, 3550)


def test_calc_all_stul():
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    # 50*100 + 12*95 + 43*97 = 5000 + 1140 + 4171 = 10311, кол-во 105
    assert result['Стул'] == (105, 10311)

def test_calc_all_has_all_goods():
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    assert set(result.keys()) == set(goods_mod.goods.keys())


def test_calc_all_positive():
    # у каждого товара есть и количество, и стоимость
    result = goods_mod.calc_all(goods_mod.goods, goods_mod.store)
    for name, (qty, cost) in result.items():
        assert qty > 0, f"{name}: кол-во должно быть > 0"
        assert cost > 0, f"{name}: стоимость должна быть > 0"

def test_format_line_exact():
    assert goods_mod.format_line('Лампа', 27, 1134) == 'Лампа - 27 шт, стоимость 1134 руб'


def test_format_line_other_values():
    assert goods_mod.format_line('Стол', 54, 27860) == 'Стол - 54 шт, стоимость 27860 руб'

def test_main_prints_all_products(capsys):
    goods_mod.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert len(out) == 4
    assert 'Лампа' in out[0]
    assert 'Стол' in out[1]
    assert 'Диван' in out[2]
    assert 'Стул' in out[3]


def test_main_prints_exact_lines(capsys):
    goods_mod.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert out[0] == 'Лампа - 27 шт, стоимость 1134 руб'
    assert out[1] == 'Стол - 54 шт, стоимость 27860 руб'
    assert out[2] == 'Диван - 3 шт, стоимость 3550 руб'
    assert out[3] == 'Стул - 105 шт, стоимость 10311 руб'


if __name__ == "__main__":
    pytest.main([__file__])