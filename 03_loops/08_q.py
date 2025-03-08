n = 5

is_prime = True

if n > 1:
    for i in range(2, int(n/2)):
        if n % i == 0:
            is_prime = False
            break

print(is_prime)