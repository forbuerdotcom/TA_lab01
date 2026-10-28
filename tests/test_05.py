import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
zoo_mod = importlib.import_module('05_zoo')

def test_add_bear_puts_bear_after_lion():
    z = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo_mod.add_bear(z)
    assert z == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']


def test_add_birds_appends_in_order():
    z = ['lion', 'kangaroo']
    zoo_mod.add_birds(z, ['rooster', 'ostrich', 'lark'])
    assert z == ['lion', 'kangaroo', 'rooster', 'ostrich', 'lark']


def test_remove_elephant():
    z = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']
    zoo_mod.remove_elephant(z)
    assert 'elephant' not in z


def test_cell_number_is_one_indexed():
    z = ['lion', 'bear', 'kangaroo']
    # lion на индексе 0 → клетка 1
    assert zoo_mod.cell_number(z, 'lion') == 1
    # kangaroo на индексе 2 → клетка 3
    assert zoo_mod.cell_number(z, 'kangaroo') == 3

def test_build_final_zoo():
    assert zoo_mod.build_final_zoo() == [
        'lion', 'bear', 'kangaroo', 'monkey',
        'rooster', 'ostrich', 'lark',
    ]


def test_build_final_zoo_no_elephant():
    assert 'elephant' not in zoo_mod.build_final_zoo()


def test_build_final_zoo_has_all_animals():
    z = zoo_mod.build_final_zoo()
    for animal in ['lion', 'bear', 'kangaroo', 'monkey',
                   'rooster', 'ostrich', 'lark']:
        assert animal in z


def test_build_final_zoo_is_fresh_each_call():
    # важно: повторный вызов не должен возвращать «накопленный» список
    a = zoo_mod.build_final_zoo()
    b = zoo_mod.build_final_zoo()
    assert a == b
    assert len(a) == 7

def test_main_prints_lion_and_lark(capsys):
    zoo_mod.main()
    out = capsys.readouterr().out
    assert 'Лев -  1' in out
    assert 'жаворонок - 7' in out


def test_main_prints_three_lists(capsys):
    zoo_mod.main()
    out = capsys.readouterr().out.strip().splitlines()
    # первые три строки — это три списка
    assert out[0].startswith('[') and 'bear' in out[0]
    assert out[1].startswith('[') and 'lark' in out[1]
    assert out[2].startswith('[') and 'elephant' not in out[2]


if __name__ == "__main__":
    pytest.main([__file__])