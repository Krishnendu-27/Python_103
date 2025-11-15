print("\n" + "=" * 10 + " LISTS: CREATION & MEMORY " + "=" * 10 + "\n")

print("print('h') output:")
print("h")
listexample = [5, 1, 2, 3, "hallo", ["word", 50]]
print("\nExample list:")
print(listexample)

print(
    "\nMemory ids (addresses) - note: small integers are interned in CPython, so id(5) may equal id(listexample[0]):"
)
print("id(5) =", id(5))
print("id(listexample[0]) =", id(listexample[0]))
print(
    "# if these are the same, both names refer to the same immutable int object in memory\n"
)

print("=" * 10 + " CREATING LISTS " + "=" * 10)
print("Empty list:", [])
print("1D list:", [1, 2, 3])
print("2D list:", [1, [1, 2, 3], 2, [4, 5, 6], 3, [7, 8, 9]])
print("3D list:", [[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Heterogeneous list:", [5, "ji", 6.5])
print("From iterable using list():", list("krish"))

print("\n" + "=" * 10 + " ACCESSING LIST ITEMS " + "=" * 10)
L = [1, 2, 3, [5, 6]]
print("L =", L)
print("L[0] (first element):", L[0])
print("L[-1] (last element):", L[-1])
print("Access inside nested list L[3][0]:", L[3][0])
print("Slicing L[0::2] (every 2nd element from 0):", L[0::2])

print("\n" + "=" * 10 + " MODIFYING LISTS " + "=" * 10)
a = [1, 2, 3]
a.append(5)  # add 5 at last
print("After append(5):", a)

b = [11, 55, 99]
a.extend(b)
print("After extend([11,55,99]):", a)

L = [1, 2, 3, 4, 5]
L.extend("delhi")  # This adds each character of "delhi"
print("After extend('delhi') -> each char appended:", L)

L.insert(1, 44)  # insert at index 1
print("After insert(1, 44):", L)

L[-1] = 5252  # replace last element
L[1:3] = [
    99,
    96,
    100,
]  # slice assignment replaces elements at indices 1 and 2 with three elements
print("After L[-1]=5252 and L[1:3]=[99,96,100]:", L)

print("\n" + "=" * 10 + " DELETING ITEMS " + "=" * 10)
L = [1, 2, 3, 4, 5]
del L[-1]  # delete by index
print("After del L[-1]:", L)
del L[1:3]  # delete by slice (indices 1 and 2)
print("After del L[1:3]:", L)

L = [1, 2, 3, 4, 5]
L.remove(5)  # remove by value (first occurrence)
print("After remove(5):", L)

L = [1, 2, 3, 4, 5]
popped = L.pop()  # pop last element and return it
print("After pop():", L, " -> popped value:", popped)

L = [1, 2, 3, 4, 5]
L.clear()
print("After clear():", L)

print("\n" + "=" * 10 + " OPERATIONS ON LISTS " + "=" * 10)
l1 = [1, 2, 3]
l2 = [4, 5, 6, 4, 5]
l3 = l1 + l2
print("Concatenation l1 + l2:", l3)
l4 = l1 * 3
print("Repetition l1 * 3:", l4)
print("Membership check 6 in l2:", 6 in l2)

print("\nLooping through l3 and printing each value*2:")
for i in l3:
    print(i * 2, end=" ")
print()  # newline

print("\nList functions: len, max, min, sorted")
print("len(l3) =", len(l3))
print("max(l3) =", max(l3))
print("min(l3) =", min(l3))
print(
    "sorted(l3, reverse=True) -> returns NEW list, original l3 unchanged:",
    sorted(l3, reverse=True),
)

print("\nCounting, reversing, and sorting (in-place vs returning new):")
print("l3.count(5) =", l3.count(5))  # count occurrences
l3.reverse()  # in-place reverse
print("After l3.reverse() (in-place):", l3)
L = [2, 1, 5, 7, 0]
print("L before sorted()/sort():", L)
print("sorted(L) -> returns NEW sorted list:", sorted(L))
print("L after sorted(L) call (unchanged):", L)
L.sort()  # in-place sort
print("L after L.sort() (in-place):", L)

print("\n" + "=" * 10 + " LIST COMPREHENSIONS " + "=" * 10)
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]
print("squares from [1,2,3,4]:", squares)
evens = [n for n in numbers if n % 2 == 0]
print("evens from [1..4]:", evens)
fruits = ["apple", "banana", "cherry"]
upper_fruits = [f.upper() for f in fruits]
print("upper_fruits:", upper_fruits)

basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]
ex = [i for i in my_fruits if i in basket if i.startswith("a")]
print("Filtered list from my_fruits that are in basket and start with 'a':", ex)
print("Nested list comprehension 3x3 matrix:")
print([[i * j for i in range(1, 4)] for j in range(1, 4)])

print("\n" + "=" * 10 + " ZIP AND OBJECTS IN LISTS " + "=" * 10)
L1 = [1, 2, 3]
L2 = [-1, -2, -3]
z = list(zip(L1, L2))  # zip pairs elements: (1,-1),(2,-2),(3,-3)
print("list(zip(L1, L2)):", z)

L5 = [1, 2, print, type]
print("List holding functions and objects:", L5)
print("Calling the stored print function from L5:")
L5[2]("Hello from stored print!")  # demonstrates that functions are objects

print("\n" + "=" * 10 + " SHALLOW COPY VS REFERENCE " + "=" * 10)
a = [1, 2, 3]
b = a  # b references same list
a.append(4)
print("After a.append(4), a:", a, "b (same ref):", b)
c = (
    a.copy()
)  # shallow copy, different object but same elements (for immutable elements it's fine)
a.append(5)
print("After a.append(5), a:", a, "c (shallow copy made earlier):", c)
print("Note: lists are mutable and can use more memory than simple arrays.")

print("\n" + "=" * 10 + " STRINGS: CREATION & SLICING " + "=" * 10)
a = "ab"
b = "cd"
c = " hi "
e = str("hi bro")
print("String a:", a)
print("String b:", b)
print("String c:", c)
print("String e:", e)

print("\nIndexing and slicing examples:")
g = "my name is K"
print("g:", g)
print("g[5] ->", g[5])  # character at index 5
print("g[-1] ->", g[-1])  # last character
print("g[0:6] ->", g[0:6])
print("g[0:] ->", g[0:])
print("g[:4] ->", g[:4])
print("g[0::2] ->", g[0::2])
print("g[::-1] (reversed string) ->", g[::-1])

print("\n" + "=" * 10 + " END OF DEMO " + "=" * 10 + "\n")
