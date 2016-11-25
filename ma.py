from time import time

from alg.ff import func


def main():
    func()


if __name__ == "__main__":
    t1 = time()
    main()
    t2 = time()
    print('\n' * 10)
    print('Time execution - %s' % (t2 - t1))
