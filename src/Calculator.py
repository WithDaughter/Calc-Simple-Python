from functools import reduce


def divide(src):
    if '/' in src:
        tokens = src.split('/')
        arr = list(map(int, tokens))
        token = arr[0]
        return reduce(lambda acc, cur: acc / cur, arr[1:], token)
    else:
        return float(src)


def multiply(src):
    if '*' in src:
        tokens = src.split('*')
        arr = map(divide, tokens)
        return reduce(lambda acc, cur: acc * cur, arr, 1)
    else:
        return divide(src)


def minus(src):
    if '-' in src:
        tokens = src.split('-')
        arr = list(map(multiply, tokens))
        token = arr[0]
        return reduce(lambda acc, cur: acc - cur, arr[1:], token)
    else:
        return multiply(src)


def plus(src):
    if '+' in src:
        tokens = src.split('+')
        arr = map(minus, tokens)
        return reduce(lambda acc, cur: acc + cur, arr, 0)
    else:
        return minus(src)


def calculate(src):
    val = plus(src)
    return val


if __name__ == '__main__':
    tests = [
        ('1 + 2 + 3', 6),
        ('1 * 2 + 3 * 2 * 2', 14),
        ('2*3*4', 24),
        ('1-2*3', -5),
        ('1-2-3', -4),
        ('6 / 2 - 3', 0),
        ('\t5.3 ', 5.3),
    ]

    def assert_(src, expected):
        val = calculate(src)
        if val == expected:
            return
        else:
            print(f'실패: {src} => {val} != {expected}')


    for src, expected in tests:
        assert_(src, expected)
