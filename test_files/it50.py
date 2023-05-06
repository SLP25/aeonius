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
            