import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest

family = importlib.import_module('04_my_family')

def test_father_height():
    assert family.get_height(family.my_family_height, "отец") == 168


def test_mother_height():
    assert family.get_height(family.my_family_height, "мать") == 165


def test_brother_height():
    assert family.get_height(family.my_family_height, "брат") == 169


def test_total_height():
    # 165 + 168 + 169 = 502
    assert family.total_height(family.my_family_height) == 502

def test_get_height_on_other_family():
    other = [["дед", 180], ["баба", 160]]
    assert family.get_height(other, "дед") == 180
    assert family.get_height(other, "баба") == 160


def test_total_height_on_other_family():
    other = [["дед", 180], ["баба", 160]]
    assert family.total_height(other) == 340


def test_total_height_empty():
    assert family.total_height([]) == 0


def test_get_height_raises_on_missing():
    with pytest.raises(ValueError):
        family.get_height(family.my_family_height, "сосед")

def test_main_prints_father_format(capsys):
    family.main()
    out = capsys.readouterr().out
    assert "Рост отца - 168 см" in out


def test_main_prints_total(capsys):
    family.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert out[-1] == "502"


if __name__ == "__main__":
    pytest.main([__file__])