# Basics of List in Python
# in python list are same as array same functionality same data structer

todolist = ["wake-up", "workout", "meditation", "eat"]
print(f"Initial todo list: {todolist}")

# append(): Add an item to the end of the list
todolist.append("go washroom")
print(f"After append: {todolist}")

# insert(): Insert an item at a specific position
todolist.insert(2, "rest")  # Insert 'rest' at index 2
print(f"After insert at index 2: {todolist}")

# extend(): Add all items from another list
extra_tasks = ["call mom", "check email"]
todolist.extend(extra_tasks)  # Adds each item from extra_tasks to todolist
print(f"After extend with extra_tasks: {todolist}")

# remove(): Remove the first occurrence of an item
todolist.remove("eat")  # Removes 'eat' if present
print(f"After remove 'eat': {todolist}")

# pop(): Remove and return the last item (or item at index)
last_task = todolist.pop()  # Removes and returns the last item
print(f"Popped task: {last_task}")
print(f"After pop: {todolist}")

# index(): Find the index of a specific item
position = todolist.index("meditation")  # Returns index of 'meditation'
print(f"Index of 'meditation': {position}")

# count(): Count how many times an item appears
count_rest = todolist.count("rest")  # Count how many times 'rest' appears
print(f"Count of 'rest': {count_rest}")

# reverse(): Reverse the list in-place
todolist.reverse()
print(f"After reverse: {todolist}")

# sort(): Sort the list in alphabetical order
todolist.sort()
print(f"After sort: {todolist}")

# sorted(): Get a new sorted list without modifying the original
sorted_list = sorted(todolist)
print(f"Sorted copy: {sorted_list}")
print(f"Original list remains sorted: {todolist}")

# clear(): Remove all items from the list
todolist.clear()
print(f"After clear: {todolist}")  # Should print []
