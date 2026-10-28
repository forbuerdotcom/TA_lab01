import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
songs_mod = importlib.import_module('06_songs_list')

def test_list_sum_three_songs():
    # Halo 4.9 + Enjoy the Silence 4.20 + Clean 5.83 = 14.93
    names = ['Halo', 'Enjoy the Silence', 'Clean']
    assert songs_mod.sum_songs_list(songs_mod.violator_songs_list, names) == pytest.approx(14.93)


def test_list_sum_does_not_include_other_songs():
    # Если бы функция суммировала ВСЁ — результат был бы другим
    names = ['Halo', 'Enjoy the Silence', 'Clean']
    result = songs_mod.sum_songs_list(songs_mod.violator_songs_list, names)
    # сумма всех песен ~ 39.9 — если тест упал, значит баг «суммирует всё» вернулся
    assert result < 20
    assert result > 10


def test_list_sum_empty_names():
    assert songs_mod.sum_songs_list(songs_mod.violator_songs_list, []) == 0


def test_list_sum_single_song():
    assert songs_mod.sum_songs_list(
        songs_mod.violator_songs_list, ['Halo']
    ) == pytest.approx(4.9)


def test_list_sum_unknown_name_ignored():
    # если имени нет в списке — просто не добавляется
    assert songs_mod.sum_songs_list(
        songs_mod.violator_songs_list, ['Не существует']
    ) == 0

def test_dict_sum_three_songs():
    # Sweetest Perfection 4.43 + Policy of Truth 4.88 + Blue Dress 4.18 = 13.49
    names = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    assert songs_mod.sum_songs_dict(songs_mod.violator_songs_dict, names) == pytest.approx(13.49)


def test_dict_sum_empty_names():
    assert songs_mod.sum_songs_dict(songs_mod.violator_songs_dict, []) == 0


def test_dict_sum_single_song():
    assert songs_mod.sum_songs_dict(
        songs_mod.violator_songs_dict, ['Halo']
    ) == pytest.approx(4.30)


def test_dict_sum_raises_on_unknown():
    with pytest.raises(KeyError):
        songs_mod.sum_songs_dict(songs_mod.violator_songs_dict, ['Не существует'])

def test_main_prints_list_total(capsys):
    songs_mod.main()
    out = capsys.readouterr().out
    assert "Три песни звучат 14.93 минут" in out


def test_main_prints_dict_total(capsys):
    songs_mod.main()
    out = capsys.readouterr().out
    assert "А другие три песни звучат 13.49 минут" in out


if __name__ == "__main__":
    pytest.main([__file__])