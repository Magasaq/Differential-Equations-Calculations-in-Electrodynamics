%%iteration
%%l - iteration veriaty 


A = [N:N]
b = [N:1]

for k = 1:N
	for i = 1:N
		A[k:i] =  -Mat[k:i]/Mat[k:k]
		b[k] = I_c[k]/Mat[k:k]
		A[k:k] = 0
while(norm(Psi) - norm(Psi_new) < exp^(-10))	
	Psi_new = Psi_init + A*Psi
	Psi = Psi_new


