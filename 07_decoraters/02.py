# debugging function call
# calculate no. of parameters that are callled in a function

def no_of_parameters(func):
    para = {}
    def wrapper(*args, **kwargs):
        para["arg"] = ", ".join(str(arg) for arg in args)
        para["kwarg"] = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"{func.__name__} has Args {para["arg"]} and KWargs {para["kwarg"]}")
        return func(*args, **kwargs)
    return wrapper

@no_of_parameters
def hi():
    pass

hi()

@no_of_parameters
def Greet(name, greet="Hello"):
    return f"{greet}!, {name}"

print(Greet("sahil", greet="hi"))