# Summary 22-12-2018 Class

## Review

Use single quotes for strings.
Logical operators and, or, not.

## Basic Concepts

### Python Conditionals

_Conditional statements_

```python
if (P(x)):
    # execute this statement
else:
    # execute this statement
```

_Conditional expressions_

```python
A if P(x) else B
```

- Why conditional expressions are preferred

	- They return a value

	- Don't break functional composition

### Python supports the usual logical conditions from mathematics

- Equals: a == b

- Not Equals: a != b

- Less than: a \< b

- Less than or equal to: a \<= b

- Greater than: a \> b

- Greater than or equal to: a \>= b

### Logical operators

- and

- or

- not

### Difference with = in Haskel and Python (equational reasoning)

An equation x = y says that x and y have the same value; any time you see one of them you can replace it by the other. Such a replacement is called a substitution. For example, suppose we are given the following definitions, which are written as equations:
x=8 y=4
These equations are going to be cited as justifications for reasoning steps, so it helps to have a standard way to name equations. The notation { x } means “the equation that defines x”. Now, suppose the problem is to evaluate 2 ∗ x + x/y. We do this by writing a chain of expressions, each one equal to the previous, beginning with the original problem and ending with the final result. Each step is justified by a reason given in braces { . . . }.[^1]
 
```
2*x + x/y
= 2*8 + 8/y       { x }
= 2*8 + 8/4       { y }
```

- Equal sign '=' in some functional languages are used for equations

- Equal sign in some imperative languages is used for assignment.

### Function definitions and lambda expressions

- All functions in Python (not just lambda functions) can be passed around.

- When to use lambda expressions

	- For one-liners in higher order functions

### How to read type signatures like domains notation

- f :: Int -\> Int

	- A function that takes something of type Int and returns something of type Int.

- f :: (Int -\> String) -\> Int

	- A function that takes a function and a String. Return something of type int

### Higher Order Functions
It fulfills this definitions if:

_It takes a function as an argument or returns a function_
Map invocation
`map(f, xs)`

In mathematics, we define a function as:

```
f(x) = x * x
```

In python, we are passing `f` as a name, similar to the composition of functions:

![Compose f with g](https://github.com/gabriels23/Python-Lab/blob/master/Classes/compose.jpeg?raw=true)


### Tip

- Think in terms of values instead of sequences of actions

## List Comprehensions

```python
import functools
import itertools

# main :: IO ()
def main():
	# LIST COMPREHENSIONS
	# {0,1}^3 Cartesian product
	A = [0,1]
	xs = [(x,y,z) for x in A for y in A for z in A]

	# {k^2 | k e B and k^2 < 101}
	B = [1,2,3,4,5,6,7,8,9,10,11]
	ys = [k*k for k in B if k*k < 101]

	# Print to the screen
	print(xs)
	print(ys)
	
# GENERIC ----------------------------------------------------------------------

main()
```

[^1]:	Discrete Mathematics Using a Computer
