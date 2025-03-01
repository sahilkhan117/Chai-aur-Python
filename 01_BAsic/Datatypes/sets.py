# 🛠️ Sets

# Definition
# Sets are unordered collections of unique items in Python.

# Use Cases
# - Sets are commonly used to eliminate duplicate entries and to perform mathematical set operations like union and intersection.

# Characteristics of Sets
# Sets are unordered collections of unique items.

# Initialization
unique_numbers = {1, 2, 3, 4, 5}

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a | set_b  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a & set_b  # {3}

# Additional Examples
# Adding and Removing Items
unique_numbers.add(6)  # Adding an item
unique_numbers.remove(1)  # Removing an item

print(f"Union of sets: {union_set}")
print(f"Intersection of sets: {intersection_set}")
print(f"Unique numbers after adding and removing: {unique_numbers}")
