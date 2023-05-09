"""aeonius

#Auxiliar (temp enquanto nao ha aeonius)
def length:
    []     => 0
    [_,*t] => 1 + (length t)

def filter:
    f -> [] => []
         [h,*t] => [h] + (filter f t) if f h else (filter f t)

def map:
    f -> [] => []
         [h,*t] => [f h] + (map t)

def fst:
    (x,y) => x

def snd:
    (x,y) => y

def head:
    [h,*_] => h

def negate:
    b => False if b else True

def id:
    x => x

def flip:
    f => f

def is_number:
    f => True

def ascii:
    _ => 1

def dup:
    f => (f,f)

def abs:
    a | a > 0 => a
      |       => -1 * a

#assumes the value exists
def find:
    a -> [h,*t] | a == h => 0 
                |        => 1 + (find a t) 


#1
def enumFromTo:
    x -> y | x > y => []
           |       => [x] + (enumFromTo (x + 1) y)


#2
def enumFromThenTo:
    x -> y -> z | x > z => []
                |       => [x] + (enumFromThenTo y (2 * y - x) z)

#3
op (++):
    []      -> x => x
    [h, *t] -> x => [h] + (t ++ x)

#4
op (!!):
    [h,*t] -> 0 => h
              n => t !! (n - 1)


#5
def reverse:
    []      => []
    [h, *t] => (reverse t) + [h]


#6
def take:
    n -> []     => []
         [h,*t] => [h] + take (n - 1) t if n > 0 else []

#7
def drop:
    n -> []     => []
         [h,*t] => drop (n - 1) t if n > 0 else [h,*t]

#8
def zip:
    []       -> _        => []
    [h1,*t1] -> []       => []
                [h2,*t2] => [(h1,h2)] + (zip t1 t2)

#9
def elem:
    x => length (filter (lambda y: x == y)) > 0

#10
def replicate:
    0 -> _ => []
    n -> a => [a] + (replicate (n - 1))

#11
def intersperce:
    x -> []      => []
         [h]     => [h]
         [h, *t] => [h,x] + (intersperce x t) 

#12
def group:
    []      => []
    [h]     => [[h]]
    [h, *t] => 
        [[h,h1,*t1],*t2] if h == h1 else [[h],[h1,*t1],*t2]
        [[h1, *t1],*t2] = group t


#13
def concat:
    []     => []
    [h,*t] => h + (concat t)

#14
def inits:
    []     => []
    [h,*t] => [] + (map (lambda y: h + y) (inits t))

#15
def tails:
    []     => []
    [h,*t] => [[h,*t]] + (tails t)

#16
def isPrefixOf:
    p -> l => elem p (inits l)

#17
def isSuffixOf:
    s -> l => elem s (tails l)

#18
def isSubsequenceOf:
    s -> l =>
            length ((filter id) . (map (aux s)) l) > 0
            def aux:
                s => isPrefixOf s


#19
def elemIndices:
    x -> l => 
            map snd (filter (lambda y: (fst y) == x) (zip l l1))
            n = length l
            l1 = enumFromTo 0 (n - 1)


#20
nub = (map head) . (group)

#21
def delete:
    x -> []     => []
         [h,*t] => [h] + (delete x t) if x <> h else t

#22
def deleteAll:
    l -> []     => l
         [h,*t] => deleteAll (delete h l) t

#23
def union:
    a -> b => a + (filter (negate . ((flip elem) a) b))

#24
def intersect:
    a -> b => filter ((flip elem) b) a

#25
def insert:
    a -> []              => [a]
         [h, *t] | h > a => [a,h,*t]
                 |       => [h] + (insert a t)

#26
unwords = concat . intersperce " "

#27
unlines = concat . intersperce "\n"

#28
def max:
    [h]    => [h]
    [h,*t] => 
        m1 if m1 > h else h
        m1 = max t

pMaior = lambda x: (find (max x) x)


#29
temRepetidos = lambda x: x == (nub x)

#30
algarismos = filter is_number

#31
def posImpares:
    [h1,h2,*t] => [h2] + posImpares t
    _          => []

#32
def posPares:
    []         => []
    [h1]       => [h1]
    [h1,h2,*t] => [h1] + posPares t
    _          => []


#33
def iSorted:
    [h1,h2,*t] => iSorted [h2,*t] if h1 <= h2 else False
    _          => True

#34
def iSort:
    []      => []
    [h, *t] => insert h (iSort *t)

#35
def menor:
    ""     -> "" => False
              _  => True
    [h,*t] -> ""                                => False
              [h1,*t1] | (ascii h) > (ascii h1) => False
                       | (ascii h) < (ascii h1) => True
                       |                        => menor (concat t) (concat t1)

#36
def elemMSet:
    a -> []         => False
         [(a,_),*_] => True
         [_,*t]     => elemMSet a t

#37
def lengthMSet:
    []         => 0
    [(_,x),*t] => x + (lengthMSet t)


#38
def converteMSet:
    []         => []
    [(a,x),*t] => (replicate x a) + (converteMSet t)


#39
def insereMSet:
    a -> []         => [(a,1)]
         [(a,x),*t] => [(a,x + 1),*t]
         [h,*t]     => [h] + insereMSet a t


#40
def removeMSet:
    a -> [] => []
         [(a,x),*t] => t if x == 1 else [(a, x - 1), *t]
         [h,*t] => [h] + (removeMSet a t)


#41
constroiMSet = map ((head >< length) . dup) group

#42
# Um either é um dicionario: {"a": valor} ou {"b": valor}

def partitionEithers:
    [] => ([],[])
    [{"a": x},*t] => 
        ([x]+a1, b1)
        (a1,b1) = partitionEithers t
    [{"b": x},*t] => 
        (a1,[x] +  b1)
        (a1,b1) = partitionEithers t


#43
# Maybe => Valor ou None

def catMaybes:
    []         => []
    [None, *t] => catMaybes t
    [x, *t]    => [x] + (catMaybes t)


#44
# Posicoes sao strings

def posicao:
    (x,y) -> []            => (x,y)
             ["Norte", *t] => posicao (x, y + 1) t
             ["Sul", *t]   => posicao (x, y - 1) t
             ["Oeste", *t] => posicao (x - 1, y) t
             ["Este", *t]  => posicao (x + 1, y) t

#45
def caminho:
    (x1,y1) -> (x2, y2) | x1 <= x2 && y1 <= y2 => (replicate (x2 - x1) "Este") + (replicate (y2 - y1) "Norte")
                        | x1 <= x2 && y1 > y2  => (replicate (x2 - x1) "Este") + (replicate (y1 - y2) "Sul")
                        | x1 > x2 && y1 <= y2  => (replicate (x1 - x2) "Oeste") + (replicate (y2 - y1) "Norte")
                        | x1 > x2 && y1 > y2   => (replicate (x1 - x2) "Oeste") + (replicate (y1 - y2) "Sul")

#46
vertical = lambda l: length (filter (lambda y: y == "Este" || y == "Oeste") l) == 0

#47
# Estrutura é um dicionario {"x": x, "y": y}

def maisCentral:
    [h] => h
    [{"x": x, "y": y},*t] =>
        {"x": x, "y": y} if d <= d1 else {"x": x1, "y": y1}
        {"x": x1, "y": y1} = maisCentral t
        d1 = (x1 ^ 2) + (y1 ^ 2)
        d = (x ^ 2) + (y ^ 2)


#48

def vizinhos:
    {"x": x, "y": y} -> [] => []
                        [{"x": x1, "y":y1},*t] => 
                            t1 if (abs (x-x1)) + (abs (y-y1)) > 1 else [{"x": x1, "y":y1}] + t1
                            t1 = vizinhos  {"x": x, "y": y} t

#49   
def mesmaOrdenada:
    [ {"x": _, "y": y},  {"x": _, "y": y1},*t] | y != y1 => False
                                               |         => mesmaOrdenada [{"x": 0, "y": y1},*t]
    _ => True


#50
def interseccaoOk:
    l => length (filter (negate . (lambda s: s == "Vermelho")) l) <= 1

"""