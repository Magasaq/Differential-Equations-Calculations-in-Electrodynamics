import sympy as sym
import numpy as np
import math
from io import StringIO   # StringIO behaves like a file object
from numpy.linalg import inv


N = 100

def FNew(N, X, Phi, I):


	F = np.zeros(N)

	for k in range(1,N):
		for j in range(1,N):
			for j in range(1,N):
				F[k] = F[k] + math.cos(2*math.pi*Phi[k] / N + X[i] - X[j])

	    	
	    F[k] = F[k] - (I[k] * N)**2

def  Jacob(N, X, Phi):
	
	W = np.zeros((N,N))

	for k in range(1,N):
		for i in range(1,N):
			for j in range(1,N):
				W[k,i] = W[k,i] - math.sin(2*math.pi*Phi[k]*(i-j)/N + X[i] - X[j])



X = np.zeros(N)
Phi = StringIO("Field.txt")
I = StringIO("Ic.txt")
N = np.size(I, axis = 1)

W = Jacob(N, X, Phi)
F = FNew(N, X, Phi, I)
Winv = inv(W)
XNew = X - Winv * F