# Summary of 20-12-2018 Class


## Basic Concepts

### What is a variable?

- It is an identifier associated to a memory location.

### Basic data types

- Int

- Float

- String (In Python, use single quotes `'`)

- Bool (In Python, don't use quotes. Remember, it's a reserved keyword)

### Structured Data Types

- Lists

- How to access an element in the `nth` position (_Hint: indexes start at 0_)

	- Using bracket notation `[]`, e.g.
		```python
		xs = ["a","b","c"]
		xs[1] # --> "b"
		```

### Function Definitions

- `return` keyword

### Function Invocations

- Always with parenthesis

## Real World Examples

### List comprehensions
```python
import functools
import itertools

# main :: IO ()
def main():
	# Set Comprehension -> List Comprehension
	# {f x | p x}
	# In set comprehension would be, 
	# A = {1,2,3}
	# {x ^ 2 | x belongs to A}
	A = [1,2,3]
	ws = [x**2 for x in A]

	# Only even numbers
	xs = [x**2 for x in A if x % 2 == 0]
	
	B = [1,2,3,4,5,6,7,8,9,10]
	ys = [5*a + 2*b for a in B for b in B]
	
	B = [1,2,3,4,5,6,7,8,9,10]
	zs = [2*k + 1 for k in B]
	
	# Print to the screen
	print(ws)
	print(xs)
	print(ys)
	print(zs)
	
# GENERIC ----------------------------------------------------------------------

main()
```

### Functions Definitions
```python
import functools
import itertools

# main :: IO ()
def main():
	print("Predecesor of number 7 is: ")
	print(pred(7))
	print("Succesor of number 7 is: ")
	print(succ(7))
	print("Max between 8 and 15 is: ")
	print(min(8,15))
	print("Min between 8 and 15 is: ")
	print(max(8,15))

# FUNCTION DEFINITIONS
# pred :: Enum a => a -> a
def pred(n):
	return n - 1
	
# succ :: Enum a => a -> a
def succ(n):
	return n + 1

# min :: Ord a => a -> a -> a
def min(x,y):
	if (x <= y):
		return x
	else:
		return y

# With If Statement
# max :: Ord a => a -> a -> a
def max(x,y):
	if (x >= y):
		return x
	else:
		return y
		
# With Conditional Expression
# min :: Ord a => a -> a -> a
def minC(x,y):
	return x if (x <= y) else y

# max :: Ord a => a -> a -> a
def maxC(x,y):
	return y if (x <= y) else x
	
# GENERIC ----------------------------------------------------------------------

# MAIN FUNCTION INVOCATION
main()
```

