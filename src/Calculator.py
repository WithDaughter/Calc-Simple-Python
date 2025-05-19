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
    src = '1*2+3*2*2'
    val = calculate(src)
    print(val)
