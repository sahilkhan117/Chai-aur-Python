# Lists

# Definition
# Lists are ordered, mutable collections of items in Python.

# Use Cases
# - Lists are commonly used to store collections of items, such as user inputs, data records, or any ordered collection.
# - They allow for easy access and manipulation of data.

# Characteristics of Lists
# Lists are ordered, mutable collections of items.

# Initialization
tea_variaties = ['Black', 'White', 'Oolong', 'Green']

# Accessing Elements
first_tea = tea_variaties[0]  # 'Black'

# Slicing
sliced_tea = tea_variaties[1:3]  # ['White', 'Oolong']

# List Methods
tea_variaties.append('Lemon')  # Adding an item
tea_variaties.remove('Lemon')  # Removing an item

# Additional Examples
# List Comprehension
squared_numbers = [x**2 for x in range(10)]  # Squaring numbers from 0 to 9

print(f"First tea: {first_tea}")
print(f"Sliced tea: {sliced_tea}")
print(f"Squared Numbers: {squared_numbers}")
