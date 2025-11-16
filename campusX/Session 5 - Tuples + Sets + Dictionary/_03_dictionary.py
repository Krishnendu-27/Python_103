"""
Pretty / runnable version of your dictionary example.
All original lines and logic are kept; I only added printed explanations.
"""

print("\n=== DICTIONARY BASICS: creation & properties ===")

# dictionary is a clction of key value pair use to store value like object its hold two value
# its knowns for map or associative array
# its mutabel we can change and add or delte
# indexing has no mening liket set index dont matter
# key can not be duplicate in dictionary
# key can not mutable items
dict = {"name": "Krish", "age": 55}
print("Initial dict:", dict)

# empty dictionary
d = {}
print("Empty dict d:", d)

# 1d dict and its homogenius becuts its key is same data type
d1 = {1: 10, 2: 20, 3: 30}
print("d1 (1D/homogeneous keys):", d1)

# with mixed keys
d2 = {1: (1, 2, 3), "hallo": "world"}
print("d2 (mixed keys):", d2)

# 2d dictonry
d3 = {
    "s1": {
        "name": "k",
        "rool": 1,
    },
    "s2": {
        "name": "G",
        "rool": 2,
    },
}
print("d3 (2D dictionary):", d3)

# type convertion
# d4 = dict([("a1", "a2"), (1, 2)])
# print(d4)
# we cann not have duplicate keys
# we can not provide mutable data type as parameter

# in dict indeing not allowed
# we search value by keys
print("\nAccessing values by key:")
print("dict['name'] ->", dict["name"])
# or we can use get
print("dict.get('age') ->", dict.get("age"))

# addding keyvalue pair
# diconaryname [key name] = value
dict["class"] = "A"
print("\nAfter adding dict['class'] = 'A':", dict)

# remove a key value pair
# pop
dict.pop("class")
print("After dict.pop('class') (removed 'class'):", dict)
# popitem it delte last key va;ue pair
dict.popitem()
print("After dict.popitem() (removed last key-value):", dict)
# del delte by keyvalue pair
# Note: following delete assumes 'name' is present; this follows your original logic
del dict["name"]
print("After del dict['name'] (removed 'name'):", dict)
# pop and del work same
# clear it clearn all
#
print("\nAccessing nested dict value d3['s1']['name'] ->", d3["s1"]["name"])

# eddng value
s5 = {"sub": "DSA", "name": "partush", "video": 50}
print("\nOriginal s5:", s5)
s5["sub"] = "python"
print("After s5['sub'] = 'python':", s5)

print("\nIterating over s5 (key : value):")
# in dictionary all aboutr keys values not matter
for i in s5:
    print(i, ": ", s5[i])

# itesms / keys / values
print("\ns5.items() ->", s5.items())  # give in list format
print("s5.keys() ->", s5.keys())
print("s5.values() ->", s5.values())

# upate its update a given dictionary with another dictionary its permanet
s6 = {"sub": "POM", "age": 55}
print("\ns6 to update s5 with:", s6)

s5.update(s6)
print("After s5.update(s6):", s5)

print("\n=== END ===")
