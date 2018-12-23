## Solutions to homework

```python
import functools
import itertools

# main :: IO ()
def main():
	s = "hello"
	xs = [3,2,1,4,5]
	print(sum(xs))
	print(maximum(xs))
	print(toUpper(s))
	
def sum(xs):
	return 0 if len(xs) == 0 else head(xs) + sum(tail(xs))

def maximum(xs):
	return head(xs) if len(xs) == 1 else max(head(xs), maximum(tail(xs)))

def toUpper(str):
	if (len(str) == 0):
		return ''
	else:
		if (ord(head(str)) < 97 and ord(head(str)) > 122):
			return head(str) + toUpper(tail(str))
		else:
			return chr(ord(head(str)) - 32) + toUpper(tail(str))

# toUpper function done with conditional expression
def toUpperExpression(str):
	return '' if (len(str) == 0) else (
		head(str) + toUpper(tail(str)) if (
		ord(head(str)) < 97 and ord(head(str)) > 122) else (
		chr(ord(head(str)) - 32) + toUpper(tail(str))
	)
	
	
# GENERIC ----------------------------------------------------------------------
# PY - Prelude

# head :: [a] -> a
def head(xs):
	return xs[0]

# sum :: [Num] -> Num
def sum_(xs):
	return sum(xs)

# tail :: [a] -> [a]
def tail(xs):
	return xs[1:]

main()
```
