# with **kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(p="sahil", c="B.tech")