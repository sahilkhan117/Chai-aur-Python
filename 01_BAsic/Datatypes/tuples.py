# 🎯 Tuples

# Definition
# Tuples are ordered, immutable collections of items in Python.

# Use Cases
# - Tuples are commonly used to store fixed collections of items, such as coordinates or RGB color values.
# - They are useful when you want to ensure that the data cannot be modified.

# Initialization
dimensions = (1920, 1080)

# Accessing Elements
width = dimensions[0]  # 1920
height = dimensions[1]  # 1080

# Additional Examples
# Tuple Packing and Unpacking
packed_tuple = (1, 2, 3)
(a, b, c) = packed_tuple  # Unpacking values

print(f"Width: {width}, Height: {height}")
print(f"Unpacked values: a={a}, b={b}, c={c}")
