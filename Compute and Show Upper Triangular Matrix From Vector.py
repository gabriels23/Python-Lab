import functools
import itertools

# main :: IO ()
def main():
	xs = [1,2,3,4]
	#xs = [x for x in range(1, 101)]
	ys = upperTriangularMatrixAsVector(xs)
	
	# Output Sum Matrix
	print(unlines(map(lambda x: str(x), ys)))

def upperTriangularMatrixAsVector(xs):
	# mat = [[0 for row in range(0, 4)] for col in range(0, 4)]
	ys = []
	lng = len(xs)
	acc = 0
	for i in range(0, lng):
		for j in range(0, lng):
			# Accumulate values of Upper Triangular Matrix
			ys.append([xs[k] for k in range(i, j + 1)])
	return ys
    
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

# unlines :: [String] -> String
def unlines(xs):
    return '\n'.join(xs)

main()
