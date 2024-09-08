# python downloading dependences

## Creating virtual environments

```bash
python -m vrnv .venv
.\.venv\Scripts\activate
pip install <package_name>
pip freeze > requirements.txt
```

* getting packages downloaded from requirements file

`pip install -r requirements.txt`

### Step 1: Set up the Project Directory

```bash
my_project/
â”œâ”€â”€ src/
â”‚   â””â”€â”€ my_package/
â”‚       â”œâ”€â”€ __init__.py
â”‚       â”œâ”€â”€ module1.py
â”‚       â””â”€â”€ module2.py
â”œâ”€â”€ tests/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ test_module1.py
â”‚   â””â”€â”€ test_module2.py
â”œâ”€â”€ .coveragerc
â”œâ”€â”€ requirements.txt
â””â”€â”€ pytest.ini
```

### Step 2: Organize Source Code (src/)

```bash
my_project/
â”œâ”€â”€ src/
â”‚   â””â”€â”€ my_package/
â”‚       â”œâ”€â”€ __init__.py
â”‚       â”œâ”€â”€ module1.py
â”‚       â””â”€â”€ module2.py
```

### Step 3: Organize Tests (tests/)

```bash
my_project/
â”œâ”€â”€ tests/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ test_module1.py
â”‚   â””â”€â”€ test_module2.py
```

### Step 4: Set Up Pytest Configuration (pytest.ini)

```bash
[pytest]
addopts = --cov=src/my_package --cov-report=term-missing
testpaths = tests
```

### Step 5: Add Coverage Configuration (.coveragerc)

```bash
[run]
source = src/my_package
branch = True

[report]
exclude_lines =
    if __name__ == '__main__':
```

### Step 6: Add Dependencies (requirements.txt)

Add pytest, pytest-cov, and any other dependencies to a requirements.txt file for easy installation.

Example requirements.txt:

```bash
pytest
pytest-cov
```

### Step 7: Write Source Code and Tests

#### Source Code

```bash
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

#### Test Code

```bash
from src.my_package.module1 import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
```

### Step 8: Running Tests with Coverage

```bash
pytest
```

### Step 9: Review Coverage Report

```bash
pytest --cov=src/my_package --cov-report=html
```

[ReferHere](https://github.com/asquarezone/khajaclassroom/commit/cab8b37a9e945bae563aaee43aeb0603c5f1953e) For Sample code.

### Type hinting

```python
def is_prime(number:int)-> bool:
```
 