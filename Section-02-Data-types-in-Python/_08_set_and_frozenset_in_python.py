# -------------------------------
# Anime Collections using Sets
# -------------------------------

# 1️⃣ Define sets for essential and optional anime
# Why: Sets store unique items and order does not matter.
# How: Use curly braces {} to define a set of anime names.
essntial_anime = {"naruto", "one piece", "bleach"}
optinal_anime = {"86", "violet evergarden", "naruto"}

# 2️⃣ Union of sets (all unique anime)
# Why: To combine all anime names from both essential and optional collections without duplicates.
# How: Use the | operator to get the union of two sets.
all_anime = essntial_anime | optinal_anime
print(f"All anime names: {all_anime}")

# 3️⃣ Intersection of sets (common anime)
# Why: To find anime that are present in both essential and optional sets.
# How: Use the & operator to get common elements.
common_anime = essntial_anime & optinal_anime
print(f"The common anime: {common_anime}")

# 4️⃣ Difference of sets (anime only in essential)
# Why: To find anime that are only in the essential set and not in optional.
# How: Use the - operator to subtract one set from another.
only_essntial_anime = essntial_anime - optinal_anime
print(f"The essential anime only: {only_essntial_anime}")

# 5️⃣ Membership test
# Why: To check if a specific anime (e.g., 'naruto') is in the essential collection.
# How: Use the `in` keyword; it returns True or False.
print(f"Is 'naruto' in essential anime? {'naruto' in essntial_anime}")

# 6️⃣ Frozenset (immutable set)
# Why: Sometimes you want a set that cannot be modified accidentally.
# How: Convert a normal set into frozenset using frozenset().
anime_constants = frozenset(essntial_anime)
print(f"Immutable anime set: {anime_constants}")
