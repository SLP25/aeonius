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