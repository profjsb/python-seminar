'''
Python Computing for Science
Lecture 0 (Advanced Python Language Concepts) -- breakout solution
  - get's us used to using yield
created by Josh Bloom at UC Berkeley, 2010, 2012, 2013 (ucbpythonclass+seminar@gmail.com)

ishivvers@berkeley.edu, joshbloom@berkeley.edu
'''

import numpy as np

def approx_Pi():
    ''' oo-series pi approximator, as a generator '''
    val = 0.
    d = 0
    while True:
        # determine this step's fraction
        if d%2 == 0:
            sign = 1.
        else:
            sign = -1.
        val += sign/(1.+2.*d)
        # yield the current approximation
        yield 4.*val
        d +=1
    # notice that you don't need a StopIteration call, but also notice that this
    # would enter an infinite loop if you called it like this:
    # >>> for value in approx_quarterPi(): print value
    #
    # pro tip:
    # control+C will kill it, if you accidentally do enter something like the above.

def approx_Pi_2(accuracy=.001, print_result=False):
    ''' oo-series pi approximator, which stops once it gets to within <accuracy> of the true value '''
    val = 0.
    d = 0
    while True:
        # determine this step's fraction
        if d%2 == 0:
            sign = 1.
        else:
            sign = -1.
        val += sign/(1.+2.*d)
        # yield the current approximation
        yield 4.*val
        d +=1
        # if we're accurate enough, break out of the infinite loop
        if abs(np.pi - 4.*val)<accuracy:
            break
    if print_result: print ' got a value of {} after {} steps\n accuracy: {}'.format(4.*val, d, abs(np.pi-4*val))
    raise StopIteration
    # much better, no risk of infinite loops!
    # note that this function exits when it hits StopIteration, though, so the print_result
    # statement MUST be BEFORE the raise statement

#EXAMPLE:
for val in approx_Pi_2(print_result=True): continue



def accelerate(series):
    """ use Euler's Transform to accelerate convergence of <series> """
    s0 = series.next() # Sn-1
    s1 = series.next() # Sn
    s2 = series.next() # Sn+1
    while True:
        yield s2 - ((s2 - s1)**2)/(s0 - 2.0*s1 + s2)
        s0, s1, s2 = s1, s2, series.next()


# EXAMPLE: converge much faster using accelerate()
steps = 0
for val in accelerate(approx_Pi()):
    print val
    steps +=1
    if abs(np.pi - val)<.001:
        break
print 'took {} steps to get a value of {}\naccuracy: {}'.format(steps, val, abs(np.pi-val))
