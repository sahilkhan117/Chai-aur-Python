# 🌟 How to open files

# 1️⃣
# file = open('./my.txt', 'w')

# try:
#     file.write('Hello')
# finally:
#     file.close()


# 2️⃣ More relevent
with open('./my.txt', 'w') as file:
    file.write('hel')
