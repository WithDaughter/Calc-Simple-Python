from functools import reduce


def multiply(src):
    if '*' in src:
        tokens = src.split('*')
        arr = map(lambda t: int(t), tokens)
        return reduce(lambda acc, cur: acc * cur, arr, 1)
    else:
        return int(src)


def plus(src):
    tokens = src.split('+')
    arr = map(lambda t: multiply(t), tokens)
    return reduce(lambda acc, cur: acc + cur, arr, 0)


def calculate(src):
    val = plus(src)
    return val

if __name__ == '__main__':
    tests = [
        ('1+2+3', 6),
        ('1*2+3*2*2', 14),
        ('2*3*4', 24),
    ]

    def assert_(src, expected):
        val = calculate(src)
        if val == expected:
            return
        else:
            print(f'실패: {src} => {val} != {expected}')


    for src, expected in tests:
        assert_(src, expected)
