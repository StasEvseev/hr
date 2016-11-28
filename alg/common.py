from alg import _input, data_from_input


class wrap:
    def __init__(self, catalog, test):
        self.catalog = catalog
        self.test = test

    def __call__(self, func):

        def wr():
            _orig_input = func.__globals__['__builtins__']['input']
            _orig_print = func.__globals__['__builtins__']['print']

            _exp = []

            def _print(string):
                _exp.append(string)
                _orig_print(string)

            func.__globals__['__builtins__']['input'] = _input('alg/data/%s/%s.txt' % (self.catalog, self.test))
            func.__globals__['__builtins__']['print'] = _print

            expected_result = [int(x) for x in
                               data_from_input('alg/data/%s/expected/%s.txt' % (self.catalog, self.test)).split('\n')]

            func()

            func.__globals__['__builtins__']['input'] = _orig_input
            func.__globals__['__builtins__']['print'] = _orig_print

            if _exp == expected_result:
                print('Ok')
            else:
                print('False')

        return wr


def func_testcases(func, input, print):
    test = func.__test__
    catalog = func.__catalog__
    _orig_print = print
    _orig_input = input

    _exp = []

    def _print(string):
        _exp.append(string)
        _orig_print(string)

    input = _input('alg/data/%s/%s.txt' % (catalog, test))
    print = _print

    expected_result = [int(x) for x in data_from_input('alg/data/%s/expected/%s.txt' % (catalog, test)).split('\n')]

    func()

    print = _orig_print
    input = _orig_input

    if _exp == expected_result:
        print('Ok')
    else:
        print('False')
