from . import _input

input = _input('alg/data/Absolute_Element_Sums/Test5.txt')


def func():
    n = int(input().strip())
    array = [int(x) for x in input().strip().split()]

    n_q = int(input().strip())
    qs = [int(x) for x in input().strip().split()]

    for q in qs:
        array = array

        sum_ = sum(array)
        # for a in array:
        #     sum_ += a
        print(sum_)
