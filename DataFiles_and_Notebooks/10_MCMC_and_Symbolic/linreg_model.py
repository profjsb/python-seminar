# linreg_model.py

"""
A model for doing pymc linear regression

switchpoint: s ~ U(0,111)
early_mean: e ~ Exp(1.)
late_mean: l ~ Exp(1.)
disasters: D[t] ~ Poisson(early if t <= s, l otherwise)
"""

import pymc
import numpy as np
import pandas as pd

# load in data
D = pd.read_csv('data_BirthRate.txt')
X = D.ix[:,1:3]
change = D['change']

#priors
b0 = pymc.Normal('b0', 0.0, 0.001, value=0)
b1 = pymc.Normal('b1', 0.0, 0.001, value=0)
b2 = pymc.Normal('b2', 0.0, 0.001, value=0)
sigma = pymc.Uniform('sigma', 0.0, 200.0, value=20)
    
#model
@pymc.deterministic(plot=False)
def modelled_y(X=X, b0=b0, b1=b1, b2=b2):
    return b0 + b1*X.ix[:,0] + b2*X.ix[:,1]
 
#likelihood
y = pymc.Normal('y', mu=modelled_y, tau=1.0/sigma**2, value=change, observed=True)