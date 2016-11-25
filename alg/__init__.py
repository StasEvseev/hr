
def data_from_input(path):
    return open(path, 'r').read()


def _input(path):
    data = data_from_input(path).split('\n')
    it = iter(data)

    def f():
        n = next(it)
        return n
    return f
