"""
Pretty / runnable version of your sets example.
I kept your original logic and lines, only added printed explanations.
"""

print("\n=== SET BASICS: creation & properties ===")

# empty set ({} is dict by default -> use set())
se = set()
print("se (empty set):", se)

# 1d set
s1 = {1, 2, 3}
print("s1 (1D set):", s1)

# 2d set (not allowed to store mutable types inside a set)
# s2 = {3, 4, 5, {7, 8, 9}}  # this will not work because set can't contain mutable types
print("Note: sets cannot contain mutable elements like lists or other sets.")

# using type conversion from list
s3 = set([1, 2, 3])
print("s3 (from list):", s3)

# duplicate not allowed
s4 = {1, 5, 2, 3, 4, 1}  # removes duplicate 1
print("s4 (duplicates removed):", s4)

print("\n=== ORDER & EQUALITY ===")
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print("s1 == s2? (order doesn't matter):", s1 == s2)
print("You cannot use indexing or slicing on sets (they are unordered).")

print("\n=== MUTATING SETS: add / update ===")
ss = {1, 2, 3, 4}
print("ss before add/update:", ss)
ss.add(50)  # hashing decides internal position
ss.update([4, 5, 9, 8])  # update from iterable
print("ss after add(50) and update([4,5,9,8]):", ss)

print("\n=== DELETING ELEMENTS ===")
# del example
s = {1, 5, 9}
print("s before del:", s)
del s
print("s deleted with del (variable removed).")

# discard example (no error if element missing)
s = {1, 5, 2, 3}
print("new s:", s)
s.discard(5)
print("after s.discard(5):", s)

# remove example (will raise error if element missing)
s.remove(3)  # 3 is present now
print("after s.remove(3):", s)

# pop removes a random item
popped = s.pop()
print("s.pop() removed:", popped, " → s now:", s)

# clear to empty the set
s.clear()
print("after s.clear():", s)

print("\n=== SET OPERATIONS (union, intersection, difference, symmetric diff) ===")
s1 = {6, 2, 3, 3, 4, 5}
s2 = {1, 2, 5, 6.6, 3, 5, 5, 2}
print("s1:", s1)
print("s2:", s2)

print("Union (s1 | s2):", s1 | s2)
print("Intersection (s1 & s2):", s1 & s2)
print("Difference s1 - s2:", s1 - s2)
print("Difference s2 - s1:", s2 - s1)
print("Symmetric difference (s1 ^ s2):", s1 ^ s2)
print("Membership test: is 1 in s2?", 1 in s2)

print("\n=== AGGREGATE FUNCTIONS ON SETS ===")
print("len(s1):", len(s1))
print("max(s2):", max(s2))
print("min(s2):", min(s2))
print("sorted(s2):", sorted(s2))
print("s1.union(s2):", s1.union(s2))

print("\n=== INTERSECTION METHODS & IN-PLACE ===")
print("s1.intersection(s2):", s1.intersection(s2))
# intersection_update returns None (it mutates s1). We'll show that behavior.
print("s1 before intersection_update:", s1)
result = s1.intersection_update(s2)
print("Result of s1.intersection_update(s2) (returned):", result)
print("s1 after intersection_update (mutated):", s1)

print("\n=== SYMMETRIC DIFFERENCE & RELATION CHECKS ===")
s3 = {1, 2, 3, 4, 51}
s4 = {4, 5, 21, 1, 2}
print("s3:", s3)
print("s4:", s4)
print("s3.symmetric_difference(s4):", s3.symmetric_difference(s4))

print("isdisjoint (s3 with itself):", s3.isdisjoint(s3))  # will be False
print("issubset (s1 subset of s2?):", s1.issubset(s2))
print("issuperset (s2 superset of s1?):", s2.issuperset(s1))

print("\n=== FROZENSET (immutable set) ===")
s5 = [1, 2, 2, 3, 4, 5, 7]
fs = frozenset(s5)
print("Original list s5:", s5)
print("frozenset(fs):", fs)
print(
    "Note: frozenset supports read operations but not write operations like add/remove."
)

print("\n=== SET COMPREHENSION ===")
print("{i for i in range(1, 10)} ->", {i for i in range(1, 10)})

print("\n=== END ===")

