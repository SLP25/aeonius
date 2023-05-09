def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def times(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def power(a, b):
    return a ** b


def lt(a, b):
    return a < b


def lteq(a, b):
    return a <= b


def eqeq(a, b):
    return a == b


def ltgt(a, b):
    return a != b


def gteq(a, b):
    return a >= b


def gt(a, b):
    return a > b


def ndnd(a, b):
    return a and b


def ouou(a, b):
    return a or b


def xor(a, b):
    return a ^ b


def negate(a):
    return not a


def index(a, i):
    return a[i]


def dot(a, b):
    return lambda x: a(b(x))


def ae_map(a):
    return lambda x: map(a, x)


def ae_filter(a):
    return lambda x: filter(a, x)


def id(a):
    return a


def fst(a):
    return a[0]


def snd(a):
    return a[1]


def head(a):
    return a[0]


def tail(a):
    return a[1:]


def flip(a):
    return lambda x, y: a(y)(x)


def is_number(a):
    return ord(a) >= ord('0') and ord(a) <= ord('9')


def ascii(a):
    return ord(a)


def dup(a):
    return (a, a)


def gtlt(a, b):
    return lambda x: (a(x[0]), b(x[1]))


def abs(a):
    return -a if a < 0 else a


def length(a):
    return len(a)
