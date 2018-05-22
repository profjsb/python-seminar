import numpy as np

def expensive_square(x):
    x = x.copy()
    y = x.copy()
    for i in range(x.size):
        x[i] = x[i] ** 2
    
    del y
    return x

def cheap_square(x):
    return x**2

square = expensive_square
#square = cheap_square

def execute():
    print("Squaring some numbers...")
    x = np.arange((5000))
    y = square(x)

#    np.testing.assert_equal(x**2, y)

if __name__ == "__main__":
    execute()
