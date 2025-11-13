# 🐍 Python Strings: Quick Reference Guide


***

## 🔤 What are Strings?

Strings are **sequences of Unicode characters** representing text. They're **immutable** (cannot be changed after creation).

***

## 📝 Creating Strings

### Different Ways to Create

```python```

# Single quotes

name = 'Alice'

# Double quotes

city = "New York"

# Triple quotes (multiline)

bio = """I am learning
Python programming
with passion"""

# Using str()

number = str(42)  \# "42"

```

---

## 🔍 String Indexing & Slicing

### Positive & Negative Indexing

``````python
word = "Python"
#  Index: 0 1 2 3 4 5
#         P y t h o n
#  Neg:  -6-5-4-3-2-1

print(word[0])      # P
print(word[-1])     # n (last character)
print(word[2])      # t
```


### Slicing Examples

``````
text = "Hello World"

print(text[0:5])    # Hello (index 0 to 4)
print(text[6:])     # World (from index 6 to end)
print(text[:5])     # Hello (start to index 4)
print(text[::2])    # HloWrd (every 2nd character)
print(text[::-1])   # dlroW olleH (reversed!)
```

---

## 🎯 Operations on Strings

### Concatenation & Repetition

``````python
print("Hello" + " " + "Python")  # Hello Python
print("Hi! " * 3)                # Hi! Hi! Hi!
```

### Comparison

```python```
print("apple" == "apple")        # True
print("apple" != "orange")       # True
print("dog" > "cat")             # True (lexicographic)
```

### Membership

``````python
text = "Python Programming"

print("Python" in text)          # True
print("Java" in text)            # False
print("gram" in text)            # True (substring exists)
```

***

## 🔧 Essential String Methods

### Case Conversion

```python```
text = "Hello World"

print(text.lower())              # hello world
print(text.upper())              # HELLO WORLD
print(text.capitalize())         # Hello world
print(text.title())              # Hello World
print(text.swapcase())           # hELLO wORLD
```

### Finding & Counting

``````python
text = "Programming is fun and amazing"

print(text.find("is"))           # 12 (first index)
print(text.count("a"))           # 2 (occurrences)
print(text.startswith("Pro"))    # True
print(text.endswith("ing"))      # True
```

### Splitting & Joining

```python```
# Split into words
sentence = "I love Python programming"
words = sentence.split()         # ['I', 'love', 'Python', 'programming']

# Join back together
rejoined = " ".join(words)       # "I love Python programming"
with_dash = "-".join(words)      # "I-love-Python-programming"
```

### Replacing

``````python
text = "I love Java"

new_text = text.replace("Java", "Python")
print(new_text)                  # I love Python
```

### Cleaning

```python```
text = "  Python  "

print(text.strip())              # Python (remove both ends)
print(text.lstrip())             # Python   (remove left)
print(text.rstrip())             #   Python (remove right)
```

---

## 📊 Checking String Types

``````python
print("123".isdigit())           # True (only digits)
print("abc".isalpha())           # True (only letters)
print("abc123".isalnum())        # True (letters + numbers)
print("_test".isidentifier())    # True (valid variable name)
```

***

## 🎨 String Formatting

### F-Strings (Recommended)

```python```
name = "Alice"
age = 25

print(f"My name is {name} and I am {age}")
# My name is Alice and I am 25
```

### Format Method

``````python
template = "Hello {}, you scored {}"
result = template.format("Bob", 95)
print(result)                    # Hello Bob, you scored 95
```

***

## 🔁 Looping Through Strings

``````

text = "Python"

# Loop through each character

for char in text:
print(char)

# Output: P y t h o n

# Loop with index

for i, char in enumerate(text):
print(f"{i}: {char}")

# Output: 0: P, 1: y, 2: t, 3: h, 4: o, 5: n

```

---

## 💡 Important: Strings are Immutable

``````python
text = "Hello"

# ❌ This will cause an error:
# text[0] = "J"  # TypeError

# ✅ Create a new string instead:
text = "J" + text[1:]
print(text)                      # Jello
```


***

## 🎯 Quick Cheat Sheet

| Task| Task | Code | Result |
|------|------|--------|
| **Length** | `len("Hello")` | 5 |
| **Reverse** | `"Hello"[::-1]` | "olleH" |
| **Uppercase** | `"hello".upper()` | "HELLO" |
| **Remove spaces** | `" Hi ".strip()` | "Hi" |
| **Replace** | `"cat".replace("c", "b")` | "bat" |
| **Split** | `"a b c".split()` | ['a', 'b', 'c'] |
| **Join** | `"-".join(['a','b'])` | "a-b" |
| **Find** | `"hello".find("l")` | 2 |
| **Count** | `"hello".count("l")` | 2 |
| **Check digit** | `"123".isdigit()` | True |

***

## 🚀 Common Use Cases

### Extract Information

```python```
email = "user@example.com"
username = email.split("@")   \# "user"
domain = email.split("@")     \# "example.com"

```

### Clean Data

``````python
messy = "  PYTHON  "
clean = messy.strip().lower()    # "python"
```


### Format Output

```python```
items = ["apple", "banana", "cherry"]
print(f"Fruits: {', '.join(items)}")

# Fruits: apple, banana, cherry

```

---

## ✨ Key Takeaways

- 🔤 Strings are **immutable** sequences of Unicode characters
- 📍 Use **indexing** to access single characters
- ✂️ Use **slicing** to extract substrings
- 🔄 Use **methods** like `.lower()`, `.split()`, `.replace()`
- 🎨 Use **f-strings** for clean string formatting
- 🔁 **Loop** through strings character by character
- ⚠️ Remember: Strings cannot be changed; create new ones instead

---```
--
