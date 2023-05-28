import aeonius

"""aeonius

y = (1,)

def batata:
    x => x + 1

op(<$>):
    x -> [h, *t] => [h, *x] <$> t
         [] => x

a = [1,2,3] <$> [4,5] <$> [6,7]

infixr 4 <$>

def g:
    str -> 0 => ""
           n => str + g str (n - 1)

def maap:
    h -> []      => []
         [h1,*t] => [h h1] + maap h t

b = maap batata [9,10]

def mult2:
    x => 2 * i for i in x if i % 2 == 1

def hasOne:
    {1: z} => True
    {}     => False

def whiile: c -> f -> i | c i => whiile c f (f i)
                        | => i

c = whiile ((!=) 10) (flip (-) 1) 20

def foor: f -> i -> 0 => i
                    n => foor f (f i) (n - 1)

d = foor (flip (/) 2) 16 6

"""


print(c)
print(d)
print(hasOne({1:2}))
