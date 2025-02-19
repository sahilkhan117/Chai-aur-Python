# 📊 Numbers

# Definition
# Numbers are a fundamental data type in Python that represent numeric values. There are three main types of numbers:
# - Integers (int): Whole numbers, both positive and negative.
# - Floating-point numbers (float): Numbers that contain a decimal point.
# - Complex numbers (complex): Numbers that have a real part and an imaginary part.

# Use Cases
# - Integers are commonly used for counting and indexing.
# - Floats are used in scientific calculations, financial applications, and anywhere precision is required.
# - Complex numbers are used in advanced mathematical computations, such as in electrical engineering.

# Types of Numbers

# Integer: Whole numbers
int_example = 123
negative_int_example = -5945

# Float: Decimal numbers
float_example = 3.1415
scientific_float_example = 1.98e5

# Complex: Numbers with real and imaginary parts
complex_example = 3 + 4j

# Type Conversion

# Binary
binary_example = 0b1010  # 10 in decimal

# Octal
octal_example = 0o17  # 15 in decimal

# Hexadecimal
hex_example = 0xa2  # 162 in decimal

# Example of Decimal Representation
from decimal import Decimal
from fractions import Fraction

decimal_example = Decimal('0.1')
fraction_example = Fraction(3, 4)

# Additional Examples
# Arithmetic Operations
sum_example = int_example + float_example  # Adding int and float
product_example = int_example * float_example  # Multiplying int and float

print(f"Decimal example: {decimal_example}")
print(f"Fraction example: {fraction_example}")
print(f"Sum of int and float: {sum_example}")
print(f"Product of int and float: {product_example}")
