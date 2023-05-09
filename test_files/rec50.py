def negate(b):
    return False if b else True

def find(a,l):
    h,*t=l
    if a == h:return 0
    return 1 + find(a,t) 

#1
def enumFromTo(f,t):
    if t-f==0: return [f]
    else: return [f]+enumFromTo(f+1, t)
#2
def enumFromThenTo(x,y,z):
    if x > z: return []
    else: return [x] + enumFromThenTo(y,(2 * y - x),z)
#3
def pp(l1,l2):
    if l1==[]:
        return l2
    else:
        h,*t = l1
        return [h] + pp(t,l2)
    
#4
def index(l,p):
    h,*t=l
    if p==0:
        return h
    else:
        return index(t, p-1)
    
#5
def reverse(l):
    if l==[]:return []
    else: 
        h,*t=l
        return reverse(t) + [h]
#6
def take(n,l):
    if l==[]:
        return []
    else:
        h,*t = l
        return [h] + take(n - 1,t if n-1 > 0 else [])
#7
def drop(n,l):
    if n==0: return l
    if l==[]: return []
    else:
        h,*t=l
        return drop(n-1,t)
#8
def zip(l1,l2):
    if l1==[] or l2==[]: return []
    else:
        [h1,*t1]=l1
        [h2,*t2]=l2
        return [(h1,h2)] + zip(t1,t2)
#9
def elem(e,l):
    if l==[]:return False
    h,*t=l
    if e==h: return True
    return elem(e, t)

#10
def replicate(n,a):
    if n==0:return []
    else: return [a]+replicate(n-1, a)
    
#11
def intersperce(e,l):
    if l==[]:return []
    h,*t=l
    if l==[h]:return [h]
    else: return [h,e]+intersperce(e, t)

#12
def group(l):
    if l==[]: return []
    h,*t=l
    if l==[h]: return [[h]]
    else:
        h2,*t2 = group(t)
        h1,*t1 = h2
        return [[h]+h2]+t2 if h==h1 else [[h]]+[h2]+t2


#13
def concat(l):
    if l==[]:return []
    else:
        h,*t=l
        return h+concat(t)

#14
def inits(l):
    if l==[]:
        return [[]]
    else:
        *h,t=l
        return inits(h)+[l]

#15
def tails(l):
    if l==[]:
        return [[]]
    else:
        h,*t =l
        return [[h,*t]] + tails(t)
    
#16
def isPrefixOf(p,l):
    return elem(p,inits(l))

#17
def isSuffixOf(s,l):
    return elem(s,tails(l))


#18
def isSubsequenceOf(s,l):
    return bool(len(filter(lambda x:x,map(lambda x:isPrefixOf(s,x),l)))>0)

#19
def elemIndices(x,l):
    return map(lambda k:k[1],filter(lambda k:k[0]==x,zip(l,enumFromTo(0, len(l)-1))))


#20
def nub(l):
    def nubb(l,ls):
        if l==[]:
            return []
        else:
            x,*xs=l
            if elem(x,ls): return nubb(xs,ls)
            else: [x]+nubb(xs,[x]+ls)            
    return nubb(l,[])

#21
def delete(x,l):
    if l==[]:return []
    h,*t=l
    return t if h==x else [h]+delete(x,t)


#22
def deleteAll(l1,l2):
    if l2==[]:return l1
    h,*t = l2
    return deleteAll(delete(h,l1),t)

#23
def union(a,b):
    return a + list(filter(lambda x: negate(elem(x, a)),b))

#24
def intersect(a,b):
    return list(filter(lambda x: elem(x,b),a))

#25
def insert(a,l):
    if l==[]:return [a]
    h,*t=l
    if h>a:return [a,h]+t
    else: return [h]+insert(a,t)

#26
def unwords(l):
    return concat(intersperce(" ",l))

#27
def unlines(l):
    return concat(intersperce("\n",l))


#28
def pMaior(l):
    def max(l):
        h,*t=l
    if l==[h]:return [h]
    else:
        m1=max(t)
        return m1 if m1 > h else h
    return find(max(l),l)


#29
def temRepetidos(x):
    return x == nub(x)

#30
def algarismos(x):
    return list(filter(lambda y:y.isnumeric(),x))

#31
def posImpares(l):
    if len(l)<2:
        return []
    else:
        h1,h2,*t = l
        return [h2] + posImpares(t)


#32
def posPares(l):
    if l==[]:return []
    h1,*t=l
    if l==[h1]:return [h1]
    h2,*t=t
    return [h1] + posPares(t)


#33
def iSorted(l):
    if len(l)<2:return True
    h1,h2,*t = l
    return iSorted([h2]+t) if h1 <= h2 else False

#34
def iSort(l):
    if l==[]:return []
    h,*t=l
    return insert(h,iSort(t))

#35
def menor(s1,s2):
    if s1=="":
        if s2=="":return False
        else :return True
    h,*t = s1
    if s2 == "": return False
    h1,*t1 =s2
    if ord(h) > ord(h1):return False
    elif ord(h) < rd(h1):return True
    return menor(concat(t),concat(t1))

#36
def elemMSet(a,l):
    if l==[]:return False
    (b,_),*t = l
    if a==b: return True
    else: return elemMSet(a, t)

#37
def lengthMSet(l):
    if l==[]:return 0
    (_,x),*t=l
    return x + lengthMSet(t)


#38
def converteMSet(l):
    if l==[]:return []
    (a,x),*t=l
    return replicate(x,a) + converteMSet(t)


#39
def insereMSet(a,l):
    if l==[]: return [(a,1)]
    h,*t=l
    if h[0]==a: return [(a,h[1] + 1)]+t
    return [h] + insereMSet(a,t)


#40
def removeMSet(a,l):
    if l==[]:return []
    h,*t=l
    if h[0]==a: return t if h[1] == 1 else [(a, h[1] - 1)]+t
    return [h] + removeMSet(a,t)

#41
def constroiMSet(l):
    gl=group(l)
    return list(map(lambda x:(x[0],len(x)),gl))

# Um either é um dicionario: {"a": valor} ou {"b": valor}
#42
def partitionEithers(l):
    if l==[]:return ([],[])
    h,*t =l
    a1,b1 = partitionEithers(t)
    if "a" in h:
        x=h["a"]
        return ([x]+a1, b1)
    else: 
        x=h["b"]
        return (a1,[x] + b1)
        

# Maybe => Valor ou None
#43
def catMaybes(l):
    if l==[]:return []
    h,*t=l
    if h==None: return catMaybes(t)
    else:return [h] + catMaybes(t)

# Posicoes sao strings
#44
def posicao(xy,l):
    x,y=xy
    if l==[]:return (x,y)
    h,*t=l
    if h=="Norte": posicao((x, y + 1),t)
    elif h=="Sul": posicao((x, y - 1),t)
    elif h=="Oeste": posicao((x - 1, y),t)
    elif h=="Este": posicao((x + 1, y),t)
    
    
#45
def caminho(p1,p2):
    x1,y1=p1
    x2, y2=p2
    if x1 <= x2 and y1 <= y2 :return replicate((x2 - x1),"Este") + replicate((y2 - y1) ,"Norte")
    elif x1 <= x2 and y1 > y2  :return replicate((x2 - x1),"Este") + replicate((y1 - y2) ,"Sul")
    elif x1 > x2 and y1 <= y2  :return replicate((x1 - x2),"Oeste") + replicate( (y2 - y1), "Norte")
    elif x1 > x2 and y1 > y2   :return replicate((x1 - x2),"Oeste") + replicate( (y1 - y2), "Sul")

#46
def vertical():
    return len(filter(lambda y: y == "Este" or y == "Oeste",l)) == 0

# Estrutura é um dicionario {"x": x, "y": y}
#47
def maisCentral(l):
    h,*t=l
    if [h]==l:return h
    rt=maisCentral(t)
    x1=rt['x']
    y1=rt['y']
    x=h['x']
    y=h['y']
    d1 = (x1 ^ 2) + (y1 ^ 2)
    d = (x ^ 2) + (y ^ 2)
    return h if d <= d1 else rt
        
        
#48
def vizinhos(p,l):
    if l==[]:return []
    x,y=p['x'],p['y']
    h,*t=l
    x1,y1=h['x'],h['y']
    t1 = vizinhos(p,t)
    return t1 if ((abs(x-x1)) + (abs(y-y1))) > 1 else [h] + t1

#49
def mesmaOrdenada(l):
    if len(l)<2:return True
    h1,h2,*t=l
    y1,y2=h1['y'],h2['y']
    if y1 != y2:return False
    else: return mesmaOrdenada([h2]+t)



#50
def interseccaoOk(l):
    return len(filter(lambda s: s != "Vermelho",l)) <= 1