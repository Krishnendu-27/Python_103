# 📋 Python Lists: Complete Mastery Guide

> **Master dynamic arrays and unlock list superpowers**

---

## 📖 Table of Contents

1. [What are Lists?](#what-are-lists)
2. [How Lists Store in Memory](#how-lists-store-in-memory)
3. [Creating Lists](#creating-lists)
4. [Accessing Items](#accessing-items)
5. [Modifying Lists](#modifying-lists)
6. [Operations on Lists](#operations-on-lists)
7. [List Functions](#list-functions)
8. [List Comprehension](#list-comprehension)
9. [Advanced Topics](#advanced-topics)
10. [Arrays vs Lists](#arrays-vs-lists)
11. [Key Takeaways](#key-takeaways)

---

## 🔤 What are Lists?

A **list** is a data type where you can store **multiple items** under **one name**. It's a **dynamic array** that can grow or shrink on the fly.

### 💡 Core Concept

```python
listexample = [5, 1, 2, 3, "hallo", ["word", 50]]
print(listexample)
# Output: [5, 1, 2, 3, 'hallo', ['word', 50]]
```

### 🎯 Characteristics of Lists

| Feature | Description |
|---------|-------------|
| **Ordered** | Items have a specific order/index |
| **Mutable** | Can be changed after creation |
| **Heterogeneous** | Can store different data types |
| **Duplicates** | Can contain duplicate values |
| **Dynamic** | Can grow or shrink at runtime |
| **Nestable** | Can contain other lists inside |
| **Accessible** | Can access items by index |
| **Object Container** | Can store any Python object |

---

## 💾 How Lists Store in Memory

### 🔍 Memory Address Concept

```python
print(id(5))                    # Memory address of 5
print(id(listexample[0]))       # Memory address of first element
# Both return the same address if referring to same value
```

### 🎯 Referential Array (How Python Works)

Python lists use **Referential Arrays** — they store **addresses**, not values directly:

```
List: [1, 2, 3]

Memory Layout:
┌──────────────────┐
│  1 (at 500)      │
│  2 (at 690)      │
│  3 (at 420)      │
└──────────────────┘

List Object Stores:
[500, 690, 420]  ← Addresses, not actual values!
```

### 📊 Dynamic Array Behavior

When you add items beyond capacity, Python:
1. Creates a **new, larger list** internally
2. **Copies** all previous values
3. **Adds** the new value
4. **Replaces** the old list reference

```python
a = [1, 2, 3]       # Initial list
a.append(4)         # Internally: create new list, copy [1,2,3], add 4
```

---

## 📝 Creating Lists

### Basic Creation

```python
# Empty list
empty = []

# 1D list (single dimension)
list_1d = [1, 2, 3]

# Heterogeneous list (mixed types)
mixed = [5, "hi", 6.5, True, None]

# Type conversion
from_string = list("krish")     # ['k', 'r', 'i', 's', 'h']
```

### Multidimensional Lists

```python
# 2D list (matrix)
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 3D list (nested matrices)
list_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Mixed nesting
mixed_nested = [1, [1, 2, 3], 2, [4, 5, 6], 3, [7, 8, 9]]
```

---

## 📍 Accessing Items

### Positive Indexing (Left → Right)

```python
L = [1, 2, 3, [5, 6]]

print(L[0])         # 1 (first element)
print(L[2])         # 3 (third element)
```

### Negative Indexing (Right ← Left)

```python
L = [1, 2, 3, [5, 6]]

print(L[-1])        # [5, 6] (last element)
print(L[-2])        # 3 (second from last)
```

### 2D List Access

```python
L = [1, 2, 3, [5, 6]]

print(L[3])         # [5, 6] (access nested list)
print(L[3][0])      # 5 (access first element of nested list)
print(L[3][1])      # 6 (access second element)
```

### Slicing

```python
L = [1, 2, 3, [5, 6]]

print(L[0::2])      # [1, 3] (every 2nd element)
print(L[1:3])       # [2, 3] (from index 1 to 2)
```

---

## 🔧 Modifying Lists

### Adding Items

#### **append()** — Add single item at end

```python
a = [1, 2, 3]
a.append(5)
print(a)            # [1, 2, 3, 5]
```

#### **extend()** — Add multiple items

```python
a = [1, 2, 3]
b = [11, 55, 99]
a.extend(b)
print(a)            # [1, 2, 3, 11, 55, 99]

# ⚠️ String gets added character by character
a.extend("delhi")   # Adds: 'd', 'e', 'l', 'h', 'i'
```

#### **insert()** — Add item at specific position

```python
L = [1, 2, 3, 4, 5]
L.insert(1, 44)
print(L)            # [1, 44, 2, 3, 4, 5]
```

### Changing Values

```python
L = [1, 2, 3, 4, 5]

# Change by index
L[-1] = 5252
print(L)            # [1, 2, 3, 4, 5252]

# Change by slicing
L[1:3] = [99, 96, 100]
print(L)            # [1, 99, 96, 100, 4, 5252]
```

### Deleting Items

#### **del** — Delete by index or slice

```python
L = [1, 2, 3, 4, 5]

del L[-1]           # Delete last element
del L[1:3]          # Delete from index 1 to 2
print(L)            # [1, 5]
```

#### **remove()** — Remove by value

```python
L = [1, 2, 3, 4, 5]
L.remove(5)         # Remove value 5
print(L)            # [1, 2, 3, 4]
```

#### **pop()** — Remove last item (or by index)

```python
L = [1, 2, 3, 4, 5]
L.pop()             # Remove last item
print(L)            # [1, 2, 3, 4]

L.pop(1)            # Remove item at index 1
print(L)            # [1, 3, 4]
```

#### **clear()** — Remove all items

```python
L = [1, 2, 3, 4, 5]
L.clear()
print(L)            # []
```

---

## 🔧 Operations on Lists

### ➕ Concatenation

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2        # Combine lists
print(l3)           # [1, 2, 3, 4, 5, 6]
```

### ➕ Repetition

```python
l1 = [1, 2, 3]
l4 = l1 * 3         # Repeat 3 times
print(l4)           # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 🔍 Membership

```python
l2 = [4, 5, 6, 4, 5]

print(6 in l2)      # True
print(10 in l2)     # False
```

### 🔁 Looping

```python
l3 = [1, 2, 3, 4, 5, 6]

for i in l3:
    print(i * 2)
# Output: 2, 4, 6, 8, 10, 12
```

---

## 🛠️ List Functions

### Length, Max, Min

```python
L = [1, 2, 3, 4, 5, 6]

print(len(L))       # 6
print(max(L))       # 6
print(min(L))       # 1
```

### Count Occurrences

```python
L = [1, 2, 3, 4, 5, 5, 5]

print(L.count(5))   # 3 (appears 3 times)
```

### Sort (Permanent)

```python
L = [2, 1, 5, 7, 0]

L.sort()            # Permanently sorts in-place
print(L)            # [0, 1, 2, 5, 7]
```

### Sorted (Non-Permanent)

```python
L = [2, 1, 5, 7, 0]

print(sorted(L))    # [0, 1, 2, 5, 7]
print(L)            # [2, 1, 5, 7, 0] (unchanged)

print(sorted(L, reverse=True))  # [7, 5, 2, 1, 0]
```

### Reverse (Permanent)

```python
L = [1, 2, 3, 4, 5]

L.reverse()         # Permanently reverses
print(L)            # [5, 4, 3, 2, 1]
```

---

## 🎨 List Comprehension

**Syntax**: `newlist = [expression for item in iterable if condition == True]`

### Basic Comprehension

```python
numbers = [1, 2, 3, 4]

# Square each number
squares = [n * n for n in numbers]
print(squares)      # [1, 4, 9, 16]
```

### With Condition

```python
numbers = [1, 2, 3, 4]

# Get only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)        # [2, 4]
```

### String Operations

```python
fruits = ["apple", "banana", "cherry"]

# Convert to uppercase
upper_fruits = [f.upper() for f in fruits]
print(upper_fruits) # ['APPLE', 'BANANA', 'CHERRY']
```

### Multiple Conditions

```python
basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]

# Items in my_fruits that exist in basket AND start with 'a'
ex = [i for i in my_fruits if i in basket if i.startswith("a")]
print(ex)           # ['apple']
```

### Nested List Comprehension

```python
# Create 3x3 multiplication table
matrix = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### 🎯 Advantages of List Comprehension

| Advantage | Description |
|-----------|-------------|
| **Time Efficient** | Faster than loops |
| **Space Efficient** | Less memory |
| **Concise** | Fewer lines of code |
| **Readable** | More Pythonic |

---

## 🔀 Zip Function

The **zip()** function pairs elements from multiple iterables:

```python
L1 = [1, 2, 3]
L2 = [-1, -2, -3]

result = list(zip(L1, L2))
print(result)       # [(1, -1), (2, -2), (3, -3)]
```

### 📌 Important: Different Lengths

```python
L1 = [1, 2, 3, 4]
L2 = ['a', 'b']

result = list(zip(L1, L2))
print(result)       # [(1, 'a'), (2, 'b')] 
# Stops at shortest list!
```

---

## ⚠️ Common Pitfalls

### Reference vs Copy

```python
a = [1, 2, 3]
b = a               # b references same list as a

a.append(4)
print(b)            # [1, 2, 3, 4] (b changed too!)

# ✅ Solution: Use copy()
c = a.copy()        # c is independent copy
a.append(5)
print(c)            # [1, 2, 3, 4] (unchanged)
```

### Mutability

```python
# Lists are MUTABLE (can change)
L = [1, 2, 3]
L[0] = 99
print(L)            # [99, 2, 3]

# ✅ This is why copy() is important
```

### Memory Overhead

Lists consume **more memory** than arrays because:
- Store **addresses**, not values
- Each element is a **Python object**

---

## 📊 Arrays vs Lists

| Aspect | Arrays | Lists |
|--------|--------|-------|
| **Size** | Fixed | Dynamic |
| **Data Type** | Same (homogeneous) | Different (heterogeneous) |
| **Speed** | Faster | Slower |
| **Memory** | Less | More |
| **Flexibility** | Less | More |
| **Use Case** | Numerical computing | General purpose |

### 🎯 Memory Storage

**Arrays**: Contiguous memory blocks
```
[1, 2, 3] → All at 500, 504, 508 (sequential)
```

**Lists**: References to scattered memory
```
[1, 2, 3] → Pointers at [500, 690, 420]
```

---

## 🔄 Objects in Lists

Python can store **any object** in lists:

```python
L = [1, 2, print, type, [1, 2, 3]]
print(L)
# [1, 2, <built-in function print>, <class 'type'>, [1, 2, 3]]
```

---

## ⚠️ Disadvantages of Python Lists

| Disadvantage | Impact |
|--------------|--------|
| **Slow** | Not ideal for large numerical operations |
| **Memory Overhead** | Stores references, not values |
| **Mutable Risk** | Easy to accidentally modify |
| **Type Flexibility** | Can cause type errors if not careful |

---

## ✨ Key Takeaways

| Concept | Summary |
|---------|---------|
| **Definition** | Dynamic array storing multiple items |
| **Memory** | Referential array storing addresses |
| **Mutable** | Can be changed after creation |
| **Heterogeneous** | Can store different data types |
| **Dynamic** | Grows/shrinks automatically |
| **Indexing** | 0-based, supports negative indices |
| **Slicing** | Extract portions with `[start:end:step]` |
| **Comprehension** | Concise way to create filtered/transformed lists |
| **Operations** | Support +, *, in, iteration |

---

## 🚀 Quick Comparison: List Methods

| Method | Effect | Permanent? |
|--------|--------|-----------|
| `append()` | Add one item | ✅ Yes |
| `extend()` | Add multiple items | ✅ Yes |
| `insert()` | Insert at position | ✅ Yes |
| `remove()` | Remove by value | ✅ Yes |
| `pop()` | Remove by index | ✅ Yes |
| `sort()` | Sort in-place | ✅ Yes |
| `sorted()` | Sort (return new) | ❌ No |
| `reverse()` | Reverse in-place | ✅ Yes |
| `copy()` | Create independent copy | ✅ Yes |
| `clear()` | Remove all items | ✅ Yes |

---

**Happy Coding! 🎉**
