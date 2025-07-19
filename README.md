
---

##  `README.md` — Python Basics: Functions, Modules, Packages, Environments, and Testing

* Functions
* Modules & importing them
* Built-in modules
* Packages & importing them
* Creating virtual environments
* Creating and using `requirements.txt`
* Manual and `unittest`-based testing

````markdown
#  Python Project: From Basics to Testing

This project walks you through the **foundational concepts** of Python development including:

- Writing reusable **functions**
- Organizing code with **modules** and **packages**
- Using **built-in modules** like `math`, `random`, `time`
- Creating and activating a **virtual environment**
- Generating a `requirements.txt` file
- Performing **manual and unit testing**

---

##  1. Functions

A **function** is a reusable block of code.

```python
# math_utils.py
def add(a, b):
    return a + b
````

>  You can now use `add()` in other files by importing it.

---

##  2. Modules

A **module** is any `.py` file that contains functions, variables, or classes.

**Example:**

```python
# main.py
import math_utils  # our custom module

print(math_utils.add(3, 5))  # Output: 8
```

> Use `import module_name` to access your functions.

---

##  3. Built-in Modules

Python comes with many built-in modules like `math`, `random`, `time`.

```python
import math
import random
import time

print(math.sqrt(25))        # 5.0
print(random.randint(1, 10))  # Random number
time.sleep(2)               # Pause execution for 2 seconds
```

---

##  4. Packages

A **package** is a folder that contains multiple modules and an `__init__.py` file.

 Example structure:

```
myproject/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── mathops.py
    └── textops.py
```

**mypackage/mathops.py**

```python
def square(n):
    return n * n
```

**mypackage/**init**.py**

```python
from .mathops import square
```

**main.py**

```python
from mypackage import square

print(square(4))  # Output: 16
```

---

##  5. Virtual Environment

Use a virtual environment to **isolate your project’s packages**.

```bash
# Create virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

---

##  6. Installing and Freezing Requirements

Install any packages (e.g., `requests`, `numpy`):

```bash
pip install requests numpy
```

Create a `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```

Install all dependencies later via:

```bash
pip install -r requirements.txt
```

---

##  7. Manual Testing

Manual testing means **calling functions directly** and checking the result.

```python
from math_utils import add

print(add(2, 3))  # Should print 5
```

---

##  8. Unit Testing with `unittest`

Create a test file like `test_math_utils.py`:

```python
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

Run the test with:

```bash
python test_math_utils.py
```

 Output:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

##  Summary

| Topic               | Command/Example                          |
| ------------------- | ---------------------------------------- |
| Create virtual env  | `python -m venv venv`                    |
| Activate env        | `source venv/bin/activate` or `venv\...` |
| Install package     | `pip install requests`                   |
| Freeze requirements | `pip freeze > requirements.txt`          |
| Install from file   | `pip install -r requirements.txt`        |
| Run tests           | `python test_file.py`                    |

---
