from bisect import bisect_left

from . import _input, data_from_input


def contains(l, elem):
    index = bisect_left(l, elem)
    if index < len(l):
        return l[index] == elem
    return False


def closest_value_index(array, value):
    positive = value > 0
    p = bisect_left(array, value)

    if p == 0:
        return array[0], p

    if p == len(array):
        return array[-1], p

    before = array[p - 1]
    after = array[p]

    if after - value == value - before:
        if after - value < 0:
            pass
        else:
            pass
        pass
    elif after - value < value - before:
        return after, p
    else:
        return before, p - 1
    # else:
    #     if after - value > value - before:
    #         return after, p
    #     else:
    #         return before, p - 1


def func_testcases():
    test = 'Test1'
    global print
    global input

    _exp = []
    _orig_print = print
    _orig_input = input

    def _print(string):
        _exp.append(string)
        _orig_print(string)

    input = _input('alg/data/Absolute_Element_Sums/%s.txt' % test)
    print = _print

    expected_result = [int(x) for x in data_from_input('alg/data/Absolute_Element_Sums/expected/%s.txt' % test).split('\n')]

    func()

    print = _orig_print
    input = _orig_input

    if _exp == expected_result:
        print('Ok')
    else:
        print('False')

    #assert _exp == expected_result, 'You input - %s, expected - %s' % (_exp, expected_result)


def func():
    n = int(input().strip())
    array = [int(x) for x in input().strip().split()]

    n_q = int(input().strip())
    qs = [int(x) for x in input().strip().split()]
    variant3(n, array, qs)


def variant2(n, array, qs):
    sorted_array = sorted(array)
    len_ = len(sorted_array)

    Q = 0

    for num_, q in enumerate(qs):
        sum_p = 0
        sum_n = 0
        Q += q
        for num, s in enumerate(sorted_array):
            if s + Q > 0:
                sum_p += sum(sorted_array[num:])
                sum_p += Q * (len_ - num)
                sum_p = abs(sum_p)
                break
            else:
                sum_n += abs(s + Q)

        print(sum_p + sum_n)


def variant3(n, array, qs):
    sorted_array = sorted(array)
    len_ = len(sorted_array)

    Q = 0

    for q in qs:
        Q += q

        _, index = closest_value_index(sorted_array, Q * -1)

        sum_n = sum(sorted_array[:index])
        sum_n += Q * index
        sum_n = abs(sum_n)

        sum_p = sum(sorted_array[index:])
        sum_p += Q * (len_ - index)
        sum_p = abs(sum_p)

        print(sum_p + sum_n)


def variant1(n, array, qs):
    sum_ = sum(array)

    for q in qs:
        sum_ += n * q
        print(sum_)
