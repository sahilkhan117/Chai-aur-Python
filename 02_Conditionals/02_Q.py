age = int(input("Enter Age: "))
day = input("Is There Wednesday (y/n): ")

price = 12 if age < 18 else 8

if day == 'y':
    price -= 2

print("Ticket Price is $", price)