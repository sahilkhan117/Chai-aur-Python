# multiple return

#  return area and circumstarence of circle

import math

def circle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return area, circum

a, c = circle(7)
print("Area:", a, "Circum:", c)