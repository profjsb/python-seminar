import numpy as np
import stuff

x = np.linspace(0, 2*np.pi, 20)

y = stuff.do_compute(x)
y2 = np.sin(x)

if abs(y - y2).max() < 1e-10:
    print "All OK!"
else:
    print "Something is wrong..."
