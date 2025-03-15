# 1. Lecsis Scoping / Climbing ⬆️🪜🧗🏻
    # agar andar na mile to bahar ja sakte hai par bahar se andar nahi aa sakte hai

username = "sahil"
def func():
    # username = "me"
    print(username)

print(username)
func()
    # Output: Sahil Sahil ⬆️☝🏻


# 2. Global oprator
# x = 99

# def func2(y):
#     z = x + y
#     return z

# print(func2(1))
# 👇🏻👇🏻⬇️⬇️
# def func3():
#     global x  # 😵very problamatic process to nahi karna hai use ise
#     x = 12

# func3() # change the value of x 
# print(x)

# 3. Closure / Bag Theory
    # jab ek func ko return ya store karte hai kisi variable me to us func ke sath-saht sari associated values of variables bhi jati hai jo us func me use hui hai

x = 99
def f1():
    # x = 88
    def f2():
        print(x)
    return f2
res = f1()
res()

    # Another Example of ĊĹÔŚĚŔ
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2) # ref: x ** 2
g = chaicoder(3) # ref: x ** 3

# print(f) # <function chaicoder.<locals>.actual at 0x00000212FDA49300>z
# print(g) # <function chaicoder.<locals>.actual at 0x00000212FDA493A0>z

print(f(3)) # 9
print(g(3)) # 27
