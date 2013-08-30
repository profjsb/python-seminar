#!/usr/bin/env python
"""
Breakout answer from the Python seminar class (week #1)
  - get's us used to using yield
created by Josh Bloom at UC Berkeley, 2010, 2012 (ucbpythonclass+seminar@gmail.com)
"""
import math

def pi_series(stop_when_close=False,close=0.00001):
    """ generate the series 4*(1 - 1/3 + 1/5 - 1/7 ...), which should be pi.
      We have Libnitz to thank for this
    """
    thesum = 0.0
    i = 1.0 ; thesign = 1.0
    while ((not stop_when_close) or (abs(4.0*thesum - math.pi) > close*math.pi)):
        thesum += thesign/i
        yield 4.0*thesum
        i += 2.0 
        thesign *= -1.0  ## change the sign in front of that term
    
    # notice that you don't need a StopIteration call

def first_n(g, n):
    for i in range(n):
        yield g.next()

def accel(series):
    """ accelerate the series convergence.... we have Euler to thank for this"""
    s0 = series.next() # Sn-1
    s1 = series.next() # Sn
    s2 = series.next() # Sn+1
    while True:
        yield s2 - ((s2 - s1)**2)/(s0 - 2.0*s1 + s2)
        s0, s1, s2 = s1, s2, series.next()

# yeilds ... we have Guido to thank for this.
# he's happy about yeild from, coming in python 3.3 ... he accepted on 26th June, 2011.
# see https://plus.google.com/115212051037621986145/posts/XkGsnBgdzVk

firstbunch = list(first_n(pi_series(stop_when_close=True,close=0.001),1000))
print "{0:.7f} ... 0.1% stops after: {1:d} iterations".format(firstbunch[-1],len(firstbunch))
print "Last breakout question:" ; print("*"*30)
b = accel(pi_series())
print "fractional accuracy first 8 in accelerated series....:"
for i in range(8): 
    print "{:.4e} ".format(abs(b.next() - math.pi)/math.pi)
a = pi_series()
print "\n" + "-"*30
print "\nfractional accuracy first 8 in un-accelerated series....:"
for i in range(8): 
    print "{:.4e} ".format(abs(a.next() - math.pi)/math.pi)
