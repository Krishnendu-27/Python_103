# -------------------------------
# Branch-wise Grocery Products
# -------------------------------

# 1️⃣ Define sets for each branch
# Why: Sets are used to store unique items without duplicates.
# How: Use curly braces {} to define a set with items.
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

# 2️⃣ Print initial sets
# Why: To see the items available in each branch.
# How: Use the print() function to display the set.
print(branch_a_products)
print(branch_b_products)

# 3️⃣ Union of both branches
# Why: To get all unique products available in either branch.
# How: Use the | operator to combine sets without duplicates.
union = branch_a_products | branch_b_products
print(union)

# 4️⃣ Intersection of both branches
# Why: To find products that are common to both branches.
# How: Use the & operator to get items present in both sets.
intersection = branch_a_products & branch_b_products
print(intersection)

# 5️⃣ Difference (products in branch A but not in branch B)
# Why: To identify items that are exclusive to branch A.
# How: Use the - operator to subtract sets.
elements_in_a_not_b = branch_a_products - branch_b_products
print(elements_in_a_not_b)

# 6️⃣ Check membership
# Why: To see if a specific product (e.g., 'ketchup') is available in branch A.
# How: Use the `in` keyword; it returns True or False.
result = 'ketchup' in branch_a_products
print(result)

# 7️⃣ Define unmodifiable essential items (frozenset)
# Why: Some items should not be changed accidentally (immutable set).
# How: Convert a set into frozenset using frozenset().
essential_items = {"milk", "bread", "ketchup"}
essential_items = frozenset(essential_items)
print(essential_items)
