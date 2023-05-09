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

def elem(var_28):
    
    match var_28:
        case var_1:
            def return_elem(var_29):    
                match var_29:
                    case []:
                        
                        return_return_elem = False
                        return return_return_elem
                    case [var_10,*var_11]:
                        
                        if eqeq(var_10, var_1):
                             
                            return_return_elem = True
                            return return_return_elem
                        if True:
                             
                            return_return_elem = ((elem (var_1)) (var_11))
                            return return_return_elem
                return return_return_elem
    return return_elem

def replicate(var_20):
    
    match var_20:
        case 0:
            def return_replicate(var_21):    
                match var_21:
                    case _:
                        
                        return_return_replicate = []
                        return return_return_replicate
                return return_return_replicate
        case _:
            def return_replicate(var_22):    
                match var_22:
                    case _:
                        
                        return_return_replicate = plus([var_22], (((replicate ((minus(var_20, 1)))) (var_22))))
                        return return_return_replicate
                return return_return_replicate
    return return_replicate

def caminho(var_98):
    
    match var_98:
        case (var_99,var_100):
            def return_caminho(var_101):    
                match var_101:
                    case (var_102,var_103):
                        
                        if lteq(ndnd(lteq(var_99, var_102), var_100), var_103):
                             
                            return_return_caminho = plus((((replicate ((minus(var_102, var_99)))) ('Este'))), (((replicate ((minus(var_103, var_100)))) ('Norte'))))
                            return return_return_caminho
                        if gt(ndnd(lteq(var_99, var_102), var_100), var_103):
                             
                            return_return_caminho = plus((((replicate ((minus(var_102, var_99)))) ('Este'))), (((replicate ((minus(var_100, var_103)))) ('Sul'))))
                            return return_return_caminho
                        if lteq(ndnd(gt(var_99, var_102), var_100), var_103):
                             
                            return_return_caminho = plus((((replicate ((minus(var_99, var_102)))) ('Oeste'))), (((replicate ((minus(var_103, var_100)))) ('Norte'))))
                            return return_return_caminho
                        if gt(ndnd(gt(var_99, var_102), var_100), var_103):
                             
                            return_return_caminho = plus((((replicate ((minus(var_99, var_102)))) ('Oeste'))), (((replicate ((minus(var_100, var_103)))) ('Sul'))))
                            return return_return_caminho
                return return_return_caminho
    return return_caminho

print(elem(5)([1,2,5]))