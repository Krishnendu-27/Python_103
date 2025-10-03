
## 📅 Friday, October 03, 2025, 5:40 PM IST

# 🎯 Python Conditionals, Modules \& Loops

Python uses **branching** for different scenarios and **loops** for repetitive tasks.

***

## 🔀 If-Else Conditionals

**Branching** means code takes different paths based on conditions.

### 📧 Login System Example

```python
email = input("Enter the email: ")
password = int(input("Enter the password: "))

if email == "o@gmail.com" and password == 1234:
    print("Correct! Welcome sir")
elif email == "o@gmail.com" and password != 1234:
    print("Email correct! Password is wrong")
elif email != "o@gmail.com" and password == 1234:
    print("Password correct! Email is wrong")
else:
    print("Incorrect! Try again")
```

> **🔑 Key Point**: Python uses **indentation** instead of braces `{}` for scope

### 🔢 Find Largest of 3 Numbers

```python
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"The biggest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The biggest number is {num2}")
else:
    print(f"The biggest number is {num3}")
```


***

## 📦 Python Modules

**Modules** are libraries containing pre-written code for common tasks.

### 🔢 Math Module

```python
import math

print(math.factorial(5))  # 120
pi = math.pi
print(pi)                 # 3.141592653589793
```


### 🔤 Keywords Module

```python
import keyword

print(keyword.kwlist)     # Shows all Python keywords
```


### 🎲 Random Module

```python
import random

print(random.randint(1, 50))  # Random number between 1-50
```


### 📅 Datetime Module

```python
import datetime

print(datetime.datetime.now())  # Current date and time
```

> **💡 Pro Tip**: Use `help('modules')` to see all available modules

***

## 🔄 Loops

Loops help show repetitive content (like products on e-commerce sites).

### ⚪ While Loop

**Basic While Loop**:

```python
x = 1
while x < 5:
    print(x)
    x += 1
else:
    print("Limit crossed!")
```

**Output**:

```
1
2
3
4
Limit crossed!
```


### 🎯 Guessing Game

```python
import random

rand = random.randint(1, 10)
n = 0
count = 0

while n != rand:
    n = int(input("Enter your guess: "))
    count += 1
    
    if n > rand:
        print("Too high! Guess lower")
    elif n < rand:
        print("Too low! Guess higher")
    else:
        print(f"Correct! You guessed it in {count} attempts")
        break
```


***

### 🔥 For Loop with Range

**Basic For Loop**:

```python
for i in range(1, 11, 2):  # start, stop, step
    print(i)
```

**Output**: `1 3 5 7 9`

**Countdown**:

```python
for i in range(10, -1, -1):  # 10 to 0
    print(i)
```

**String Iteration**:

```python
for i in 'DELHI':
    print(i)
```

**Output**:

```
D
E
L
H
I
```


***

## 🎲 Range Function Patterns

| Pattern | Code | Output |
| :-- | :-- | :-- |
| **Count Up** | `range(1, 6)` | `1, 2, 3, 4, 5` |
| **Count Down** | `range(5, 0, -1)` | `5, 4, 3, 2, 1` |
| **Skip Numbers** | `range(0, 10, 2)` | `0, 2, 4, 6, 8` |
| **From Zero** | `range(5)` | `0, 1, 2, 3, 4` |


***

## 🎯 Common Modules Quick Reference

| Module | Purpose | Common Functions |
| :-- | :-- | :-- |
| **`math`** | Mathematical operations | `factorial()`, `pi`, `sqrt()` |
| **`random`** | Random numbers/choices | `randint()`, `choice()`, `shuffle()` |
| **`datetime`** | Date and time operations | `now()`, `date()`, `time()` |
| **`keyword`** | Python keywords | `kwlist` |


***

## ✨ Key Takeaways

- **🎯 Conditionals**: Use `if-elif-else` for branching logic
- **📦 Modules**: Import libraries with `import module_name`
- **🔄 While Loop**: Great for unknown iterations (like guessing games)
- **🔥 For Loop**: Perfect for known iterations using `range()`
- **📏 Indentation**: Python's way of defining code blocks
- **🎲 Range**: Flexible function for generating number sequences

***
