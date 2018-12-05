# Python Lab

Some math and programming experiments.

## Solving common Python issues

### Unindent does not match indentation level

**Windows**: Hit `Ctrl+Shift+P` to open Command Palette. Select `Convert Spaces to Tabs`

## Useful Info

**Running code in Atom**

- Save file with `.py` extension.
- Hit `Ctrl+Shift+B` to run code.

### How to writing a simple Python script

Paste this code in Atom (or another text editor). 

Template:

```python
import functools
import itertools

# main :: IO ()
def main():
	## MAIN CODE GOES HERE
	
	
# GENERIC FUNCTIONS ----------------------------------------------------------------------
## FUNCTIONS GO HERE

main()
```

### Code samples

**Calculate vector norm**
```python
import functools

# main :: IO ()
def main():
	xs = [1,2,3]
	print(foldl(lambda acc, x: acc + x * x, 0, xs))
	
# GENERIC ----------------------------------------------------------------------
# PY - Prelude

# foldl :: (a -> b -> a) -> a -> [b] -> a
def foldl(f, a, xs):
	return functools.reduce(f, xs, a);

main()
```

**Square each vector entry**
```python

import functools

# main :: IO ()
def main():
	xs = [1,2,3]
	ys = map(lambda x: x*2, xs)
	print(ys)
	
# GENERIC ----------------------------------------------------------------------

main()
```
