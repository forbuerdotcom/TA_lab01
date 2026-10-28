"""Тесты задания 03: фильмы через срезы строки."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib
import inspect

import pytest

movies = importlib.import_module('03_favorite_movies')


def test_first_movie():
    assert movies.first_movie() == 'Терминатор'


def test_last_movie():
    assert movies.last_movie() == 'Назад в будущее'


def test_second_movie():
    assert movies.second_movie() == 'Пятый элемент'


def test_second_from_end():
    assert movies.second_from_end() == 'Чужие'


def test_no_commas():
    for fn in (movies.first_movie, movies.last_movie,
               movies.second_movie, movies.second_from_end):
        assert ',' not in fn()


def test_no_leading_or_trailing_spaces():
    for fn in (movies.first_movie, movies.last_movie,
               movies.second_movie, movies.second_from_end):
        result = fn()
        assert result == result.strip(), f"{fn.__name__}: лишние пробелы по краям"


def test_uses_only_slicing():
    """В исходниках функций не должно быть строковых методов."""
    forbidden = ['.split(', '.find(', '.index(', '.partition(', '.rpartition(',
                 '.rsplit(', 're.', '.strip(']
    for fn in (movies.first_movie, movies.last_movie,
               movies.second_movie, movies.second_from_end):
        source = inspect.getsource(fn)
        # берём только строку после return — там должно быть чистое срезание
        expr = source.split('return', 1)[1]
        for bad in forbidden:
            assert bad not in expr, f"{fn.__name__} использует {bad} — нельзя"


def test_main_prints_in_order(capsys):
    movies.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert out == ['Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие']


if __name__ == "__main__":
    pytest.main([__file__])