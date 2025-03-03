Password = "MynameisMS"
no_of_Char = len(Password)

if no_of_Char < 6:
    Strenght = "Weak"
elif no_of_Char < 10:
    Strenght = "Medium"
else:
    Strenght = "Strong"

print("Your Password is", Strenght)