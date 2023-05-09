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
def enumFromTo(var_0):
    
    match var_0:
        case var_1:
            def return_enumFromTo(var_2):    
                match var_2:
                    case var_3:
                        
                        if gt(var_1, var_3):
                             
                            return_return_enumFromTo = []
                            return return_return_enumFromTo
                        if True:
                             
                            return_return_enumFromTo = plus([var_1], (((enumFromTo ((plus(var_1, 1)))) (var_3))))
                            return return_return_enumFromTo
                return return_return_enumFromTo
    return return_enumFromTo

def enumFromThenTo(var_4):
    
    match var_4:
        case var_1:
            def return_enumFromThenTo(var_5):    
                match var_5:
                    case var_3:
                        def return_return_enumFromThenTo(var_6):    
                            match var_6:
                                case var_7:
                                    
                                    if gt(var_1, var_7):
                                         
                                        return_return_return_enumFromThenTo = []
                                        return return_return_return_enumFromThenTo
                                    if True:
                                         
                                        return_return_return_enumFromThenTo = plus([var_1], ((((enumFromThenTo (var_3)) ((minus(times(2, var_3), var_1)))) (var_7))))
                                        return return_return_return_enumFromThenTo
                            return return_return_return_enumFromThenTo
                return return_return_enumFromThenTo
    return return_enumFromThenTo

def plusplus(var_8):
    
    match var_8:
        case []:
            def return_plusplus(var_9):    
                match var_9:
                    case var_1:
                        
                        return_return_plusplus = var_1
                        return return_return_plusplus
                return return_return_plusplus
        case [var_10,*var_11]:
            def return_plusplus(var_12):    
                match var_12:
                    case var_1:
                        
                        return_return_plusplus = plus([var_10], (plusplus(var_11, var_1)))
                        return return_return_plusplus
                return return_return_plusplus
    return return_plusplus
def exclexcl(var_13):
    
    match var_13:
        case [var_10,*var_11]:
            def return_exclexcl(var_14):    
                match var_14:
                    case 0:
                        
                        return_return_exclexcl = var_10
                        return return_return_exclexcl
                    case var_15:
                        
                        return_return_exclexcl = exclexcl(var_11, (minus(var_15, 1)))
                        return return_return_exclexcl
                return return_return_exclexcl
    return return_exclexcl
def reverse(var_16):
    
    match var_16:
        case []:
            
            return_reverse = []
            return return_reverse
        case [var_10,*var_11]:
            
            return_reverse = plus(((reverse (var_11))), [var_10])
            return return_reverse
    return return_reverse

def take(var_17):
    
    match var_17:
        case var_15:
            def return_take(var_18):    
                match var_18:
                    case []:
                        
                        return_return_take = []
                        return return_return_take
                    case [var_10,*var_11]:
                        
                        return_return_take = plus([var_10], ((take ((minus(var_15, 1)))) (var_11))) if gt(var_15, 0) else []
                        return return_return_take
                return return_return_take
    return return_take

def drop(var_19):
    
    match var_19:
        case var_15:
            def return_drop(var_20):    
                match var_20:
                    case []:
                        
                        return_return_drop = []
                        return return_return_drop
                    case [var_10,*var_11]:
                        
                        return_return_drop = ((drop ((minus(var_15, 1)))) (var_11)) if gt(var_15, 0) else [var_10,*var_11]
                        return return_return_drop
                return return_return_drop
    return return_drop

def zip(var_21):
    
    match var_21:
        case []:
            def return_zip(var_22):    
                match var_22:
                    case _:
                        
                        return_return_zip = []
                        return return_return_zip
                return return_return_zip
        case [var_23,*var_24]:
            def return_zip(var_25):    
                match var_25:
                    case []:
                        
                        return_return_zip = []
                        return return_return_zip
                    case [var_26,*var_27]:
                        
                        return_return_zip = plus([(var_23,var_26)], (((zip (var_24)) (var_27))))
                        return return_return_zip
                return return_return_zip
    return return_zip

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

def replicate(var_30):
    
    match var_30:
        case 0:
            def return_replicate(var_31):    
                match var_31:
                    case _:
                        
                        return_return_replicate = []
                        return return_return_replicate
                return return_return_replicate
        case var_15:
            def return_replicate(var_32):    
                match var_32:
                    case var_33:
                        
                        return_return_replicate = plus([var_33], (((replicate ((minus(var_15, 1)))) (var_33))))
                        return return_return_replicate
                return return_return_replicate
    return return_replicate

def intersperce(var_34):
    
    match var_34:
        case var_1:
            def return_intersperce(var_35):    
                match var_35:
                    case []:
                        
                        return_return_intersperce = []
                        return return_return_intersperce
                    case [var_10]:
                        
                        return_return_intersperce = [var_10]
                        return return_return_intersperce
                    case [var_10,*var_11]:
                        
                        return_return_intersperce = plus([var_10,var_1], (((intersperce (var_1)) (var_11))))
                        return return_return_intersperce
                return return_return_intersperce
    return return_intersperce

def group(var_36):
    
    match var_36:
        case []:
            
            return_group = []
            return return_group
        case [var_10]:
            
            return_group = [[var_10]]
            return return_group
        case [var_10,*var_11]:
            [[var_23,*var_24],*var_27] = (group (var_11))
            
            return_group = [[var_10,var_23,*var_24],*var_27] if eqeq(var_10, var_23) else [[var_10],[var_23,*var_24],*var_27]
            return return_group
    return return_group

def concat(var_37):
    
    match var_37:
        case []:
            
            return_concat = []
            return return_concat
        case [var_10,*var_11]:
            
            return_concat = plus(var_10, ((concat (var_11))))
            return return_concat
    return return_concat

def inits(var_38):
    
    match var_38:
        case []:
            
            return_inits = []
            return return_inits
        case [var_10,*var_11]:
            
            return_inits = plus([], (((ae_map ((lambda var_39: plus(var_10, var_3)))) (((inits (var_11)))))))
            return return_inits
    return return_inits

def tails(var_40):
    
    match var_40:
        case []:
            
            return_tails = []
            return return_tails
        case [var_10,*var_11]:
            
            return_tails = plus([[var_10,*var_11]], ((tails (var_11))))
            return return_tails
    return return_tails

def isPrefixOf(var_41):
    
    match var_41:
        case var_42:
            def return_isPrefixOf(var_43):    
                match var_43:
                    case var_44:
                        
                        return_return_isPrefixOf = ((elem (var_42)) (((inits (var_44)))))
                        return return_return_isPrefixOf
                return return_return_isPrefixOf
    return return_isPrefixOf

def isSuffixOf(var_45):
    
    match var_45:
        case var_46:
            def return_isSuffixOf(var_47):    
                match var_47:
                    case var_44:
                        
                        return_return_isSuffixOf = ((elem (var_46)) (((tails (var_44)))))
                        return return_return_isSuffixOf
                return return_return_isSuffixOf
    return return_isSuffixOf

def isSubsequenceOf(var_48):
    
    match var_48:
        case var_46:
            def return_isSubsequenceOf(var_49):    
                match var_49:
                    case var_44:
                        def return_return_isSubsequenceOf(var_50):
                            
                            match var_50:
                                case var_46:
                                    
                                    return_return_return_isSubsequenceOf = (isPrefixOf (var_46))
                                    return return_return_return_isSubsequenceOf
                            return return_return_return_isSubsequenceOf
                        
                        return_return_isSubsequenceOf = gt((length ((dot(((ae_filter (id))), (((ae_map (((return_return_isSubsequenceOf (var_46)))))) (var_44)))))), 0)
                        return return_return_isSubsequenceOf
                return return_return_isSubsequenceOf
    return return_isSubsequenceOf

def elemIndices(var_51):
    
    match var_51:
        case var_1:
            def return_elemIndices(var_52):    
                match var_52:
                    case var_44:
                        var_15 = (length (var_44))
                        
                        var_53 = ((enumFromTo (0)) ((minus(var_15, 1))))
                        
                        return_return_elemIndices = ((ae_map (snd)) ((((ae_filter ((lambda var_54: eqeq(((fst (var_3))), var_1)))) ((((zip (var_44)) (var_53))))))))
                        return return_return_elemIndices
                return return_return_elemIndices
    return return_elemIndices

var_55 = dot(((ae_map (head))), (group))

def delete(var_56):
    
    match var_56:
        case var_1:
            def return_delete(var_57):    
                match var_57:
                    case []:
                        
                        return_return_delete = []
                        return return_return_delete
                    case [var_10,*var_11]:
                        
                        return_return_delete = plus([var_10], (((delete (var_1)) (var_11)))) if ltgt(var_1, var_10) else var_11
                        return return_return_delete
                return return_return_delete
    return return_delete

def deleteAll(var_58):
    
    match var_58:
        case var_44:
            def return_deleteAll(var_59):    
                match var_59:
                    case []:
                        
                        return_return_deleteAll = var_44
                        return return_return_deleteAll
                    case [var_10,*var_11]:
                        
                        return_return_deleteAll = ((deleteAll ((((delete (var_10)) (var_44))))) (var_11))
                        return return_return_deleteAll
                return return_return_deleteAll
    return return_deleteAll

def union(var_60):
    
    match var_60:
        case var_33:
            def return_union(var_61):    
                match var_61:
                    case var_62:
                        
                        return_return_union = plus(var_33, ((ae_filter ((dot(negate, (((((flip (elem))) (var_33))) (var_62))))))))
                        return return_return_union
                return return_return_union
    return return_union

def intersect(var_63):
    
    match var_63:
        case var_33:
            def return_intersect(var_64):    
                match var_64:
                    case var_62:
                        
                        return_return_intersect = ((ae_filter (((((flip (elem))) (var_62))))) (var_33))
                        return return_return_intersect
                return return_return_intersect
    return return_intersect

def insert(var_65):
    
    match var_65:
        case var_33:
            def return_insert(var_66):    
                match var_66:
                    case []:
                        
                        return_return_insert = [var_33]
                        return return_return_insert
                    case [var_10,*var_11]:
                        
                        if gt(var_10, var_33):
                             
                            return_return_insert = [var_33,var_10,*var_11]
                            return return_return_insert
                        if True:
                             
                            return_return_insert = plus([var_10], (((insert (var_33)) (var_11))))
                            return return_return_insert
                return return_return_insert
    return return_insert

var_67 = dot(concat, (intersperce (' ')))

var_68 = dot(concat, (intersperce ('\n')))

def max(var_69):
    
    match var_69:
        case [var_10]:
            
            return_max = [var_10]
            return return_max
        case [var_10,*var_11]:
            var_70 = (max (var_11))
            
            return_max = var_70 if gt(var_70, var_10) else var_10
            return return_max
    return return_max

var_71 = lambda var_72: var_1

var_73 = lambda var_74: eqeq(var_1, ((var_55 (var_1))))

var_75 = (ae_filter (is_number))

def posImpares(var_76):
    
    match var_76:
        case [var_23,var_26,*var_11]:
            
            return_posImpares = plus([var_26], (posImpares (var_11)))
            return return_posImpares
        case _:
            
            return_posImpares = []
            return return_posImpares
    return return_posImpares

def posPares(var_77):
    
    match var_77:
        case []:
            
            return_posPares = []
            return return_posPares
        case [var_23]:
            
            return_posPares = [var_23]
            return return_posPares
        case [var_23,var_26,*var_11]:
            
            return_posPares = plus([var_23], (posPares (var_11)))
            return return_posPares
        case _:
            
            return_posPares = []
            return return_posPares
    return return_posPares

def iSorted(var_78):
    
    match var_78:
        case [var_23,var_26,*var_11]:
            
            return_iSorted = (iSorted ([var_26,*var_11])) if lteq(var_23, var_26) else False
            return return_iSorted
        case _:
            
            return_iSorted = True
            return return_iSorted
    return return_iSorted

def iSort(var_79):
    
    match var_79:
        case []:
            
            return_iSort = []
            return return_iSort
        case [var_10,*var_11]:
            
            return_iSort = ((insert (var_10)) ((times(iSort, var_11))))
            return return_iSort
    return return_iSort

def menor(var_80):
    
    match var_80:
        case '':
            def return_menor(var_81):    
                match var_81:
                    case '':
                        
                        return_return_menor = False
                        return return_return_menor
                    case _:
                        
                        return_return_menor = True
                        return return_return_menor
                return return_return_menor
        case [var_10,*var_11]:
            def return_menor(var_82):    
                match var_82:
                    case '':
                        
                        return_return_menor = False
                        return return_return_menor
                    case [var_23,*var_24]:
                        
                        if gt(((ascii (var_10))), ((ascii (var_23)))):
                             
                            return_return_menor = False
                            return return_return_menor
                        if lt(((ascii (var_10))), ((ascii (var_23)))):
                             
                            return_return_menor = True
                            return return_return_menor
                        if True:
                             
                            return_return_menor = ((menor (((concat (var_11))))) (((concat (var_24)))))
                            return return_return_menor
                return return_return_menor
    return return_menor

def elemMSet(var_83):
    
    match var_83:
        case var_33:
            def return_elemMSet(var_84):    
                match var_84:
                    case []:
                        
                        return_return_elemMSet = False
                        return return_return_elemMSet
                    case [(var_33,_),*_]:
                        
                        return_return_elemMSet = True
                        return return_return_elemMSet
                    case [_,*var_11]:
                        
                        return_return_elemMSet = ((elemMSet (var_33)) (var_11))
                        return return_return_elemMSet
                return return_return_elemMSet
    return return_elemMSet

def lengthMSet(var_85):
    
    match var_85:
        case []:
            
            return_lengthMSet = 0
            return return_lengthMSet
        case [(_,var_1),*var_11]:
            
            return_lengthMSet = plus(var_1, ((lengthMSet (var_11))))
            return return_lengthMSet
    return return_lengthMSet

def converteMSet(var_86):
    
    match var_86:
        case []:
            
            return_converteMSet = []
            return return_converteMSet
        case [(var_33,var_1),*var_11]:
            
            return_converteMSet = plus((((replicate (var_1)) (var_33))), ((converteMSet (var_11))))
            return return_converteMSet
    return return_converteMSet

def insereMSet(var_87):
    
    match var_87:
        case var_33:
            def return_insereMSet(var_88):    
                match var_88:
                    case []:
                        
                        return_return_insereMSet = [(var_33,1)]
                        return return_return_insereMSet
                    case [(var_33,var_1),*var_11]:
                        
                        return_return_insereMSet = [(var_33,plus(var_1, 1)),*var_11]
                        return return_return_insereMSet
                    case [var_10,*var_11]:
                        
                        return_return_insereMSet = plus([var_10], ((insereMSet (var_33)) (var_11)))
                        return return_return_insereMSet
                return return_return_insereMSet
    return return_insereMSet

def removeMSet(var_89):
    
    match var_89:
        case var_33:
            def return_removeMSet(var_90):    
                match var_90:
                    case []:
                        
                        return_return_removeMSet = []
                        return return_return_removeMSet
                    case [(var_33,var_1),*var_11]:
                        
                        return_return_removeMSet = var_11 if eqeq(var_1, 1) else [(var_33,minus(var_1, 1)),*var_11]
                        return return_return_removeMSet
                    case [var_10,*var_11]:
                        
                        return_return_removeMSet = plus([var_10], (((removeMSet (var_33)) (var_11))))
                        return return_return_removeMSet
                return return_return_removeMSet
    return return_removeMSet

var_91 = []

def partitionEithers(var_92):
    
    match var_92:
        case []:
            
            return_partitionEithers = ([],[])
            return return_partitionEithers
        case [{ 'a':var_1 },*var_11]:
            (var_93,var_94) = (partitionEithers (var_11))
            
            return_partitionEithers = (plus([var_1], var_93),var_94)
            return return_partitionEithers
        case [{ 'b':var_1 },*var_11]:
            (var_93,var_94) = (partitionEithers (var_11))
            
            return_partitionEithers = (var_93,plus([var_1], var_94))
            return return_partitionEithers
    return return_partitionEithers

def catMaybes(var_95):
    
    match var_95:
        case []:
            
            return_catMaybes = []
            return return_catMaybes
        case [None,*var_11]:
            
            return_catMaybes = (catMaybes (var_11))
            return return_catMaybes
        case [var_1,*var_11]:
            
            return_catMaybes = plus([var_1], ((catMaybes (var_11))))
            return return_catMaybes
    return return_catMaybes

def posicao(var_96):
    
    match var_96:
        case (var_1,var_3):
            def return_posicao(var_97):    
                match var_97:
                    case []:
                        
                        return_return_posicao = (var_1,var_3)
                        return return_return_posicao
                    case ['Norte',*var_11]:
                        
                        return_return_posicao = ((posicao ((var_1,plus(var_3, 1)))) (var_11))
                        return return_return_posicao
                    case ['Sul',*var_11]:
                        
                        return_return_posicao = ((posicao ((var_1,minus(var_3, 1)))) (var_11))
                        return return_return_posicao
                    case ['Oeste',*var_11]:
                        
                        return_return_posicao = ((posicao ((minus(var_1, 1),var_3))) (var_11))
                        return return_return_posicao
                    case ['Este',*var_11]:
                        
                        return_return_posicao = ((posicao ((plus(var_1, 1),var_3))) (var_11))
                        return return_return_posicao
                return return_return_posicao
    return return_posicao

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

var_104 = lambda var_105: eqeq((length ((((ae_filter ((lambda var_106: eqeq(ouou(eqeq(var_3, 'Este'), var_3), 'Oeste')))) (var_44))))), 0)

def vizinhos(var_107):
    
    match var_107:
        case { 'x':var_1,'y':var_3 }:
            def return_vizinhos(var_108):    
                match var_108:
                    case []:
                        
                        return_return_vizinhos = []
                        return return_return_vizinhos
                    case [{ 'x':var_99,'y':var_100 },*var_11]:
                        var_24 = ((vizinhos ({ 'x' : var_1,'y' : var_3})) (var_11))
                        
                        return_return_vizinhos = var_24 if gt(plus(((abs ((minus(var_1, var_99))))), ((abs ((minus(var_3, var_100)))))), 1) else plus([{ 'x' : var_99,'y' : var_100}], var_24)
                        return return_return_vizinhos
                return return_return_vizinhos
    return return_vizinhos

def mesmaOrdenada(var_109):
    
    match var_109:
        case [{ 'x':_,'y':var_3 },{ 'x':_,'y':var_100 },*var_11]:
            
            if excleq(var_3, var_100):
                 
                return_mesmaOrdenada = False
                return return_mesmaOrdenada
            if True:
                 
                return_mesmaOrdenada = (mesmaOrdenada ([{ 'x' : 0,'y' : var_100},*var_11]))
                return return_mesmaOrdenada
        case _:
            
            return_mesmaOrdenada = True
            return return_mesmaOrdenada
    return return_mesmaOrdenada

def interseccaoOk(var_110):
    
    match var_110:
        case var_44:
            
            return_interseccaoOk = lteq((length ((((ae_filter ((dot(negate, (lambda var_111: eqeq(var_46, 'Vermelho')))))) (var_44))))), 1)
            return return_interseccaoOk
    return return_interseccaoOk
