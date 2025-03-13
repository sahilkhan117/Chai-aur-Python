# use of Yeild
# store any func previous work 

def even_generator(lim):
    for i  in range(2, lim+1, 2):
        # return i
        yield i
    

for i in even_generator(10):
    print(i)