# Summary of 21-12-2018 Class

```python
import functools
import itertools

# main :: IO ()
def main():
	A = range(-10,11)
	B = [0,1]
	xs = [5*x for x in A if abs(2*x) <= 8]
	print(elem(0, B))

def length(xs):
	return 0 if (xs == []) else 1 + length(tail(xs))

def elem(x, xs):
	return x in xs
	
# GENERIC ----------------------------------------------------------------------
# PY - Prelude

# tail :: [a] -> [a]
def tail(xs):
	return xs[1:]

main()
```
