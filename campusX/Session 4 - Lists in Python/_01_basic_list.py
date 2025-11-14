print("h")
listexample = [5, 1, 2, 3, "hallo", ["word", 50]]
print(listexample)

# how list store in memoery
print(id(5))
print(id(listexample[0]))
# both are same becuse both refer the same memory block

## Creating List
# Empty
print([])
# 1D list
print([1, 2, 3])
# 2D list
print([1, [1, 2, 3], 2, [4, 5, 6], 3, [7, 8, 9]])
# 3D list
print([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# hextrogenuous list where many types of data prent
print([5, "ji", 6.5])
# homogenius list use use same data type
# using type conversion
print(list("krish"))

## Accessing item from a list
L = [1, 2, 3, [5, 6]]
# positve
print(L[0])
# negative
print(L[-1])
# by [] we enter in the list
# how work on 2d list
print(L[3][0])
#
# # slicing
print(L[0::2])

# ## Accessing Items from a List
# # append
a = [1, 2, 3]
a.append(5)  # add 5 at last
print(a)
# extend use to add multiple elment on time
b = [11, 55, 99]
a.extend(b)

L = [1, 2, 3, 4, 5]
L.extend("delhi")  # This adds each character of "delhi"
print(L)
# insert
L.insert(1, 44)
print(L)
# we can change value via index and slicing
L[-1] = 5252
L[1:3] = [99, 96, 100]
print(L)
# Deleting items from a List
# del
L = [1, 2, 3, 4, 5]

# indexing
del L[-1]

# slicing
del L[1:3]
print(L)

# remove

L = [1, 2, 3, 4, 5]

L.remove(5)

print(L)
# pop
L = [1, 2, 3, 4, 5]

L.pop()

print(L)
# clear
L = [1, 2, 3, 4, 5]

L.clear()

print(L)

# operation on list
# arthmetic
l1 = [1, 2, 3]
l2 = [4, 5, 6, 4, 5]
l3 = l1 + l2  # same as string
print(l3)
l4 = l1 * 3  # mens its multiple l1 in 3 times then add in onelist
print(l4)
# membership
print(6 in l2)
# loop
for i in l3:
    print(i * 2)
## List Functions
# len give length
print(len(l3))
print(max(l3))
print(min(l3))
print(sorted(l3, reverse=True))

# count
print(l3.count(5))  # it find how many times the number apper in the list
# reversed is a permanate operation bit sorted is non permatent operation
l3.reverse()
print(l3)

# sort vs sorted
# sorted is non permatenet but sort is permatent
L = [2, 1, 5, 7, 0]
print(L)
print(sorted(L))
print(L)
L.sort()
print(L)
# List Comprehension
# List Comprehension provides a concise way of creating lists.
# newlist = [expression for item in iterable if condition == True]
# Advantages of List Comprehension
#
# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]
print(squares)  # [1, 4, 9, 16]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6]

fruits = ["apple", "banana", "cherry"]
upper_fruits = [f.upper() for f in fruits]
print(upper_fruits)

# Nested if with List Comprehension
basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'
ex = [i for i in my_fruits if i in basket if i.startswith("a")]
print(ex)

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i * j for i in range(1, 4)] for j in range(1, 4)])
