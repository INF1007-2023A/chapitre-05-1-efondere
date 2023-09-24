#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffix = 'JKLMNOPQ', 'ack'
    name_list = []
    for prefix in prefixes:
        name_list.append(prefix + suffix)

    return name_list


def prime_integer_summation() -> int:
    # somme des 100 premiers nombres premiers
    prime_numbers = []
    number = 2

    while len(prime_numbers) < 100:
        is_divisable = False
        for prime_number in prime_numbers:
            if number % prime_number == 0:
                is_divisable = True
                break

        if not is_divisable:
            prime_numbers.append(number)

        number += 1
        
    sum = 0
    for prime_number in prime_numbers:
        sum += prime_number
    return sum


def factorial(number: int) -> int:
    result = 1
    while number > 0:
        result *= number
        number -= 1

    return result


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    def is_group_acceptable(group):
        if not 4 <= len(group) <= 10:
            return False

        has_over_70 = False
        has_exactly_50 = False
        has_minor = False
        for member in group:
            if member == 25:
                return True
            if member < 18:
                has_minor = True
            if member == 50:
                has_exactly_50 = True
            if member > 70:
                has_over_70 = True

        if has_minor:
            return False

        if has_over_70 and has_exactly_50:
            return False

        return True

    return [is_group_acceptable(g) for g in groups]


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
