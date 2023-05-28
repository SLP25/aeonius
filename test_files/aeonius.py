import aeonius

"""aeonius

#1
def enumFromTo1:
    x -> y | x > y => []
           |       => [x] + (enumFromTo1 (x + 1) y)


#2
def enumFromThenTo1:
    x -> y -> z | x > z => []
                |       => [x] + (enumFromThenTo1 y (2 * y - x) z)

#3
op (+++):
    []      -> x => x
    [h, *t] -> x => [h] + (t +++ x)

#4
op (!!!):
    [h,*t] -> 0 => h
              n => t !!! (n - 1)


#5
def reverse1:
    []      => []
    [h, *t] => (reverse1 t) + [h]


#6
def take1:
    n -> []     => []
         [h,*t] => [h] + take1 (n - 1) t if n > 0 else []

#7
def drop1:
    n -> []     => []
         [h,*t] => drop1 (n - 1) t if n > 0 else [h,*t]

#8
def zip1:
    []       -> _        => []
    [h1,*t1] -> []       => []
                [h2,*t2] => [(h1,h2)] + (zip1 t1 t2)

#9
def elem1:
    x -> []               => False
         [h, *t] | h == x => True
                 |        => elem1 x t

#10
def replicate1:
    0 -> _ => []
    n -> a => [a] + (replicate1 (n - 1) a)

#11
def intersperce1:
    x -> []      => []
         [h]     => [h]
         [h, *t] => [h,x] + (intersperce1 x t) 

#12
def group1:
    []      => []
    [h]     => [[h]]
    [h, *t] => 
        [[h,h1,*t1],*t2] if h == h1 else [[h],[h1,*t1],*t2]
        [[h1, *t1],*t2] = group1 t


#13
def concat1:
    []     => []
    [h,*t] => h + (concat1 t)

#14
def inits1:
    []     => [[]]
    [h,*t] => [[]] + (ae_map (lambda y: [h] + y) (inits1 t))

#15
def tails1:
    []     => [[]]
    [h,*t] => [[h,*t]] + (tails1 t)

#16
def isPrefixOf1:
    p -> l => elem1 p (inits1 l)

#17
def isSuffixOf1:
    s -> l => elem1 s (tails1 l)

#18
def isSubsequenceOf1:
    [] -> l => True
    [h,*t] -> [] => False
              [h1,*t1] | h==h1 => isSubsequenceOf1 t t1
                       |       => isSubsequenceOf1 [h,*t] t1

#19
def elemIndices1:
    x -> l => 
            ae_map snd (ae_filter (lambda y: (fst y) == x) (zip1 l l1))
            n = length l
            l1 = enumFromTo1 0 (n - 1)


#20
def nub1:
    []     => []
    [h,*t] => 
        n if (elem1 h n) else ([h] + n)
        n = nub1 t

#21
def delete1:
    x -> []     => []
         [h,*t] => [h] + (delete1 x t) if x != h else t

#22
def deleteAll1:
    [] -> _ => []
    l -> []     => l
         [h,*t] => deleteAll1 (delete1 h l) t

#23
def union1:
    a -> b => a + (ae_filter (negate . ((flip elem1) a)) b)

#24
def intersect1:
    a -> b => ae_filter ((flip elem1) b) a

#25
def insert1:
    a -> []              => [a]
         [h, *t] | h > a => [a,h,*t]
                 |       => [h] + (insert1 a t)

#26
unwords1 = concat1 . intersperce1 [" "]

#27
unlines1 = concat1 . intersperce1 ["\n"]

def max1:
    [h]    => h
    [h,*t] => 
        m1 if m1 > h else h
        m1 = max1 t
        
#28
pMaior1 = head . (uncurry elemIndices1) . (maximum >< id) . dup


#29
temRepetidos1 = lambda x: x == (nub1 x)

#30
algarismos1 = ae_filter is_number

#31
def posImpares1:
    [h1,h2,*t] => [h2] + posImpares1 t
    _          => []

#32
def posPares1:
    []         => []
    [h1]       => [h1]
    [h1,h2,*t] => [h1] + posPares1 t
    _          => []


#33
def iSorted1:
    [h1,h2,*t] => iSorted1 [h2,*t] if h1 <= h2 else False
    _          => True

#34
def iSort1:
    []      => []
    [h, *t] => insert1 h (iSort1 t)

#35
def menor1:
    []     -> [] => False
              _  => True
    [h,*t] -> []                                => False
              [h1,*t1] | (ascii h) > (ascii h1) => False
                       | (ascii h) < (ascii h1) => True
                       |                        => menor1 t t1

#36
def elemMSet1:
    a -> []         => False
         [(b,_),*t] | a == b => True
                    |        => elemMSet1 a t
         [_,*t]     => elemMSet1 a t

#37
def lengthMSet1:
    []         => 0
    [(_,x),*t] => x + (lengthMSet1 t)


#38
def converteMSet1:
    []         => []
    [(a,x),*t] => (replicate1 x a) + (converteMSet1 t)


#39
def insereMSet1:
    a -> []         => [(a,1)]
         [(b,x),*t] | a == b => [(a,x + 1),*t]
                    |        => [(b,x)] + (insereMSet1 a t) 
         [h,*t]     => [h] + insereMSet1 a t

#40
def removeMSet1:
    a -> [] => []
         [(b,x),*t] | a == b => t if x == 1 else [(a, x - 1), *t]
                    |        => [(b,x)] + (removeMSet1 a t)
         [h,*t] => [h] + (removeMSet1 a t)


#41
constroiMSet1 = ae_map ((head >< length) . dup) . group1

# Um either é um dicionario: {"1": valor} ou {"2": valor}
#42
def partitionEithers1:
    [] => ([],[])
    [{1: x},*t] => 
        ([x]+a1, b1)
        (a1,b1) = partitionEithers1 t
    [{2: x},*t] => 
        (a1,[x] +  b1)
        (a1,b1) = partitionEithers1 t

# Maybe => Valor ou None

#43
def catMaybes1:
    []         => []
    [None, *t] => catMaybes1 t
    [x, *t]    => [x] + (catMaybes1 t)

# Posicoes sao strings
#44
def posicao1:
    (x,y) -> []            => (x,y)
             ["Norte", *t] => posicao1 (x, y + 1) t
             ["Sul", *t]   => posicao1 (x, y - 1) t
             ["Oeste", *t] => posicao1 (x - 1, y) t
             ["Este", *t]  => posicao1 (x + 1, y) t

#45
def caminho1:
    (x1,y1) -> (x2, y2) | x1 <= x2 && y1 <= y2 => (replicate1 (x2 - x1) "Este") + (replicate1 (y2 - y1) "Norte")
                        | x1 <= x2 && y1 > y2  => (replicate1 (x2 - x1) "Este") + (replicate1 (y1 - y2) "Sul")
                        | x1 > x2 && y1 <= y2  => (replicate1 (x1 - x2) "Oeste") + (replicate1 (y2 - y1) "Norte")
                        | x1 > x2 && y1 > y2   => (replicate1 (x1 - x2) "Oeste") + (replicate1 (y1 - y2) "Sul")

#46
vertical1 = lambda l: length (ae_filter (lambda y: elem1 y (["Oeste", "Este"])) l) == 0

# Estrutura é um tuplo (x,y)
#47
def maisCentral1:
   [h] => h
   [(x,y),*t] =>
       (x,y) if d <= d1 else (x1,y1)
       (x1,y1) = maisCentral1 t
       d1 = (x1 ^ 2) + (y1 ^ 2)
       d = (x ^ 2) + (y ^ 2)


#48
def vizinhos1:
    (x,y) -> [] => []
             [(x1,y1),*t] => 
                 t1 if (abs (x-x1)) + (abs (y-y1)) > 1 else [(x1,y1)] + t1
                 t1 = vizinhos1  (x,y) t

#49
def mesmaOrdenada1:
    [ (_,y),  (_, y1),*t] => 
        False if y != y1 else mesmaOrdenada1 [(0,y1),*t]
    _ => True


#50
def interseccaoOk1:
    l => length (ae_filter (negate . (lambda s: s == "Vermelho")) l) <= 1
"""