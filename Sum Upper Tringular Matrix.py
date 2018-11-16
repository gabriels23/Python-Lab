import functools
import itertools

# main :: IO ()
def main():
	xs = [1, 2, 3, 4]
	a = [[0 for row in range(0, 4)] for col in range(0, 4)]
	
	for i in range(0, 4):
		for j in range(0, 4):
			# Build Upper Triangular Matrix
			a[i][j] = sum([xs[k] for k in range(i, j + 1)])

	# Sum Matrix
	n = sum(flatten(a))
	print(n)
    
# GENERIC ----------------------------------------------------------------------
# PY - Prelude

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    return lambda xs: list(
        itertools.chain.from_iterable(
            map(f, xs)
        )
    )
    
# concatMap :: (a -> [b]) -> [a] -> [b]
# def concatMap(f):
#     return lambda xs: [ys[0] for ys in [f(x) for x in xs] if ys]

# Flatten arbitrarily nested lists
# flatten :: NestedList a -> [a]
def flatten(x):
    return concatMap(flatten)(x) if isinstance(x, list) else [x]

# map :: (a -> b) -> [a] -> [b]
def _map(f):
    return lambda xs: list(map(f, xs))

# sum :: [Num] -> Num
def sum_(xs):
    return sum(xs)

main()
