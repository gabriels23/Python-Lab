# Importing Minimum Rank library into Jupyter Notebook

## What's a Python Module?

## How to import a folder with **.py** files?

A structure like this:
  - Folder
    - **\_\_init\_\_.py** [1]
    - file1.py
    - file2.py

Is imported into Jupyter with the following statements [2]

```py
import Folder
```

### __init.py__ contents
import Folder.file1


To access the required function, `.` syntax should be used, as in:

```py
Folder.file1.function1
```

[1]: Into **__init__.py**, it's necesarry to import required modules.

[2]: Provided **$PYTHONPATH** enviromental variable is correctly set.
