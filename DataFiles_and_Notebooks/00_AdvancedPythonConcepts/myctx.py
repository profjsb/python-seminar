"""
PYTHON SEMINAR AY250 example context managers and decorators 
   created by Josh Bloom at UC Berkeley, 2010,2012,2013 (ucbpythonclass+seminar@gmail.com)
"""

class MyDecor:
    def __enter__(self):
        print "Entered a wonderful technicolor world. Build it up" 
        
    def __exit__(self,*args):
        print "...exiting this wonderful world. Tear it down."
        
class MyDecor1:
    
    def __init__(self,expression="None"):
        self.expression = expression
    def __enter__(self):
        print "Entered a wonderful technicolor world. Build it up" 
        return eval(self.expression)
    def __exit__(self,*args):
        print "...exiting this wonderful world. Tear it down."


def entryExit(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

def introspect(f):
    def wrapper(*arg,**kwarg):
        print "Function name = %s" % f.__name__
        print " docstring = %s" % f.__doc__
        if len(arg) > 0:
            print "   ... got passed args: %s " % str(arg)
        if len(kwarg.keys()) > 0:
            print "   ... got passed keywords: %s " % str(kwarg)
        return f(*arg,**kwarg)
    return wrapper

@introspect
def myrange(*arg,**kwarg):
    return range(*arg,**kwarg)

def accepts(*types):
    """ Function decorator. Checks that inputs given to decorated function
      are of the expected type.
  
      Parameters:
      types -- The expected types of the inputs to the decorated function.
               Must specify type for each parameter.
    """
    def decorator(f):
        def newf(*args):
            assert len(args) == len(types)
            argtypes = tuple(map(type, args))
            if argtypes != types:
                a = "in %s "  % f.__name__
                a += "got %s but expected %s" % (argtypes,types)
                raise TypeError, a
            return f(*args)
        return newf
    return decorator
    
