# Tuple 
# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# In short, a tuple is an *immutable* list. A tuple can not be changed in any way once it is created.
# Characterstics
# Ordered
# Unchangeble
# Allows duplicate

### Creating Tuples
# empty
t1 = ()
# sinlgle item tuple refer its data type
t2 = 3  # wrong
t3 = (3,)  # right
t4 = (1, 2, 3, 50)  # homegenius tuple
t5 = (
    5,
    99,
    "halo",
    63.6,
)  # hettogenuis tuple
t6 = (1, (1, 2), 3, (5, 4))
t7 = tuple("hallo")  # creation tuple via tuple
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t7)

### Accessing Items
# Indexing its also support - indexing and if index not available give error
print(t4[2])
# Slicing
print(t5[0::2])

# for nested tuple
print(t6[1][1])


### Editing items and adding items
# its deos not support becuse tuple inmutable


### deldeting items
# we can delte a full tuple but not a single elmnet dosnot allow

l10 = (1, 2, 5, 6, 3)
print(l10)
del l10

## operation and function on tuple
# + and *
l11 = (1, 4, 7, 8, 9)
l12 = (7, 8, 9, 6, 3)
print(l11 + l12)
print(l12 * 2)
# membership
print(5 in l12)
# iteration
for i in l12:
    print(i * 5)

l1 = (1, 4, 5, 6, 3, 2, 7, 8, 9, 10)
# function
# sum , len , max . sorted avaialbe on tuple
print(len(l1))
print(max(l1))
print(min(l1))
print(sorted(l1))
print(l1.index(6))

### Difference between Lists and Tuples

# - Syntax
# - Mutability
# - Speed its deciede wich is mutable or imutable imutable data type are faster we find it by time
import time

L = list(range(10000))
T = tuple(range(10000))
start = time.time()
for i in L:
    i * 5
print("list time", time.time() - start)

start = time.time()
for i in T:
    i * 5
print("tupple time", time.time() - start)
# its fater

# - Memory
import sys

print("list size ", sys.getsizeof(L))
print("tupple size ", sys.getsizeof(T))  # agin its take less space
# - Built in functionality is more in list than tupple becuse list in imutable
# - Error prone : its more error prone its took more debuging becuscs it dynamic

# - Usability: why need tuple if all thing happend in list becuse tuple is inmutable
# its for use in read only tuple more usefull

## tupl unpacking
a, b, c = (1, 2, 3)
# its need to be baclneced
print(a, b, c)

# so zip can help us to merge 2 or more elmnet we can see it by unpacking
zip1 = (1, 2, 3, 4, 5, 6)
zip2 = (7, 8, 9, 10, 11, 12)
z = zip(zip1, zip2)
print(list(z))  # its give list of tupple

# set 

# a set is an unoders collection of items every set elmnet is quniqu no duplicate  and it must be immutable cannot changed
# however a set itself mutable we can add and remoce items from it
# set can also be used to perform mathametical set operation union , intersection
# charcetrthis
# - its unorder mens 321 = 123
# - mutable
# - we cannot have suplicate value
# -  can not contain mutable data type mens we can not store set in set but number in set is possible

# empty
# in pythoon dictonry and set bot use {} but by default { } reprasent dictonary
se = set()
# 1 d set
s1 = {1, 2, 3}
# 2d set
# s2 = {3, 4, 5, {7, 8, 9}}  this will not work becuse we can not store imutable data in set
# set are unorder its use hasing by default
# using type convertion
s3 = set([1, 2, 3])
# duplicate not allowd
s4 = {1, 5, 2, 3, 4, 1}  # it remove the duplicate one
print(s4)
# in set
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2)  # true becuse the content is same
# we can not use index in set and slicing also

# but we can add delte and uodate
ss = {1, 2, 3, 4}
ss.add(50)  # hassing cohtrol the idnexing of new ittem
ss.update([4, 5, 9, 8])  # we have to send it via list
print(ss)

## delteing keyword
# del
s = {1, 5, 9}
del s
# discard
s = {1, 5, 2, 3}
s.discard(5)  # we can delte a item and if not available the tem its not whrow error
# remove
s.remove(3)  # if not available the tem  its  whrow error

s.pop()  # it delte a random item
# clear : to delte full set
s.clear()

## set operation
s1 = {6, 2, 3, 3, 4, 5}
s2 = {1, 2, 5, 6.6, 3, 5, 5, 2}
# union (|) every set ietem will print one one time no duplicate
print(s1 | s2)
# intersection (&) :  only print common item
print(s1 & s2)
# diffrence(-) only print the item not presennt in sencon set but prenst on first set
print(s1 - s2)
print(s2 - s1)
# symetric difference (^) it print all th elmnet that are uniqu in both set
print(s1 ^ s2)
# menership test
print(1 in s2)

# set have also min max , len , sorted
print(len(s1))
print(max(s2))
print(min(s2))
print(sorted(s2))

print(s1.union(s2))

## intersection is just give the common elemenet
print(s1.intersection(s2))
# intersection_update is store value of intersection in first set
print(s1.intersection_update(s2))
# symmetric_difference
s3 = {1, 2, 3, 4, 51}
s4 = {4, 5, 21, 1, 2}
print(s3.symmetric_difference(s4))

# is disjoint : mens any ietms are not comon
print(s3.isdisjoint(s3))
# issubset:  mens is 1st set have all the lmnet that listed on set 2
print(s1.issubset(s2))
# issuperset mens is all value of first set is  presnt in secoend  item
print(s2.issuperset(s1))
# frozenset we can not change after creation we can past anything mens list tupple or dicotinory
s5 = [1, 2, 2, 3, 4, 5, 7]
fs = frozenset(s5)
# all operation work becuse its not change the set we just read but wont work write operation like  push remove

# it also work set compreshintion
print({i for i in range(1, 10)})
