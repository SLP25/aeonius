
def elemIndices(var_51):
    
    match var_51:
        case var_1:
            def return_elemIndices(var_52):    
                match var_52:
                    case var_44:
                        var_15 = (length (var_44))
                        
                        var_53 = ((enumFromTo (0)) ((minus(var_15)(1))))
                        
                        return_return_elemIndices = ((ae_map (snd)) ((((ae_filter ((lambda var_54: eqeq(((fst (var_54))))(var_1)))) ((((zip (var_44)) (var_53))))))))
                        return return_return_elemIndices
                return return_return_elemIndices
    return return_elemIndices

var_55 = dot(((ae_map (head))))((group))




def union(var_60):
    
    match var_60:
        case var_33:
            def return_union(var_61):    
                match var_61:
                    case var_62:
                        
                        return_return_union = plus(var_33)(((ae_filter ((dot(negate)((((((flip (elem))) (var_33))) (var_62))))))))
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


var_67 = dot(concat)((intersperce (' ')))

var_68 = dot(concat)((intersperce ('\n')))



var_71 = lambda var_72: var_72

var_73 = lambda var_74: eqeq(var_74)(((var_55 (var_74))))

var_75 = (ae_filter (is_number))


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
                        
                        if gt(((ascii (var_10))))(((ascii (var_23)))):
                             
                            return_return_menor = False
                            return return_return_menor
                        if lt(((ascii (var_10))))(((ascii (var_23)))):
                             
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


def insereMSet(var_87):
    
    match var_87:
        case var_33:
            def return_insereMSet(var_88):    
                match var_88:
                    case []:
                        
                        return_return_insereMSet = [(var_33,1)]
                        return return_return_insereMSet
                    case [(var_33,var_74),*var_11]:
                        
                        return_return_insereMSet = [(var_33,plus(var_74)(1)),*var_11]
                        return return_return_insereMSet
                    case [var_10,*var_11]:
                        
                        return_return_insereMSet = plus([var_10])(((insereMSet (var_33)) (var_11)))
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
                    case [(var_33,var_74),*var_11]:
                        
                        return_return_removeMSet = var_11 if eqeq(var_74)(1) else [(var_33,minus(var_74)(1)),*var_11]
                        return return_return_removeMSet
                    case [var_10,*var_11]:
                        
                        return_return_removeMSet = plus([var_10])((((removeMSet (var_33)) (var_11))))
                        return return_return_removeMSet
                return return_return_removeMSet
    return return_removeMSet

var_91 = []







var_104 = lambda var_105: eqeq((length ((((ae_filter ((lambda var_106: eqeq(ouou(eqeq(var_106)('Este'))(var_106))('Oeste')))) (var_105))))))(0)

var_107 = lambda var_108: var_108


def interseccaoOk(var_112):
    
    match var_112:
        case var_108:
            
            return_interseccaoOk = lteq((length ((((ae_filter ((dot(negate)((lambda var_113: eqeq(var_113)('Vermelho')))))) (var_108))))))(1)
            return return_interseccaoOk
    return return_interseccaoOk
