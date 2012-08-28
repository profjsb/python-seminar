"""
PYTHON SEMINAR AY250 example iterators/generators; 
   created by Josh Bloom at UC Berkeley, 2010,2012x (ucbpythonclass+seminar@gmail.com)
"""

class jReverse(object):
     "Iterator class for looping over a sequence backwards"
     def __init__(self, data):
        self.data = data
        self.index = len(data)

     def __iter__(self):
        # this is a required of an iterating class
        return self

     def next(self):
        # we got to the front of the array
        if self.index == 0:
            self.index = len(self.data)
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class Reverse(object):
     "Iterator class for looping over a sequence backwards"
     def __init__(self, data):
        self.data = data
        self.index = len(data)

     def __iter__(self):
        # this is a required of an iterating class
        return self

     def next(self):
        # we got to the front of the array
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def countdown(start,end=0,step=1.0):
    """
show off a simple yield
step downward until end is reached. start is required, end and step are keywords.
    """
    i = start
    while (i >= end) or end == None:
        yield i
        i -= step
    raise StopIteration

def fib(start=0,end=None):
    a = long(start)
    b = start + 1L
    while ((a < end) or (end is None)):
        yield a
        a, b = b, a + b

def fib1(start=0,end=None,maxnum=100):
    """
another yield example, allowing the user to start their own fibbinoci sequence at
start (default is 0)
    """
    a = long(start)
    b = start + 1L
    n_yielded = 0
    while (n_yielded < maxnum or maxnum is None) and ((end is None) or (abs(a) < abs(end))):
        "abs needed to control against silly user starting with a negative number"
        yield a
        n_yielded += 1
        a, b = b, a + b
    
    # if we got here then we are returning instead of yielding. The countdown is finished
    # we could raise a StopException excception here...this is done for us implicitly

        
