import aeonius

"""aeonius

y = (1,)

def f:
    [] => 0
    [_,*x] => f x + 1

op(<$>):
    x -> [h, *t] => [h, *x] <$> t
         [] => x

a = [1,2,3] <$> [4,5] <$> [6,7]

infixr 4 <$>

def g:
    str -> 0 => ""
           n => str + g str (n - 1)

def foor:
    f -> i -> 0 => i
         i -> n => while f (i-1) (f i)

b = foor ((+) 1) 0 10

"""

print(b)
