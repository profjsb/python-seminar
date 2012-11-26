from numpy_basic import foo
import numpy as np

x = np.zeros((5, 7))
print "Before:"
print x

y = foo(x)

print "After:"
print y
