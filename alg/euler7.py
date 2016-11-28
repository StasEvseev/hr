#!/bin/python3
import math
from collections import OrderedDict

from alg.common import wrap

saved_value_is_prime = dict()


def is_prime(val):
    if val in saved_value_is_prime:
        return True

    s_root = int(math.sqrt(val))
    for i in range(2, s_root + 1):
        if val % i == 0:
            return False
    saved_value_is_prime[val] = True
    return True


def generator():
    number = 0
    for i in range(2, 9999999):
        if is_prime(i):
            number += 1
            yield number, i


result = dict()


def get_prime_by_number(number):
    value = result.get(number)

    if value:
        return value

    for num, value in generator():
        result[num] = value
        if num == number:
            return value


@wrap(catalog='10001st prime', test='Test2')
def func():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())

        value = get_prime_by_number(n)

        print(value)
