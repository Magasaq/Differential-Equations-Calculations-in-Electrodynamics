
### Solution of the scheme
#The given scheme can be converted to a differential equation: $i^{'} + i = 0$

from math import *
import matplotlib.pyplot as plt

# Initial Values
i = 0
i_deriv = 1
t = 0
tf = 100
h = 0.0002
Noumber_of_it = int((tf - t) / h)
iarr = []

# Definition of differential equations
def func(i):
    return -i 

for _ in range(Noumber_of_it):
    k1 = func(i)
    k2 = func(i + 0.5 * h * k1)
    k3 = func(i + 0.5 * h * k2)
    k4 = func(i + h * k3)
    
    i_deriv = i_deriv + (h / 6) * (k1 + 2 * (k2 + k3) + k4)
    i = i + i_deriv * h
    t = t + h
    iarr.append(i)

plt.plot(np.arange(0, tf, h), iarr)
plt.xlabel("Time")
plt.ylabel("i")
plt.show()