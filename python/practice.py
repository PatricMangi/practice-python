def square(x):
    y=x**x
    return y

def multi(x):
    y=x*x
    return y

def add(x):
    y=x+x
    return y

def rae(x):
    a=add(x)
    b=multi(x)
    c=square(x)

    return a,b,c

print(rae(5))
    
def square(x):
    y=x**x
    z=x/7
    return y,z
def add(x):

    y=x*3

    z=x/3

    return y,z
print(square(3))

def rae(x):
    c=square(x)
    a=add(x)
    return c,a

print(rae(5))
