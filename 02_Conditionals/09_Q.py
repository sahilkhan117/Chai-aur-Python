year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The Year", year, "is a Leap Year")
else:
    print("The Year", year, "is NOT a Leap Year")