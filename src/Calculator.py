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


def parenthesis(src):
    if '(' in src:
        start = src.index('(')
        val = parenthesis(src[start + 1:])
        return parenthesis(src[0:start] + val)
    elif ')' in src:
        end = src.index(')')
        val = str(plus(src[0:end]))
        return val + src[end + 1:]
    else:
        return src

def calculate(src):
    parened = parenthesis(src)
    val = plus(parened)
    return val


if __name__ == '__main__':
    tests = [
        ('1 + 2 + 3', 6),
        ('1 * 2 + 3 * 2 * 2', 14),
        ('2*3*4', 24),
        ('23-(333 - 330)', 20),
        ('23-((300 + 30+3) - 330)', 20),
        ('(20+3)-((300 + 30+3) - (300+30))', 20),
        ('1-2*3', -5),
        ('1-2-3', -4),
        ('6 / 2 - 3', 0),
        ('\t5.3 ', 5.3),
    ]


    def assert_(src, expected):
        val = calculate(src)
        if val == expected:
            print(f'성공: {src} => {expected}')
        else:
            print(f'실패: {src} => {val} != {expected}')


    for src, expected in tests:
        try:
            assert_(src, expected)
        except Exception as e:
            print(e)
