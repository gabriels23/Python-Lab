# Elias Generic Function Library

```python
import functools
import itertools

# main :: IO ()
def main():
	A = [1,2,3]
	print(innerProduct(A))

# GENERIC FUNCTIONS ------------------------------------------------------------
def length(xs):
	return 0 if xs == [] else 1 + length(tail(xs))

def elem(x, xs):
	return False if xs == [] else (x == head(xs)) or elem(x, tail(xs))

def head(xs):
	return xs[0]
	
def tail(xs):
	return xs[1:]

# FIX SLICE
# def slice(m, n, xs):
	# return take(n)(drop(m)(xs))

def sum(xs):
	return 0 if xs == [] else head(xs) + sum(tail(xs))
 
def product(xs):
	return 1 if xs == [] else head(xs) * product(tail(xs)) 

def max(x, y):
	return x if x - y >= 0 else y

def maximum(xs):
	return head(xs) if length(xs) == 1 else max(head(xs), maximum(tail(xs)))

def id(x):
	return x

def map(f, xs):
	return [] if length(xs) == 0 else [f(head(xs))] + map(f, tail(xs))

def filter1(p, xs):
	if (length(xs) == 0):
		return []
	else:
		if (p(head(xs))):
			return [head(xs)] + filter(p, tail(xs))
		else:
			return filter(p, tail(xs))
	
def filter2(p, xs):
	return [] if length(xs) == 0 else (
		[head(xs)] + filter(p, tail(xs)) if p(head(xs)) else filter(p, tail(xs))
	)
	
def pred(n):
	return n - 1

def succ(n):
	return n + 1
	
def enumFromTo(m, n):
	[m] if m == n else enumFromTo(m, n - 1) + [n]

def innerProduct(xs):
	return sum(map(lambda x: x * x, xs))
	
	
# PY - Prelude

# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
	return lambda xs: (
		xs[0:n]
		if isinstance(xs, list)
		else list(itertools.islice(xs, n))
	)

# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
	def go(xs):
		if isinstance(xs, list):
			return xs[n:]
		else:
			return take(n)(xs)
	return lambda xs: go(xs)

main()
```
