def fact(number: int):
    if number < 0:
        return None

    if number == 0:
        return 1

    else:
        return number * fact(number - 1)


def is_prime(number: int):
    from math import ceil

    number = abs(number)

    if number == 0 or number == 1:
        return False

    elif number == 2:
        return True

    end = ceil(number ** 0.5) + 1

    for i in range(2, end):
        if number % i == 0:
            return False

    return True
