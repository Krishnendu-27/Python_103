# 📦 Python Collections: Tuples, Sets & Dictionaries

> **Master immutable and unordered data structures**

---

## 📖 Table of Contents

1. [Tuples](#tuples)
2. [Sets](#sets)
3. [Dictionaries](#dictionaries)
4. [Comparison Table](#comparison-table)
5. [Key Takeaways](#key-takeaways)

---

## 🔒 Tuples

### 🎯 What is a Tuple?

A **tuple** is an **immutable list** — once created, it cannot be changed. It's similar to a list but read-only.

### 📋 Characteristics

| Feature | Details |
|---------|---------|
| **Ordered** | Items have specific positions |
| **Immutable** | Cannot change after creation |
| **Allows Duplicates** | Can contain duplicate values |
| **Indexable** | Access by index and slicing |
| **Faster** | More efficient than lists |
| **Memory** | Uses less memory than lists |

---

### 📝 Creating Tuples

#### Basic Creation

```python
# Empty tuple
t1 = ()

# Single item (IMPORTANT: needs comma!)
t2 = (3,)       # ✅ Correct
t2_wrong = (3)  # ❌ Wrong - just an integer!

# Multiple items
t3 = (1, 2, 3)

# Heterogeneous tuple
t4 = (5, 99, "hello", 63.6)

# Nested tuple
t5 = (1, (1, 2), 3, (5, 4))

# Using tuple() constructor
t6 = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

### 📍 Accessing Items

```python
t = (1, 2, 3, [5, 6])

# Positive indexing
print(t[0])         # 1
print(t[2])         # 3

# Negative indexing
print(t[-1])        # [5, 6]

# Slicing
print(t[0::2])      # (1, 3)

# Nested access
print(t[3][1])      # 6
```

### ❌ Cannot Modify Tuples

```python
t = (1, 2, 3)

# ❌ All these will raise errors:
# t[0] = 99              # Cannot change
# t.append(4)            # No append method
# t.extend([4, 5])       # No extend method
# t.remove(3)            # No remove method
```

### 🗑️ Deleting Tuples

```python
t = (1, 2, 3)

# Can only delete the entire tuple
del t
# print(t)  # ❌ NameError - t no longer exists

# ⚠️ Cannot delete individual elements
```

---

### 🔧 Operations on Tuples

#### Concatenation & Repetition

```python
t1 = (1, 4, 7, 8, 9)
t2 = (7, 8, 9, 6, 3)

print(t1 + t2)      # (1, 4, 7, 8, 9, 7, 8, 9, 6, 3)
print(t2 * 2)       # (7, 8, 9, 6, 3, 7, 8, 9, 6, 3)
```

#### Membership & Iteration

```python
t = (5, 10, 15, 20)

print(5 in t)       # True

for i in t:
    print(i * 2)
# Output: 10, 20, 30, 40
```

### 🛠️ Tuple Functions

```python
t = (1, 4, 5, 6, 3, 2, 7, 8, 9, 10)

print(len(t))       # 10
print(max(t))       # 10
print(min(t))       # 1
print(sorted(t))    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(t.index(6))   # 3 (index of value 6)
print(t.count(3))   # 1 (appears 1 time)
```

---

### ⚡ Tuple Unpacking

Extract tuple elements into variables:

```python
a, b, c = (1, 2, 3)
print(a, b, c)      # 1 2 3

# With zip
zip1 = (1, 2, 3)
zip2 = (7, 8, 9)
z = zip(zip1, zip2)
print(list(z))      # [(1, 7), (2, 8), (3, 9)]
```

---

### 📊 Tuples vs Lists Speed

```python
import time

L = list(range(10000))
T = tuple(range(10000))

# Time list iteration
start = time.time()
for i in L:
    i * 5
print("List time:", time.time() - start)    # Slower

# Time tuple iteration
start = time.time()
for i in T:
    i * 5
print("Tuple time:", time.time() - start)   # Faster ⚡
```

### 💾 Memory Comparison

```python
import sys

L = list(range(10000))
T = tuple(range(10000))

print("List size:", sys.getsizeof(L))       # More memory
print("Tuple size:", sys.getsizeof(T))      # Less memory ⚡
```

---

## 🎯 Sets

### 🎯 What is a Set?

A **set** is an **unordered collection** of **unique items**. It uses hashing and has no duplicates.

### 📋 Characteristics

| Feature | Details |
|---------|---------|
| **Unordered** | No specific order (321 = 123) |
| **Mutable** | Can add/remove items |
| **No Duplicates** | Each element is unique |
| **No Indexing** | Cannot access by index |
| **Immutable Elements** | Can't contain lists or dicts |
| **Fast Lookup** | Uses hashing |

---

### 📝 Creating Sets

```python
# Empty set (⚠️ {} is a dict, not a set!)
s1 = set()

# With items
s2 = {1, 2, 3}

# Duplicates removed automatically
s3 = {1, 5, 2, 3, 4, 1}  # {1, 5, 2, 3, 4}

# Type conversion
s4 = set([1, 2, 3])      # {1, 2, 3}
s5 = set("hello")        # {'h', 'e', 'l', 'o'}

# ❌ Cannot contain mutable items:
# s6 = {1, 2, [3, 4]}  # Error - lists not allowed
# s7 = {1, 2, {3, 4}}  # Error - sets not allowed
```

### 🔍 Membership & Equality

```python
s1 = {1, 2, 3}
s2 = {3, 2, 1}

print(s1 == s2)         # True (same content, order doesn't matter)
print(2 in s1)          # True
print(5 in s1)          # False
```

### ❌ No Indexing or Slicing

```python
s = {1, 2, 3}

# ❌ These won't work:
# print(s[0])         # Error
# print(s[1:3])       # Error
```

---

### ✏️ Adding & Updating Items

```python
s = {1, 2, 3, 4}

# Add single item
s.add(50)
print(s)                # {1, 2, 3, 4, 50}

# Add multiple items (must be iterable)
s.update([4, 5, 9, 8])
print(s)                # {1, 2, 3, 4, 5, 8, 9, 50}
```

### 🗑️ Deleting Items

```python
s = {1, 5, 2, 3}

# discard() - no error if not found
s.discard(5)            # {1, 2, 3}
s.discard(999)          # No error

# remove() - raises error if not found
s.remove(3)             # {1, 2}
# s.remove(999)         # ❌ KeyError!

# pop() - removes random item
s.pop()                 # Removes one item

# clear() - remove all
s.clear()               # Set is now empty
```

---

### 🔧 Set Operations

#### Union (|)

All elements from both sets (no duplicates):

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)          # {1, 2, 3, 4, 5}
print(s1.union(s2))     # {1, 2, 3, 4, 5}
```

#### Intersection (&)

Only common elements:

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 & s2)          # {3, 4}
print(s1.intersection(s2))  # {3, 4}
```

#### Difference (-)

Elements in first set but not in second:

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 - s2)          # {1, 2}
print(s2 - s1)          # {5, 6}
```

#### Symmetric Difference (^)

Elements unique to both sets:

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 ^ s2)          # {1, 2, 5, 6}
print(s1.symmetric_difference(s2))  # {1, 2, 5, 6}
```

---

### 📊 Set Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `add()` | Add one item | `s.add(5)` |
| `update()` | Add multiple | `s.update([1,2])` |
| `remove()` | Remove (error if not found) | `s.remove(5)` |
| `discard()` | Remove (no error) | `s.discard(5)` |
| `pop()` | Remove random | `s.pop()` |
| `clear()` | Remove all | `s.clear()` |
| `union()` | All elements | `s1.union(s2)` |
| `intersection()` | Common elements | `s1.intersection(s2)` |
| `difference()` | Not in second | `s1.difference(s2)` |
| `isdisjoint()` | No common items? | `s1.isdisjoint(s2)` |
| `issubset()` | Is s1 inside s2? | `s1.issubset(s2)` |
| `issuperset()` | Does s1 contain s2? | `s1.issuperset(s2)` |

---

### 🔍 Set Relationships

```python
s1 = {1, 2, 3}
s2 = {1, 2}
s3 = {4, 5}

# isdisjoint - no common items
print(s1.isdisjoint(s3))        # True (no overlap)

# issubset - is s2 inside s1?
print(s2.issubset(s1))          # True

# issuperset - does s1 contain s2?
print(s1.issuperset(s2))        # True
```

### 🔄 Set Comprehension

```python
# Create set with comprehension
s = {i for i in range(1, 10)}
print(s)                        # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# With condition
s2 = {i for i in range(1, 10) if i % 2 == 0}
print(s2)                       # {2, 4, 6, 8}
```

### 🧊 FrozenSet

Immutable set (cannot add/remove):

```python
s = [1, 2, 2, 3, 4]
fs = frozenset(s)              # frozenset({1, 2, 3, 4})

# ✅ Read operations work
print(1 in fs)                  # True

# ❌ Write operations fail
# fs.add(5)                     # Error
# fs.remove(1)                  # Error
```

---

## 🗝️ Dictionaries

### 🎯 What is a Dictionary?

A **dictionary** is a **key-value pair collection**, like a map or object. It stores data with unique keys.

### 📋 Characteristics

| Feature | Details |
|---------|---------|
| **Key-Value Pairs** | Data stored as {key: value} |
| **Mutable** | Can add/remove/modify items |
| **Unordered** | (Python 3.7+ maintains insertion order) |
| **Unique Keys** | No duplicate keys allowed |
| **Immutable Keys** | Keys must be immutable |
| **Indexed by Keys** | Access via keys, not positions |

---

### 📝 Creating Dictionaries

```python
# Basic dictionary
dict1 = {"name": "Krish", "age": 55}

# Empty dictionary
d = {}

# Homogeneous keys
d1 = {1: 10, 2: 20, 3: 30}

# Mixed keys
d2 = {1: (1, 2, 3), "hello": "world"}

# 2D dictionary (nested)
d3 = {
    "student1": {"name": "Krish", "roll": 1},
    "student2": {"name": "Gyan", "roll": 2}
}

# Type conversion
d4 = dict([("a1", "a2"), (1, 2)])
```

### 🔍 Accessing Values

```python
dict1 = {"name": "Krish", "age": 55}

# By key
print(dict1["name"])            # Krish

# Using get()
print(dict1.get("age"))         # 55
print(dict1.get("email", "N/A")) # N/A (default if not found)

# Nested access
d3 = {"s1": {"name": "Krish", "roll": 1}}
print(d3["s1"]["name"])         # Krish
```

### ✏️ Adding & Updating

```python
dict1 = {"name": "Krish"}

# Add new key
dict1["age"] = 25
print(dict1)                    # {'name': 'Krish', 'age': 25}

# Update existing key
dict1["name"] = "Gyan"
print(dict1)                    # {'name': 'Gyan', 'age': 25}

# Update multiple (from another dict)
dict2 = {"class": "A", "age": 30}
dict1.update(dict2)
print(dict1)
# {'name': 'Gyan', 'age': 30, 'class': 'A'}
```

### 🗑️ Deleting Items

```python
dict1 = {"name": "Krish", "age": 25, "city": "Delhi"}

# pop() - remove by key
dict1.pop("age")                # {'name': 'Krish', 'city': 'Delhi'}

# popitem() - remove last
dict1.popitem()                 # Removes most recent item

# del - remove by key
del dict1["name"]

# clear() - remove all
# dict1.clear()                 # {}
```

### 🔁 Iteration

```python
dict1 = {"name": "Krish", "age": 25, "city": "Delhi"}

# Iterate keys
for key in dict1:
    print(key)                  # name, age, city

# Iterate key-value pairs
for key, value in dict1.items():
    print(f"{key}: {value}")
```

### 📊 Dictionary Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `keys()` | Get all keys | `dict1.keys()` |
| `values()` | Get all values | `dict1.values()` |
| `items()` | Get all key-value pairs | `dict1.items()` |
| `get()` | Get value safely | `dict1.get("name")` |
| `pop()` | Remove by key | `dict1.pop("age")` |
| `popitem()` | Remove last | `dict1.popitem()` |
| `update()` | Merge dictionaries | `dict1.update(dict2)` |
| `clear()` | Remove all | `dict1.clear()` |

### 📋 Getting Dictionary Info

```python
dict1 = {"name": "Krish", "age": 25}

# Get all keys
print(dict1.keys())             # dict_keys(['name', 'age'])

# Get all values
print(dict1.values())           # dict_values(['Krish', 25])

# Get key-value pairs
print(dict1.items())
# dict_items([('name', 'Krish'), ('age', 25)])
```

---

## 📊 Comparison Table

| Aspect | List | Tuple | Set | Dictionary |
|--------|------|-------|-----|-----------|
| **Syntax** | `[]` | `()` | `{}` | `{}` with `:` |
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Ordered** | ✅ Yes | ✅ Yes | ❌ No | ✅ (3.7+) |
| **Indexed** | ✅ Yes | ✅ Yes | ❌ No | By key |
| **Duplicates** | ✅ Yes | ✅ Yes | ❌ No | No (keys) |
| **Speed** | Medium | ⚡ Fast | ⚡ Fast | ⚡ Fast |
| **Memory** | More | Less | Less | More |
| **Use Case** | Sequence | Immutable | Unique | Mapping |

---

## ✨ Key Takeaways

| Concept | Summary |
|---------|---------|
| **Tuples** | Immutable lists - use when data shouldn't change |
| **Sets** | Unique unordered items - use for membership testing |
| **Dictionaries** | Key-value storage - use for mapping data |
| **Speed** | Tuples & sets faster than lists & dicts |
| **Memory** | Tuples use least memory |
| **Immutability** | Makes tuples safe for concurrent code |
| **Set Operations** | Union, intersection, difference powerful for logic |
| **Dict Access** | Use `.get()` to avoid KeyError |

---

**Happy Coding! 🎉**
