
"""
Created on Wed Dec 30 00:43:23 2020

@author: HP
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
f=lambda x:x**2+3
x=np.linspace(-1,2,200)
fx=f(x)
gx=np.ones(fx.shape)
plt.plot(x,fx,gx)
plt.fill_between(x,fx,gx)
plt.xlim((-3,3))
plt.title("Area between two curves")
plt.show()