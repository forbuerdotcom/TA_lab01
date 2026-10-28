import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
import pytest
secret = importlib.import_module('07_secret')
def test_first_word():
    assert secret.decode_word(0) == 'в'


def test_second_word():
    assert secret.decode_word(1) == 'бане'


def test_third_word():
    assert secret.decode_word(2) == 'веник'


def test_fourth_word():
    assert secret.decode_word(3) == 'дороже'


def test_fifth_word():
    assert secret.decode_word(4) == 'денег'


def test_full_phrase():
    assert secret.decode_message() == 'в бане веник дороже денег'


def test_words_count():
    assert len(secret.decode_message().split()) == 5


def test_only_cyrillic_and_spaces():
    phrase = secret.decode_message()
    for ch in phrase:
        assert ch.isalpha() or ch == ' ', f"лишний символ: {ch!r}"


def test_no_digits_in_result():

    phrase = secret.decode_message()
    assert not any(c.isdigit() for c in phrase)


def test_decode_word_raises_on_bad_index():
    with pytest.raises(IndexError):
        secret.decode_word(99)

def test_main_prints_phrase(capsys):
    secret.main()
    out = capsys.readouterr().out.strip()
    assert out == 'в бане веник дороже денег'


if __name__ == "__main__":
    pytest.main([__file__])