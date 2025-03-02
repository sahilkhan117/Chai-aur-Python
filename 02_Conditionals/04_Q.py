# Determine A Fruit is Ripe, Unripe or Overripe
# e.g. Banana : {Yellow:Ripe, Green:Unripe, Brown:Overripe}

fruit = "Banana"
Color = "Yellow"

Check = {
    "Banana": {"Yellow": "Ripe", "Green": "Unripe", "Brown": "Overripe"},
    "Mango": {"Yellow": "Ripe", "Green": "Unripe", "Brown": "Overripe"},
}

print("The", Color, fruit, "is", Check[fruit][Color])