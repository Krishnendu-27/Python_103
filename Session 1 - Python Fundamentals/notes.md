# Why Python popular?

## 1. Philosophy

Python is often considered one of the easiest languages to learn. Its syntax is clear, concise, and highly readable, resembling everyday English. This makes it beginner-friendly and suitable for developers at all levels.

---

## 2. Batteries Included

Python comes with a robust standard library, which means it provides built-in data types, operators, and functions. This "batteries-included" philosophy makes it easy to perform common tasks without the need for additional tools or complicated setup.

---

## 3. General Purpose

Python supports multiple programming paradigms:
- **Object-Oriented Programming (OOP)**
- **Procedural Programming**
- **Functional Programming**

This flexibility allows Python to be used for various applications, including:
- **Desktop software**
- **Data Science**
- **Game development**
  
Its versatility makes it an excellent choice for almost any project.

---

## 4. Vibrant Community

Python has a vast and active community. This results in continuous growth, rich libraries, frameworks, and resources for learning and development. Whether you're a beginner or an expert, there's always support available.

---

# Why Python for Data Science?

## 1. Easy to Learn

Python's simple syntax and readability make it one of the most popular languages for beginners and professionals alike. It's particularly appealing to data scientists who want to focus more on solving problems than on learning complex language syntax.

---

## 2. Proximity to Mathematics

Python is widely used in data science because it supports a range of powerful mathematical libraries, such as **NumPy**, **SciPy**, and **Pandas**. These libraries allow for seamless mathematical computations, data manipulation, and analysis. Python is, therefore, an ideal language for anyone working with data, from statistics to machine learning.

### 📤 Output \& `print()` Function

- **`print` is a function**, and Python is **case-sensitive**: `A` and `a` are different.
- Use **commas** to print multiple, different-type values:

```python
print("halo", 1, 5.5, True)
```

- Use **`sep`** to specify a custom separator:

```python
print("halo", 1, 5.5, True, sep="/")
```


***

### 🧮 Data Types

| Type | Example | Notes |
| :-- | :-- | :-- |
| **Integer** | `1`, `42` | Up to ~1×10³⁰⁸ |
| **Float** | `5.5`, `1.7e308` | Up to ~1.7×10³⁰⁸ |
| **Boolean** | `True`, `False` |  |
| **String** | `"hello"` |  |
| **Complex** | `5+6j` |  |
| **List** | `[1, 3, 4, 5]` | Mutable sequence |
| **Tuple** | `(1, 2, 3, 4, 5)` | Immutable sequence |
| **Set** | `{1, 2, 3, 4, 5}` | Unordered, unique elements |
| **Dict** | `{'name':'krish','age':5}` | Key–value pairs |

```python
print(type(5.6))  # <class 'float'>
```


***

### 🏷️ Variables

- Python variables are **dynamically typed**—no type declaration needed.
- A variable can hold **any** type, e.g.:

```python
num = 50
num = True
```

- Multiple assignment:

```python
a, b, c = 1, 2, 3
a = b = c = 5
```


***

### 🔑 Keywords \& Identifiers

- **Keywords** are *reserved words* (32 in Python) and cannot be used as variable names.
- **Identifiers** are names you choose for variables, functions, classes, etc.

***

### 📥 User Input

- Use `input()` to read from the console:

```python
name = input("Enter your name: ")
```

- **Type conversion**: `input()` returns a string, so convert when needed:

```python
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
total = num1 + num2
print(total)
```

- **Explicit conversion** is manual (e.g., `int(a)`), **implicit** is automatic by Python.

***

### 🔢 Literals / Values

#### Integer Literals

```python
decimal_num = 10
binary_literal = 0b1010
octal_literal = 0o12
hex_literal = 0xA
```


#### Float Literals

```python
float_1 = 10.5
float_2 = 1.5e3   # 1.5 × 10³
float_3 = 1.5e-3  # 1.5 × 10⁻³
```


#### Complex Literals

```python
x = 3.14 + 9j
print(x, x.real, x.imag)
```


#### String Literals

```python
a = 'Hello'                  # Single-quoted
b = "Python"                 # Double-quoted
c = '''This is               # Triple-quoted
a multi-line string'''
d = r"C:\Users\Python"       # Raw string
symbol = "\u00A9"            # Unicode ©
raw_str = r"raw \n bro"
```


#### Boolean Arithmetic

```python
print(True + 4)   # 5   (True == 1)
print(False + 4)  # 4   (False == 0)
```


#### `None` (Null Value)

```python
z = None
print(z)
```
