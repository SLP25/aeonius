#1
def enumFromTo(i,f):
    return list(range(i,f+1))
#2
def enumFromThenTo(i,t,f):
    return list(range(i,f+1,t-i))
#3
def pp(a,b):
    return a+b
#4
def index(l,p):
    return l[p]
#5
def reverse(l):
    return l[::-1]
#6
def take(n,l):
    return l[:n]
#7
def drop(n,l):
    return l[n:]
#8
    def zipp(l1,l2):
        return list(zip(l1,l2))
#9
def elem(e,l):
    return e in l
#10
def replicate(n,a):
    return [a for i in range(n)]
#11
def intersperse(e,l):
    last=l.pop()
    ln=[]
    for i in l:
        ln.append(i)
        ln.append(e) 
    ln.append(last) 
    return ln
#12
def group(l):
    if l==[]:return []
    lr=[[l.pop(0)]]
    for i in l:
        if i==lr[-1][0]:
            lr[-1].append(i)
        else:
            lr.append([i])
    return lr
#13
def concat(l):
    r=[]
    for i in l:
        r+=i
    return r
#14
def inits(l):
    lr=[]
    for i in range(len(l)+1):
        lr.append(l[:i])
    return lr
#15
def tails(l):
    lr=[]
    for i in range(len(l)+1):
        lr.append(l[i:])
    return lr
#16
def isPrefixOf(l1,l2):
    return l1==l2[:len(l1)]
#17
def isSuffixOf(l1,l2):
    return l1==l2[-len(l1):]
#18
def isSubsequenceOf(l1,l2):
    if l1==[]: return True
    for i in l2:
        if i==l1[0]:
            l1.pop(0)
            if l1==[]:
                return True
    return False
#19
def elemIndicesAux(a,l):
    for p,i in enumerate(l):
        if a==i:
            yield p

def elemIndices(a,l):
    return list(elemIndicesAux(a, l))
#20
def nub(l):
    return list(set(l))

#21
def delete(x,l):
    l.remove(x)
    return l

#22
def deleteAll(l1,l2):
    for i in l2:
        l1.remove(i)
    return l1

#23
def union(a,b):
    c=[]+a
    for i in b:
        if i not in a:
            c.append(i)
    return c

#25
def intersectAux(a,b):
    for i in a:
        if i in b:
            yield i

#24
def intersect(a,b):
    return list(intersectAux(a, b))

#25
def insert(a,l):
    if l==[]:return [a]
    h,*t=l
    if h>a:return [a,h]+t
    else: return [h]+insert(a,t)
    
#26
def unwords(l):
    return " ".join(l)

#27
def unlines(l):
    return "\n".join(l)


#28
def maxx(l):
    return max(l)

def pMaior(l):
    return max(enumerate(l),key=lambda x:x[1])[0]


#29
def temRepetidos(x):
    return x!=list(set(x))

#30
def algarismos(x):
    return list(filter(lambda y:y.isnumeric(),x))

#31
def posImpares(l):
    return l[1::2]

#32
def posPares(l):
    return l[0::2]
#33
def iSorted(l):
    return l.sorted()

#34
def iSort(l):
    return sorted(l)
#35
def menor(s1,s2):
    return s1<s2
#36
def elemMSet(a,l):
    return a in map(lambda x:x[0],l)
#37
def lengthMSet(a,l):
    return sum(map(lambda x:x[1],l))

def converteMSetAux(l):
    for i in l:
        for j in range(i[1]):
            yield i[0]
#38
def converteMSet(l):
    return list(converteMSetAux(l))
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
def constroiMSetAux(l):
    for i in set(l):
        yield (i,l.count(i))
        
def constroiMSet(l):
    return list(constroiMSetAux(l))
#42
def partitionEithers(l):
    r={"a":[],"b":[]}
    for i in l:
        for k,v in i.items():
            r[k].append(v)
    return (r['a'],r['b'])

#43
# Maybe => Valor ou None

def catMaybes(l):
    return list(filter(lambda x:x!=None, l))

#44
# Posicoes sao strings

def posicao(xy,l):
    x,y=xy
    if l==[]:return (x,y)
    for p in l:
        if p=="Norte": y+=1
        elif p=="Sul": y-=1
        elif p=="Oeste":x -= 1
        elif p=="Este":x += 1
    return (x,y)

#45
def caminho(p1,p2):
    x1,y1=p1
    x2, y2=p2
    norm=lambda x:0 if x<0 else x
    r=[]
    r+=['Este']*norm(x2 - x1)
    r+=['Oeste']*norm(x1 - x2)
    r+=['Norte']*norm(y2 - y1)
    r+=['Sul']*norm(y1 - y2)
    return r

#46
def vertical():
    return len(filter(lambda y: y == "Este" or y == "Oeste",l)) == 0
#47
def maisCentral(l):
    return min(l,key=lambda x: (x['x'] ^ 2) + (x['y'] ^ 2))
#48
def vizinhos(p,l):
    return list(filter(lambda h:(abs(p['x']-h['x']) + abs(p['y']-h['y'])) <= 1,l))
#49
def mesmaOrdenada(l):
    return len(set(map(lambda x:x['y'],l)))==1
#50
def interseccaoOk(l):
    return len(filter(lambda s: s != "Vermelho",l)) <= 1