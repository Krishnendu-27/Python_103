# =====================================
# String Creation and Basics
# =====================================

print("\n--- STRING CREATION ---")
a = "ab"
b = "cd"
c = """ hi """
e = str("hi bro")

print("String a:", a)
print("String b:", b)
print("String c:", c)
print("String e:", e)

# =====================================
# Indexing and Slicing
# =====================================

print("\n--- INDEXING AND SLICING ---")
g = "my name is K"
print("String g:", g)
print("Character at index 5:", g[5])  # e
print("Last character (negative index):", g[-1])  # K
print("Slice g[0:6]:", g[0:6])  # my nam
print("Slice g[0:]:", g[0:])  # my name is K
print("Slice g[:4]:", g[:4])  # my n
print("Slice g[0::2]:", g[0::2])  # skipping
print("Reversed string g[::-1]:", g[::-1])

# =====================================
# Deleting a String
# =====================================

print("\n--- DELETE STRING VARIABLE ---")
s = "bro"
print("Before delete:", s)
del s
print("After delete: variable 's' deleted (cannot print now)")

# =====================================
# String Operations Overview
# =====================================

print("\n--- STRING OPERATIONS ---")

# Arithmetic
print("\n[Arithmetic Operations]")
print("'delhi' + ' mumbai' =", "delhi" + " mumbai")
print("'krish' * 5 =", "krish" * 5)

# Relational
print("\n[Relational Operations]")
print("'delhi' != 'pune' =", "delhi" != "pune")
print("'mumbai' > 'delhi' =", "mumbai" > "delhi")
print("'Pune' > 'pune' =", "Pune" > "pune")

# Logical
print("\n[Logical Operations]")
print("'hello' and '' =", "hello" and "")
print("'hello' or 'world' =", "hello" or "world")

# =====================================
# Loops on Strings
# =====================================

print("\n--- LOOPS ON STRINGS ---")
s = "hihalo bro"
print("Loop printing each character:")
for i in s:
    print(i, end=" ")
print("\nLoop printing 'h' for each iteration:")
for i in s:
    print("h", end=" ")
print()

# =====================================
# Membership Operations
# =====================================

print("\n--- MEMBERSHIP OPERATIONS ---")
print("'D' in s:", "D" in s)

# =====================================
# Common String Functions
# =====================================

print("\n--- COMMON STRING FUNCTIONS ---")
print("Length of s:", len(s))
print("Max character in s (by ASCII):", max(s))
print("Min character in s (by ASCII):", min(s))
print("Sorted list of characters in s:", sorted(s))
print("Sorted in reverse:", sorted(s, reverse=True))

# =====================================
# String Methods
# =====================================

print("\n--- STRING METHODS ---")
a = "halo bro"
print("Original string:", a)
print("capitalize() ->", a.capitalize())
print("lower() ->", a.lower())
print("swapcase() ->", a.swapcase())

print("\nCount and Find:")
print("'my name is kai'.count('k') =", "my name is kai".count("k"))
print("'my name is kai'.find('k') =", "my name is kai".find("k"))
print("'my name is kai'.index('k') =", "my name is kai".index("k"))

print("\nstartswith() / endswith():")
print("'my name is bro'.endswith('bro') =", "my name is bro".endswith("bro"))
print("'my name is bro'.startswith('bro') =", "my name is bro".startswith("bro"))

# =====================================
# Formatting and Checking Methods
# =====================================

print("\n--- STRING FORMATTING & CHECK METHODS ---")
name = "krish"
gender = "male"
print("Formatted string:", "Hi, my name is {} and I am {}".format(name, gender))
print("isalnum() ->", name.isalnum())
print("isalpha() ->", name.isalpha())

# =====================================
# Split / Join / Replace
# =====================================

print("\n--- SPLIT / JOIN / REPLACE ---")
sentence = "hi halo bro how ared"
print("Original sentence:", sentence)
print("Split ->", sentence.split())
print("Join ->", " ".join(["hi", "halo", "bro", "how", "ared"]))
print("Replace 'bro' with 'brother' ->", sentence.replace("bro", "brother"))

print("\n--- END OF PROGRAM ---")

