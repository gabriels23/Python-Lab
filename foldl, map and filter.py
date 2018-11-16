import functools

# main :: IO ()
def main():
    xs = [1, 2, 3, 4, 5]
    ys = map(lambda x: x * 2, xs)
    zs = filter(lambda x: x % 2 == 0, xs)
    ws = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, xs))

    n = foldl(multiply, 1, xs)
    print(n)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# GENERIC ----------------------------------------------------------------------
# PY - Prelude

# filter :: (a -> Bool) -> [a] -> [a]
def filter_(f):
    return lambda xs: filter(f, xs)

# foldl :: (a -> b -> a) -> a -> [b] -> a
def foldl(f, a, xs):
    return functools.reduce(f, xs, a);

# map :: (a -> b) -> [a] -> [b]
def _map(f):
    return lambda xs: list(map(f, xs))

main()
