#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'
# в формате "Три песни звучат ХХХ минут"
def sum_songs_list(songs, names):
    #Сумма длительностей песен с указанными именами из списка [[name, duration], ...].
    total = 0 #счетчик
    for song_name, duration in songs:
        if song_name in names:
            total += duration
    return round(total, 3)


# Распечатайте общее время звучания трех других песен:
# 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
# в формате "А другие три песни звучат ХХХ минут"
def sum_songs_dict(songs, names):
    #Сумма длительностей песен с указанными именами из словаря {name: duration}.
    total = 0
    for name in names:
        total += songs[name]
    return round(total, 3)


def main():
    three = ['Halo', 'Enjoy the Silence', 'Clean']
    total = sum_songs_list(violator_songs_list, three)
    print(f"Три песни звучат {total} минут")

    three_other = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    total2 = sum_songs_dict(violator_songs_dict, three_other)
    print(f"А другие три песни звучат {total2} минут")


if __name__ == '__main__':
    main()