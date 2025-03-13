# func with *args

# takes variabilt or multiple no. as arguments and sum all of them

def sum_All(*args):
    return sum(args)

print(sum_All(1, 2))
print(sum_All(1, 2, 3, 4))
print(sum_All(1, 2, 3, 4, 5, 6))