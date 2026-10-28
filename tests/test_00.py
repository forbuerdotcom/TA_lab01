import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import math
import pytest
distance = importlib.import_module('00_distance')


def test_distances_between_known_cities():
    distances = distance.compute_distances(distance.sites)

    # Moscow (550, 370) + London (510, 510):  40^2 + 140^2 = 21200
    assert distances['Moscow']['London'] == pytest.approx(math.sqrt(21200))

    # Moscow (550, 370) + Paris (480, 480):   70^2 + 110^2 = 17000
    assert distances['Moscow']['Paris'] == pytest.approx(math.sqrt(17000))

    # London (510, 510) + Paris (480, 480):   30^2 + 30^2 = 1800
    assert distances['London']['Paris'] == pytest.approx(math.sqrt(1800))


def test_no_self_distances():
    # В словаре города не должно быть расстояния до самого себя
    distances = distance.compute_distances(distance.sites)
    for city in distance.sites:
        assert city not in distances[city]


def test_distances_symmetric():
    # d(A, B) == d(B, A)
    distances = distance.compute_distances(distance.sites)
    for city1 in distance.sites:
        for city2 in distance.sites:
            if city1 != city2:
                assert distances[city1][city2] == pytest.approx(
                    distances[city2][city1]
                )


def test_all_cities_present():
    # Для каждого города — все остальные, кроме него самого
    distances = distance.compute_distances(distance.sites)
    assert set(distances.keys()) == set(distance.sites.keys())
    n = len(distance.sites)
    for city in distance.sites:
        assert len(distances[city]) == n - 1


def test_main_prints_distances(capsys):
    distance.main()
    out = capsys.readouterr().out
    assert 'Moscow' in out
    assert 'London' in out
    assert 'Paris' in out


if __name__ == "__main__":
    pytest.main([__file__])