# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# In short, a tuple is an *immutable* list. A tuple can not be changed in any way once it is created.
# Characterstics
# Ordered
# Unchangeble
# Allows duplicate

print("\n=== Creating Tuples ===")

# empty
t1 = ()
print("t1 (empty tuple):", t1)

# sinlgle item tuple refer its data type
t2 = 3  # wrong
print("t2 (wrong single item, it's int):", t2)

t3 = (3,)  # right
print("t3 (correct single item tuple):", t3)

t4 = (1, 2, 3, 50)  # homegenius tuple
print("t4 (homogeneous):", t4)

t5 = (
    5,
    99,
    "halo",
    63.6,
)  # hettogenuis tuple
print("t5 (heterogeneous):", t5)

t6 = (1, (1, 2), 3, (5, 4))
print("t6 (nested tuple):", t6)

t7 = tuple("hallo")  # creation tuple via tuple
print("t7 (tuple from string):", t7)


print("\n=== Accessing Items ===")
print("t4[2] =", t4[2])
print("t5[0::2] =", t5[0::2])
print("Nested item t6[1][1] =", t6[1][1])


print("\n=== Editing items ===")
print("Tuples are immutable → cannot edit or add items")


print("\n=== Deleting Tuple ===")
l10 = (1, 2, 5, 6, 3)
print("Before deleting l10:", l10)
del l10
print("l10 deleted successfully")


print("\n=== Operations on Tuples ===")
l11 = (1, 4, 7, 8, 9)
l12 = (7, 8, 9, 6, 3)

print("l11 + l12 =", l11 + l12)
print("l12 * 2 =", l12 * 2)
print("Is 5 in l12? →", 5 in l12)

print("\nIterating on l12 (each * 5):")
for i in l12:
    print(i * 5)

l1 = (1, 4, 5, 6, 3, 2, 7, 8, 9, 10)

print("\n=== Functions on Tuple ===")
print("len(l1) =", len(l1))
print("max(l1) =", max(l1))
print("min(l1) =", min(l1))
print("sorted(l1) =", sorted(l1))
print("Index of 6 in l1 =", l1.index(6))


print("\n=== List vs Tuple Speed Test ===")
import time

L = list(range(10000))
T = tuple(range(10000))

start = time.time()
for i in L:
    i * 5
print("List time:", time.time() - start)

start = time.time()
for i in T:
    i * 5
print("Tuple time:", time.time() - start)


print("\n=== Memory Usage ===")
import sys

print("List size:", sys.getsizeof(L))
print("Tuple size:", sys.getsizeof(T))


print("\n=== Tuple Unpacking ===")
a, b, c = (1, 2, 3)
print("Unpacked values:", a, b, c)

print("\n=== Zip Example ===")
zip1 = (1, 2, 3, 4, 5, 6)
zip2 = (7, 8, 9, 10, 11, 12)

z = zip(zip1, zip2)
print("Zipped list:", list(z))
