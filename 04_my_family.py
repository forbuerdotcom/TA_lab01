#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["мать", "отец", "брат"]

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ["мать", 165],
    ["отец", 168],
    ["брат", 169]
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
def get_height(family_height, name):
    """Возвращает рост члена семьи по имени."""
    for member_name, height in family_height:
        if member_name == name:
            return height
    raise ValueError(f"{name} не найден в списке")


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
def total_height(family_height):
    """Сумма ростов всех членов семьи."""
    summ = 0
    for name in range(len(family_height)):
        summ += family_height[name][1]
    return summ


def main():
    print("Рост отца - {} см".format(get_height(my_family_height, "отец")))
    print(total_height(my_family_height))


if __name__ == '__main__':
    main()