num = int(input("Enter Age: "))

if num < 13:
    print("Child")
elif num < 20:
    print("Teenager")
elif num < 60:
    print("Adult")
else:
    print("Senior")