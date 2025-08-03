# Tuples and Membership Testing

# Tuples are defined in Python with () and are immutable:
# once created, their elements cannot be changed, added, or removed.

name = ("kelin", "ayanokoji", "naruto")
print(name)

# Unpacking tuple into variables
name1, name2, name3 = name
print(f"{name1}, {name3}, {name2}")

# Swapping values in Python (tuple unpacking)
num1 = 69
num2 = 96
print(f"Before swap -> num1: {num1}, num2: {num2}")
num2, num1 = num1, num2
print(f"After swap  -> num1: {num1}, num2: {num2}")

# Membership testing with 'in' returns a boolean (case-sensitive)
print(f"Is 'nobita' in name? {'nobita' in name}")
print(f"Is 'ayanokoji' in name? {'ayanokoji' in name}")
