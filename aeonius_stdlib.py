def plus(a):
    return lambda x: a + x


def minus(a):
    return lambda x: a - x


def times(a):
    return lambda x: a * x


def div(a):
    return lambda x: a / x


def mod(a):
    return lambda x: a % x


def power(a):
    return lambda x: a ** x


def lt(a):
    return lambda x: a < x


def lteq(a):
    return lambda x: a <= x


def eqeq(a):
    return lambda x: a == x


def ltgt(a):
    return lambda x: a != x


def gteq(a):
    return lambda x: a >= x


def gt(a):
    return lambda x: a > x


def ndnd(a):
    return lambda x: a and x


def ouou(a):
    return lambda x: a or x


def xor(a):
    return lambda x: a ^ x


def negate(a):
    return not a


def index(a):
    return lambda x: a[x]


def dot(a):
    return lambda x: lambda y: a(x(y))


def ae_map(a):
    return lambda x: list(map(a, x))


def ae_filter(a):
    return lambda x: list(filter(a, x))


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
    return lambda x: lambda y: a(y)(x)


def gtlt(a):
    return lambda b: lambda x: (a(x[0]), b(x[1]))


def maximum(a):
    return max(a)


def minimum(a):
    return min(a)


def uncurry(a):
    return lambda x: a(x[0])(x[1])


def is_number(a):
    return ord(a) >= ord('0') and ord(a) <= ord('9')


def get(a):
    return lambda x: a[x]


def ascii(a):
    return ord(a)


def dup(a):
    return (a, a)


def abs(a):
    return -a if a < 0 else a


def length(a):
    return len(a)
