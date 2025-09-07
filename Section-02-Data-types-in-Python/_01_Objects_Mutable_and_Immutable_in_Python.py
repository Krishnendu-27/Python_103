# Object must have identity , type , value

sugar_ammount = 2
print(f"sugar amount in first: {sugar_ammount}")

sugar_ammount = 12
print(f"sugar amount in second: {sugar_ammount}")

# The variable sugar_ammount does not change the integer object;
# it simply points to a new reference (12 instead of 2).
# To confirm, we can compare their ids:
print(f"id of integer 2: {id(2)}")    # e.g., 10746448
print(f"id of integer 12: {id(12)}")  # e.g., 10746768

# The integer object 2 remains in memory, but the name refers
# to a different object after reassignment.

# A set is a collection of data and is mutable.
fruties = set()
print(f"initial fruties value: {fruties}")
print(f"id of fruties before change: {id(fruties)}")

fruties.add("banana")
fruties.add("apple")
print(f"fruties after additions: {fruties}")
print(f"id of fruties after change: {id(fruties)}")

# Unlike numbers, a set does not create a new object each time;
# it modifies the existing object in place, so its id remains the same.
# Thus, sets are mutable, while numbers are immutable.
