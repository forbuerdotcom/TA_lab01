import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
garden_mod = importlib.import_module('08_garden')

def test_garden_set_unique():
    g = garden_mod.garden_set()
    assert isinstance(g, set)
    assert len(g) == 5   # ромашка (2x), роза (2x), одуванчик, гладиолус, подсолнух


def test_meadow_set_unique():
    m = garden_mod.meadow_set()
    assert isinstance(m, set)
    assert len(m) == 4   # клевер (2x), одуванчик (2x), ромашка (2x), мак

def test_all_flowers():
    assert garden_mod.all_flowers() == {
        'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух',
        'клевер', 'мак',
    }


def test_common_flowers():
    assert garden_mod.common_flowers() == {'ромашка', 'одуванчик'}


def test_only_in_garden():
    assert garden_mod.only_in_garden() == {'роза', 'гладиолус', 'подсолнух'}


def test_only_in_meadow():
    assert garden_mod.only_in_meadow() == {'клевер', 'мак'}

def test_all_is_union_of_parts():
    assert len(garden_mod.all_flowers()) == (
        len(garden_mod.only_in_garden())
        + len(garden_mod.only_in_meadow())
        + len(garden_mod.common_flowers())
    )


def test_disjoint_parts():
    # «только в саду», «только на лугу», «и там и там» — попарно не пересекаются
    a = garden_mod.only_in_garden()
    b = garden_mod.only_in_meadow()
    c = garden_mod.common_flowers()
    assert a & b == set()
    assert a & c == set()
    assert b & c == set()


def test_originals_not_mutated():
    assert len(garden_mod.garden) == 7
    assert len(garden_mod.meadow) == 7

def test_main_prints_all_four(capsys):
    garden_mod.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert len(out) == 4
    assert 'гладиолус' in out[0] and 'клевер' in out[0]   # все
    assert 'ромашка' in out[1] and 'одуванчик' in out[1]  # общие
    assert 'роза' in out[2]                               # только сад
    assert 'мак' in out[3]                                # только луг


if __name__ == "__main__":
    pytest.main([__file__])