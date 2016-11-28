from bisect import bisect_left

from alg.common import func_testcases


def closest_value_index(array, value):
    p = bisect_left(array, value)

    if p == 0:
        return array[0], p

    if p == len(array):
        return array[-1], p

    before = array[p - 1]
    after = array[p]

    if after - value == value - before:
        if after - value < 0:
            return before, p - 1
        else:
            return after, p
    else:
        return after, p


def func():

    func_testcases(func1)


def func1():
    n = int(input().strip())
    array = [int(x) for x in input().strip().split()]

    n_q = int(input().strip())
    qs = [int(x) for x in input().strip().split()]
    variant3(n, array, qs)
func1.__test__ = 'Test5'
func1.__catalog__ = 'Absolute_Element_Sums'


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

    for num, q in enumerate(qs):
        Q += q

        dif = 1

        _, index = closest_value_index(sorted_array, Q * -1 + dif)

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
