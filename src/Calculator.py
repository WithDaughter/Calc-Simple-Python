from functools import reduce


def plus(src):
    tokens = src.split('+')
    arr = map(lambda t: int(t), tokens)
    return reduce(lambda acc, cur: acc + cur, arr, 0)


def calculate(src):
    val = plus(src)
    return val

if __name__ == '__main__':
    src = '1+2+3'
    val = calculate(src)
    print(val)
