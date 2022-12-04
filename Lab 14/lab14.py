
import numpy as np
import pandas as pd
from scipy import stats
from random import random

balls = np.arange(1, 1000)

emptybin = []

for N in balls:
    
    bins = np.zeros(N)
    
    for b in range(N):
        bins[int(N * random())] += 1
        
        
    emptybin.append(np.sum(bins == 0))
 
import matplotlib.pyplot as plt

plt.plot(balls, emptybin)
plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(balls, emptybin)

print("\n")
print("SciPy Linear Regression Solution")
print(" Slope = ", slope)
print(" Intercept = ", intercept)
print(" R-squared = ", r_value**2)

"""
SciPy Linear Regression Solution 
 slope: 0.36837836634229415
 intercept: -0.02602000798390236 
 rvalue: 0.997749733854947
"""