# 📚 Dictionaries

# Definition
# Dictionaries are unordered collections of key-value pairs in Python.

# Use Cases
# - Dictionaries are commonly used to store data with labels, such as user profiles, configuration settings, or any associative data.

# Initialization
person = {'name': 'Bob', 'age': 32}

# Accessing Values
name = person['name']  # 'Bob'

# Dictionary Methods
person['age'] = 33  # Update value

# Get method
age = person.get('age')  # 33

# Additional Examples
# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

print(f"Name: {name}, Age: {age}")
