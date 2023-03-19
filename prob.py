from math import *
import numpy as np
import math 

a = np.array(15)
b = np.array(15)
p = 24

def func( a, b):
	for i in range(1,15):
		for j in range(1,15):
			if i == j:
				continue

			
			h =  cos(p*(j-i) + a[j] - b[i])
	
	return h


print(func(a,b))