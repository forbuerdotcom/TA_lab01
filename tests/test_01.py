"""Тесты задания 01: площадь круга и попадание точки внутрь."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib

import pytest

circle = importlib.import_module('01_circle')


# ---------------------------------------------------------------------------
# 1. Конкретные значения: формула площади и попадания считаются правильно
# ---------------------------------------------------------------------------
def test_circle_area_value():
    # pi * r^2 = 3.1415926 * 1764 = 5541.7693...
    assert circle.circle_area(42) == pytest.approx(5541.7693)


def test_point_inside_value():
    # (23, 34): sqrt(23^2 + 34^2) = sqrt1685 ~~ 41.05 < 42
    assert circle.is_inside((23, 34), 42) is True


def test_point_outside_value():
    # (30, 30): sqrt(900 + 900) ~~ 42.43 > 42
    assert circle.is_inside((30, 30), 42) is False



def test_area_grows_quadratically():
    # S(2r) = 4 * S(r)
    assert circle.circle_area(20) == pytest.approx(4 * circle.circle_area(10))


def test_area_zero_radius():
    assert circle.circle_area(0) == 0


def test_origin_is_always_inside():
    assert circle.is_inside((0, 0), 42) is True


def test_boundary_is_not_inside():
    # Ровно на границе (расстояние == radius) — не внутри (строгое <)
    assert circle.is_inside((42, 0), 42) is False
    assert circle.is_inside((0, -42), 42) is False


def test_symmetry_of_quadrants():
    # Точка попадает/не попадает независимо от знака координат
    for x, y in [(10, 10), (-10, 10), (10, -10), (-10, -10)]:
        assert circle.is_inside((x, y), 42) is True
    for x, y in [(40, 40), (-40, 40), (40, -40), (-40, -40)]:
        assert circle.is_inside((x, y), 42) is False



def test_main_prints_expected_lines(capsys):
    circle.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert out[0] == '5541.7693'
    assert out[1] == 'True'
    assert out[2] == 'False'


if __name__ == "__main__":
    pytest.main([__file__])