def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def times(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def power(a,b):
    return a ** b

def lt(a,b):
    return a < b

def lteq(a,b):
    return a <= b

def eqeq(a,b):
    return a == b

def gteq(a,b):
    return a >= b

def gt(a,b):
    return a > b

def ndnd(a,b):
    return a and b

def ouou(a,b):
    return a or b

def xor(a,b):
    return a ^ b

def negate(a):
    return not a

def index(a, i):
    return a[i]

def dot(a,b):
    return lambda x: a(b(x))

def mp(a):
    return lambda x: map(a, x)

def fltr(a):
    return lambda x: filter(a, x)