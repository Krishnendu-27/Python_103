"""
Shopping List Program
---------------------
This script demonstrates how to manage a grocery shopping list using basic Python list operations.
Each step includes an explanation of what function is used, why it is needed, and how it works.
"""

# Step 1: Create a grocery list
# Using a list to store grocery items allows easy addition, removal, and sorting.
my_cart = ["apples", "bananas", "milk"]
print("Initial list:", my_cart)

# Step 2: Append - Add an item to the end of the list
# .append(item) adds the specified element to the end.
my_cart.append("bread")
print("\nAfter append (added 'bread'):", my_cart)

# Step 3: Insert - Add an item at a specific position
# .insert(index, item) adds the item at the given index.
# Here, index 0 means inserting 'ketchup' at the start of the list.
my_cart.insert(0, "ketchup")
print("\nAfter insert (added 'ketchup' at beginning):", my_cart)

# Step 4: Remove - Delete a specific item by value
# .remove(item) deletes the first occurrence of that item from the list.
my_cart.remove("bananas")
print("\nAfter remove (removed 'bananas'):", my_cart)

# Step 5: Pop - Remove and return the last item
# .pop() removes the last item and returns it. This is useful when we need to use or display the removed item.
removed_item = my_cart.pop()
print("\nAfter pop (removed last item):", my_cart)
print("Removed item:", removed_item)

# Step 6: Extend - Add multiple items at once
# .extend(iterable) adds each element from another list (or iterable) to the current list.
# This is better than multiple .append() calls.
my_cart.extend(["rice", "butter"])
print("\nAfter extend (added 'rice' and 'butter'):", my_cart)

# Step 7: Sort - Arrange list items in alphabetical order
# .sort() modifies the list in place to sort the items.
my_cart.sort()
print("\nAfter sort (alphabetical order):", my_cart)

# Step 8: Reverse - Reverse the current order of items
# .reverse() flips the order of elements in place.
my_cart.reverse()
print("\nAfter reverse (reversed order):", my_cart)

# Step 9: List concatenation using + operator
# Using + joins two lists together into a new list.
# Here, we add 'juice' and 'jam' to create a new list called new_cart.
new_cart = my_cart + ["juice", "jam"]
print("\nAfter concatenation (+ operator):", new_cart)

# Step 10: List repetition using * operator
# The * operator duplicates the list a given number of times.
# This is useful for repeating elements or testing operations on larger lists.
doubled_cart = my_cart * 2
print("\nAfter duplication (* operator):", doubled_cart)

# Step 11: Convert a string to a list using .split()
# .split() breaks a string into a list of words based on spaces by default.
# Useful for processing text inputs.
string = "tomato cucumber spinach"
vegetable_list = string.split()
print("\nConverted string to list using .split():", vegetable_list)

print("\n✅ Shopping list operations completed successfully!")
