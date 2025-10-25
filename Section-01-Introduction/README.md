### 1. Functions & Basic I/O

- **All output** in Python is done via functions—most commonly `print()`.
- **Function call syntax:**

  ```python
  print("halo")
  ```

- **Inspecting the interpreter:**

  ```python
  import sys
  print(sys.version)  # e.g. "3.11.4"
  ```

- Anything inside `()` after a name is a **function call**. You can define many of your own functions.

---

### 2. Classes & Objects

- A **class** is like a **factory** or blueprint that defines a new data type, encapsulating **properties** (attributes) and **methods** (functions).

- An **object** is an **instance** of a class—a concrete “unit” built from the blueprint.

  ```python
  class Car: 
      def __init__(self, model, year):
          self.model = model      # property
          self.year  = year

      def honk(self):             # method
          print("Beep!")

  my_car = Car("Sedan", 2025)     # object
  my_car.honk()                   # prints "Beep!"
  ```

- The `__init__` method runs when you create a new object, initializing its attributes.

---

### 3. Virtual Environments

- **Why?** Keep each project’s dependencies isolated—different projects can use different library versions without conflict.
- **Create:**

  ```bash
  python3 -m venv .venv
  ```

- **Activate:**

  - **Bash / Zsh:**

    ```bash
    source .venv/bin/activate
    ```

  - **Fish shell:**

    ```fish
    . .venv/bin/activate.fish
    ```

- **Deactivate:**

  ```bash
  deactivate
  ```

- **Requirements file:** List your dependencies and versions in `requirements.txt` so teammates can install them all at once:

  ```
  flask==2.3.2
  requests>=2.30.0
  ```

---

### 4. Modules & Packages

- Any **`.py` file** is a **module**. You import it to reuse its functions, classes, and variables.
- A **package** is a folder containing modules **plus** an `__init__.py` file (which may be empty).

  ```text
  my_project/
  ├─ utils/
  │  ├─ __init__.py
  │  ├─ file_ops.py
  │  └─ network.py
  └─ main.py
  ```

- Importing:

  ```python
  from utils.file_ops import read_file
  from utils import network
  ```

---

### 5. Code Style: PEP 8 & Readability

- **PEP 8** is the official style guide for Python code. Key rules include:

  - **4‑space indents**, no tabs
  - **`snake_case`** for functions and variables
  - **`PascalCase`** for class names
  - Limit lines to **79 characters**
  - Leave **two blank lines** between top‑level definitions

- Consistent style makes code **portable**, **readable**, and **maintainable**.

---

### 6. The Zen of Python

Python’s guiding principles, by Tim Peters—invoke with `import this`:

