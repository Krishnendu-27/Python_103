# Create a dictionary
anime_list = dict(type="anime", size="1tb", most_genre="action, thriller")
print(anime_list)

# Another way to create a dictionary
another_anime_list = {}
another_anime_list["anime_name"] = "Naruto"
another_anime_list["episodes"] = 500
print(another_anime_list)
print(another_anime_list["anime_name"])
# Add a new key-value pair
another_anime_list["main_villain"] = "Kaguya"
print(another_anime_list)

# Membership testing
print(f"Is 'Naruto' present in anime list? {'Naruto' in another_anime_list}")

# Print all keys, values, and items
print(f"All keys are: {another_anime_list.keys()}")
print(f"All values are: {another_anime_list.values()}")
print(f"All items are: {another_anime_list.items()}")

# Remove the last inserted item using popitem()
main_villain = another_anime_list.popitem()
print(main_villain)
print(another_anime_list)

# To remove a specific element, use del
del another_anime_list["episodes"]
print(another_anime_list)

# To avoid a crash in Python, we can use get()
is_available = anime_list.get("type", "type not found")
print(is_available)
