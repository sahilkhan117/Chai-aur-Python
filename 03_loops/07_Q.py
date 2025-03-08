# validate user in put between 1 and 10

while True:
    n = int(input("Enter a No.: "))
    if 1 <= n <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number")

