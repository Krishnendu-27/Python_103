# 🐍 Python Strings: Complete Mastery Guide

> **Master the art of working with text in Python**

---

## 📖 Table of Contents

1. [What are Strings?](#what-are-strings)
2. [Creating Strings](#creating-strings)
3. [String Indexing](#string-indexing)
4. [String Slicing](#string-slicing)
5. [Operations on Strings](#operations-on-strings)
6. [String Methods](#string-methods)
7. [Loop Control & Strings](#loop-control--strings)
8. [Formatting Strings](#formatting-strings)
9. [Quick Reference](#quick-reference)

---

## 🔤 What are Strings?

Strings are **sequences of Unicode characters** that represent text. They're one of the most important data types in Python.

### Key Characteristics

- ✅ **Immutable**: Cannot be changed after creation
- ✅ **Ordered**: Each character has a specific position (index)
- ✅ **Iterable**: Can loop through each character
- ✅ **Unicode**: Supports all languages and emojis 🌍

### ASCII vs Unicode

| Encoding | Bits | Coverage | Use |
|----------|------|----------|-----|
| **ASCII** | 8 bits | 128 characters (English) | Legacy systems |
| **Unicode** | 16+ bits | 1M+ characters (All languages) | Modern Python 3 |

---

## 📝 Creating Strings

### Multiple Ways to Create

```python
# Single quotes
greeting = 'Hello'

# Double quotes
message = "Welcome to Python"

# Triple quotes (multiline strings)
poem = """Roses are red
Violets are blue
Python is awesome
And so are you"""

# Using str() constructor
number_string = str(42)          # "42"
pi_string = str(3.14159)         # "3.14159"
```

### Why Multiple Quote Types?

```python
# Avoid escaping quotes
sentence1 = "I'm learning Python"      # No escape needed
sentence2 = 'He said "Hello"'          # No escape needed

# Use escaping if necessary
sentence3 = "I\'m learning Python"     # With escape
```

---

## 📍 String Indexing

Python assigns each character an **index** starting from **0**.

### Positive Indexing (Left → Right)

```python
name = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5

print(name[0])       # P
print(name[2])       # t
print(name[5])       # n
```

### Negative Indexing (Right ← Left)

```python
name = "Python"
#       P  y  t  h  o  n
#      -6 -5 -4 -3 -2 -1

print(name[-1])      # n (last character)
print(name[-2])      # o
print(name[-6])      # P (first character)
```

### Visual Map

```
String: "PYTHON"
Forward:  0 1 2 3 4 5
          P Y T H O N
Backward: -6-5-4-3-2-1
```

---

## ✂️ String Slicing

Extract portions of a string using **range notation**: `string[start:end:step]`

### Basic Slicing

```python
text = "Hello World"

print(text[0:5])     # Hello (from 0 to 4, end excluded)
print(text[6:])      # World (from 6 to end)
print(text[:5])      # Hello (from start to 4)
print(text[6:11])    # World (from 6 to 10)
```

### Slicing with Step

```python
text = "Python Programming"

print(text[::2])     # Pto rgamn (every 2nd character)
print(text[1::2])    # yhn ormig (every 2nd, starting at 1)
print(text[::3])     # Pog rm (every 3rd character)
```

### Reversing Strings

```python
text = "Hello"

print(text[::-1])    # olleH (entire string reversed)
print(text[4:0:-1])  # olleH (from index 4 to 1, reversed)
```

---

## 🔧 Operations on Strings

### ➕ Concatenation

```python
first = "Hello"
second = "World"

result = first + " " + second
print(result)        # Hello World
```

### ➕ Repetition

```python
word = "Ha"
print(word * 3)      # HaHaHa
```

### ⚖️ Comparison

```python
# Equality
print("apple" == "apple")       # True
print("apple" == "orange")      # False

# Lexicographic comparison (dictionary order)
print("apple" < "banana")       # True (a comes before b)
print("Zebra" < "apple")        # True (Z has lower ASCII than a)
```

### 🔍 Membership

```python
text = "Hello World"

# Check if substring exists
print("World" in text)          # True
print("Python" in text)         # False

# Check if substring doesn't exist
print("World" not in text)      # False
```

### 🎯 Logical Operations

```python
# AND: Returns first falsy or last value
print("hello" and "world")      # world
print("hello" and "")           # (empty string)

# OR: Returns first truthy or last value
print("hello" or "world")       # hello
print("" or "world")            # world

# NOT: Inverts boolean
print(not "hello")              # False
print(not "")                   # True
```

---

## 🛠️ String Methods

### 🔤 Case Conversion

```python
text = "Hello Python World"

print(text.lower())             # hello python world
print(text.upper())             # HELLO PYTHON WORLD
print(text.capitalize())        # Hello python world
print(text.title())             # Hello Python World
print(text.swapcase())          # hELLO pYTHON wORLD
```

### 🔎 Searching

```python
text = "Hello World Hello"

# Find first occurrence
print(text.find("Hello"))       # 0
print(text.find("World"))       # 6
print(text.find("Python"))      # -1 (not found)

# Index (raises error if not found)
print(text.index("World"))      # 6

# Count occurrences
print(text.count("Hello"))      # 2
print(text.count("l"))          # 3
```

### ✅ Checking Types

```python
print("12345".isdigit())        # True
print("Hello".isalpha())        # True
print("Hello123".isalnum())     # True
print("hello_world".isidentifier())  # True
print("   ".isspace())          # True
```

### ✂️ Splitting & Joining

```python
# Split into list
sentence = "I love Python programming"
words = sentence.split()        # ['I', 'love', 'Python', 'programming']

# Split by specific character
csv = "apple,banana,orange"
fruits = csv.split(",")         # ['apple', 'banana', 'orange']

# Join list into string
result = " ".join(words)        # I love Python programming
dash_result = "-".join(words)   # I-love-Python-programming
```

### 🔄 Replace

```python
text = "I love Java"

new_text = text.replace("Java", "Python")
print(new_text)                 # I love Python

# Replace only first N occurrences
text2 = "hello hello hello"
result = text2.replace("hello", "hi", 2)
print(result)                   # hi hi hello
```

### 🧹 Stripping Whitespace

```python
text = "  Hello World  "

print(text.strip())             # Hello World (both ends)
print(text.lstrip())            # Hello World   (left only)
print(text.rstrip())            #   Hello World (right only)
```

### ✔️ Starting & Ending

```python
text = "Hello Python World"

print(text.startswith("Hello"))     # True
print(text.startswith("Python"))    # False
print(text.endswith("World"))       # True
print(text.endswith("Python"))      # False
```

---

## 🔁 Loop Control & Strings

### Break Statement

```python
text = "Python"

for char in text:
    if char == "h":
        break           # Exit loop immediately
    print(char)

# Output: P y t
```

### Continue Statement

```python
text = "Python"

for char in text:
    if char == "t":
        continue        # Skip to next iteration
    print(char)

# Output: P y h o n
```

### Pass Statement

```python
text = "Python"

for char in text:
    if char == "t":
        pass            # Do nothing, placeholder
    print(char)

# Output: P y t h o n
```

### Iterating Through Strings

```python
text = "Hello"

# Loop through each character
for char in text:
    print(char)
# Output: H e l l o

# Loop with index
for i, char in enumerate(text):
    print(f"{i}: {char}")
# Output:
# 0: H
# 1: e
# 2: l
# 3: l
# 4: o
```

---

## 🎨 Formatting Strings

### F-Strings (Modern & Recommended)

```python
name = "Alice"
age = 25
score = 95.5

# Basic formatting
print(f"Hello {name}")          # Hello Alice

# Multiple variables
print(f"Name: {name}, Age: {age}")
# Name: Alice, Age: 25

# Expressions in f-strings
print(f"Next year: {age + 1}")   # Next year: 26

# Formatting numbers
print(f"Score: {score:.1f}")    # Score: 95.5
```

### Format Method

```python
template = "Hello {}, you scored {}"
result = template.format("Bob", 98)
print(result)                   # Hello Bob, you scored 98

# Named placeholders
template2 = "Name: {name}, Age: {age}"
result2 = template2.format(name="Charlie", age=30)
print(result2)                  # Name: Charlie, Age: 30
```

### Percent Operator (Legacy)

```python
name = "David"
age = 28

print("Name: %s, Age: %d" % (name, age))
# Name: David, Age: 28
```

---

## ⚠️ Strings are Immutable

```python
text = "Hello"

# ❌ This will cause an error:
# text[0] = "J"  # TypeError: 'str' object does not support item assignment

# ✅ Create a new string instead:
text = "J" + text[1:]
print(text)                     # Jello
```

---

## 📊 Quick Reference Table

| Task | Code | Result |
|------|------|--------|
| **Length** | `len("Hello")` | `5` |
| **Uppercase** | `"hello".upper()` | `"HELLO"` |
| **Lowercase** | `"HELLO".lower()` | `"hello"` |
| **Reverse** | `"Hello"[::-1]` | `"olleH"` |
| **First 3 chars** | `"Hello"[:3]` | `"Hel"` |
| **Last 2 chars** | `"Hello"[-2:]` | `"lo"` |
| **Replace** | `"cat".replace("c", "b")` | `"bat"` |
| **Remove spaces** | `" Hi ".strip()` | `"Hi"` |
| **Split** | `"a b c".split()` | `['a', 'b', 'c']` |
| **Join** | `"-".join(['a','b'])` | `"a-b"` |
| **Find index** | `"hello".find("l")` | `2` |
| **Count** | `"hello".count("l")` | `2` |
| **Starts with** | `"hello".startswith("he")` | `True` |
| **Ends with** | `"hello".endswith("lo")` | `True` |
| **Is digit** | `"123".isdigit()` | `True` |
| **Is alpha** | `"abc".isalpha()` | `True` |

---

## 🎯 Real-World Examples

### Extract Email Parts

```python
email = "user@example.com"

username = email.split("@")[0]      # "user"
domain = email.split("@")[1]        # "example.com"

print(f"User: {username}, Domain: {domain}")
# User: user, Domain: example.com
```

### Clean & Format Data

```python
messy_data = "  PYTHON  PROGRAMMING  "

clean = messy_data.strip().lower()  # "python  programming"
formatted = clean.replace("  ", " ") # "python programming"

print(formatted)
```

### Generate Message

```python
items = ["apple", "banana", "cherry"]
message = f"Fruits: {', '.join(items)}"

print(message)
# Fruits: apple, banana, cherry
```

### Validate Input

```python
user_input = "user123"

if user_input.isalnum():
    print("Valid username")
else:
    print("Contains special characters")
```

---

## ✨ Key Takeaways

| Concept | Key Point |
|---------|-----------|
| **Immutable** | Strings cannot be changed; create new ones |
| **Indexing** | Access characters with `[index]` (0-based) |
| **Slicing** | Extract substrings with `[start:end:step]` |
| **Methods** | Rich library of built-in methods |
| **F-Strings** | Use `f"text {variable}"` for formatting |
| **Unicode** | Full support for all languages & emojis |
| **Operations** | Concatenate, compare, search, and manipulate |

---

## 🚀 Next Steps

- Practice string manipulation daily
- Explore built-in methods with `dir(str)`
- Build text processing projects
- Master regex for advanced pattern matching

---

**Happy Coding! 🎉**-
