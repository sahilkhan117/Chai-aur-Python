# Calculate sum of even numbers up to a given number n

n = 10
sum_of_even = 0

for i in range(n+1):
    if i%2 == 0:
        sum_of_even += 1

print(sum_of_even)