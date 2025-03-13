# lambda func: A lambda function is a small anonymous function defined using the `lambda` keyword.
# It can have any number of arguments but only one expression.
# The expression is evaluated and returned.

# Use cases:
# 1. Simple functions that are used only once or a few times.
# 2. Functions that are passed as arguments to higher-order functions (e.g., map, filter, sorted).
# 3. When you want to write concise code.

# Example:
# cube of a no.

cube = lambda x: x ** 3

print(cube(3))
