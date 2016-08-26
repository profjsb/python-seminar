#!/usr/bin/env python
"""
Breakout answer from the Python seminar class (week #1)
  - get's us used to using yield
created by Josh Bloom at UC Berkeley, 2010, 2012, 2016 (ucbpythonclass+seminar@gmail.com)
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
        yield next(g)

def accel(series):
    """ accelerate the series convergence.... we have Euler to thank for this"""
    s0 = next(series) # Sn-1
    s1 = next(series) # Sn
    s2 = next(series) # Sn+1
    while True:
        yield s2 - ((s2 - s1)**2)/(s0 - 2.0*s1 + s2)
        s0, s1, s2 = s1, s2, next(series)

how_close = 0.001  # 0.1%
firstbunch = \
   list(first_n(pi_series(stop_when_close=True,close=how_close),\
                 1000))

print("{0:.7f} ... {2}% stops after: {1:d} iterations\n"
      .format(firstbunch[-1],len(firstbunch),how_close*100))

print("Last breakout question:") 
print("*"*30)

b = accel(pi_series())
print("fractional accuracy first 8 in accelerated series:")

for i in range(8): 
    print("{:.4e} ".format(abs(next(b) - math.pi)/math.pi))
    
a = pi_series()
print("\n" + "-"*30)
print("\nfractional accuracy first 8 in un-accelerated series:")
for i in range(8): 
    print("{:.4e} ".format(abs(next(a) - math.pi)/math.pi))