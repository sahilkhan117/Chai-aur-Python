# recursive func: A function that calls itself is known as a recursive function.

# factorial

def factorial(n):
    # Base Case
    if n == 0:
        return 1
    
    # recursive func
    return n * factorial(n - 1)


print(factorial(7))