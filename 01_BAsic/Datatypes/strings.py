# 📝 Strings

# Definition
# Strings are sequences of characters enclosed in quotes. They are used to represent text data.

# Use Cases
# - Strings are commonly used for text processing, user input, and formatting output.
# - They can be manipulated using various methods for tasks such as searching, replacing, and formatting.

# Initialization
chai = "Masala chai"

# String Manipulation

# Slicing
first_char = chai[0]  # 'M'
sliced_chai = chai[0:6]  # 'Masala'
last_char = chai[-1]  # 'i'

# String Methods
space_chai = '    masala    chai    '
stripped_chai = space_chai.strip()  # 'masala    chai'

# Length
length_of_chai = len(chai)  # 10

# Upper and Lower Case
upper_case_chai = chai.upper()  # 'MASALA CHAI'
lower_case_chai = chai.lower()  # 'masala chai'

# Formatting
name = 'Bob'
age = 32
sentence = f'My name is {name} and I am {age} years old'

# Split & Join
s = 'Masala, Ginger, Lemon, Ice'
split_list = s.split(', ')  # ['Masala', 'Ginger', 'Lemon', 'Ice']
joined_string = ' '.join(['Masala', 'Ginger', 'Lemon', 'Ice'])  # 'Masala Ginger Lemon Ice'

# Additional Examples
# Replacing
replaced_string = chai.replace('Masala', 'Ginger')  # 'Ginger chai'

print(f"Stripped Chai: {stripped_chai}")
print(f"Upper Case Chai: {upper_case_chai}")
print(f"Sentence: {sentence}")
print(f"Replaced String: {replaced_string}")
