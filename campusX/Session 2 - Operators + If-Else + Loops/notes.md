
## 📅 Friday, October 03, 2025, 1:53 PM IST

# 🐍 Python Operators

Python provides various operators to perform operations on data and variables.

***

## ➕ Arithmetic Operators

| Operator | Description | Example | Output |
| :-- | :-- | :-- | :-- |
| `+` | Addition | `5 + 6` | `11` |
| `-` | Subtraction | `5 - 6` | `-1` |
| `*` | Multiplication | `5 * 6` | `30` |
| `/` | Division (float) | `5 / 6` | `0.8333...` |
| `//` | Floor Division (integer) | `5 // 6` | `0` |
| `%` | Modulus (remainder) | `5 % 6` | `5` |
| `**` | Exponentiation (power) | `5 ** 6` | `15625` |

```python
print(5 + 6)    # 11
print(5 - 6)    # -1
print(5 * 6)    # 30
print(5 / 6)    # 0.8333333333333334
print(5 // 6)   # 0 (integer division)
print(5 ** 6)   # 15625 (5 to the power of 6)
```


***

## ⚖️ Relational (Comparison) Operators

| Operator | Description | Example | Output |
| :-- | :-- | :-- | :-- |
| `>` | Greater than | `4 > 5` | `False` |
| `<` | Less than | `4 < 5` | `True` |
| `>=` | Greater than or equal | `4 >= 5` | `False` |
| `<=` | Less than or equal | `4 <= 5` | `True` |
| `==` | Equal to | `4 == 5` | `False` |
| `!=` | Not equal to | `4 != 5` | `True` |

```python
print(4 > 5)    # False
print(4 < 5)    # True
print(4 >= 5)   # False
print(4 <= 5)   # True
print(4 == 5)   # False
print(4 != 5)   # True
```


***

## 🔗 Logical Operators

| Operator | Description | Example | Output |
| :-- | :-- | :-- | :-- |
| `and` | Both conditions must be True | `1 < 5 and 5 > 1` | `True` |
| `or` | At least one condition must be True | `1 > 5 or 5 > 1` | `True` |
| `not` | Reverses the condition | `not True` | `False` |

```python
print(1 < 5 and 5 > 1)  # True (both conditions are True)
print(1 > 5 or 5 > 1)   # True (second condition is True)
print(not True)         # False (reverses True to False)
```


***

## 🔢 Bitwise Operators

Work on binary representations of numbers:

### **`&` (Bitwise AND)**

- **Rule**: Keep bit as `1` only if both bits are `1`

```python
print(2 & 3)  # 2
# 2 = 10 (binary)
# 3 = 11 (binary)
# -----
# 2 = 10 (result)
```


### **`|` (Bitwise OR)**

- **Rule**: Keep bit as `1` if at least one bit is `1`

```python
print(2 | 3)  # 3
# 2 = 10 (binary)
# 3 = 11 (binary)
# -----
# 3 = 11 (result)
```


### **`^` (Bitwise XOR)**

- **Rule**: Keep bit as `1` only if bits are different

```python
print(2 ^ 3)  # 1
# 2 = 10 (binary)
# 3 = 11 (binary)
# -----
# 1 = 01 (result)
```


### **`~` (Bitwise NOT)**

- **Formula**: `~n = -(n + 1)`

```python
print(~5)  # -6
# 5 → flip all bits → add 1 → make negative
```


### **`<<` (Left Shift)**

- **Formula**: `n << k = n * (2 ** k)`

```python
print(5 << 1)  # 10
# 5 = 101 → shift left by 1 → 1010 = 10
```


### **`>>` (Right Shift)**

- **Formula**: `n >> k = n // (2 ** k)`

```python
print(5 >> 1)  # 2
# 5 = 101 → shift right by 1 → 10 = 2
```


***

## 📝 Assignment Operators

| Operator | Description | Example | Equivalent |
| :-- | :-- | :-- | :-- |
| `=` | Assign value | `a = 10` | `a = 10` |
| `+=` | Add and assign | `a += 10` | `a = a + 10` |
| `-=` | Subtract and assign | `a -= 10` | `a = a - 10` |
| `*=` | Multiply and assign | `a *= 2` | `a = a * 2` |
| `/=` | Divide and assign | `a /= 2` | `a = a / 2` |
| `%=` | Modulus and assign | `a %= 2` | `a = a % 2` |

```python
a = 10
print(a)     # 10
a += 10
print(a)     # 20
a -= 10
print(a)     # 10
a %= 2
print(a)     # 0
```

> **Note**: Python doesn't support `++` or `--` operators like C/C++

***

## 🔍 Membership Operators

Check if a value exists in a sequence:


| Operator | Description | Example | Output |
| :-- | :-- | :-- | :-- |
| `in` | Returns True if value exists | `'G' in 'Ghosh'` | `True` |
| `not in` | Returns True if value doesn't exist | `10 not in [1,2,3]` | `True` |

```python
print('G' in 'Ghosh')           # True
print(5 in [1, 2, 3, 6, 4])     # False
print(10 not in [1, 2, 3, 6, 4]) # True
```


***

## 🧮 Practical Example: Sum of Digits

**Problem**: Find the sum of all digits in a number entered by user.

```python
num = int(input("Enter the number: "))
sum = 0

while num != 0:
    r = num % 10      # Extract last digit
    sum = sum + r     # Add to sum
    num = num // 10   # Remove last digit

print(f"Sum of digits: {sum}")
```

**Example**:

- Input: `123`
- Process: `3 + 2 + 1 = 6`
- Output: `6`

***

## ✨ Key Takeaways

- **Arithmetic**: Use `//` for integer division, `**` for power
- **Bitwise**: Work on binary level, useful for optimization
- **Assignment**: Shorthand operators save code
- **Membership**: Perfect for checking existence in collections
- **Logic**: `and`, `or`, `not` for condition combinations

***
